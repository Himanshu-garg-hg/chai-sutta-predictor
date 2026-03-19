import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
import pickle
from pathlib import Path

# versioning
model_version = os.getenv("MODEL_VERSION", "v1")

# Get the project root directory
models_dir = Path(__file__).resolve().parents[1] / "models"
models_dir.mkdir(parents=True, exist_ok=True)

data_path = Path(__file__).resolve().parents[1] / "data" / "chai_sutta_data.csv"

# Load dataset
print(f"Loading dataset from: {data_path}")
df = pd.read_csv(data_path)

# Encode categorical data
le_gender = LabelEncoder()
df['gender'] = le_gender.fit_transform(df['gender'])

le_habit = LabelEncoder()
df['habit'] = le_habit.fit_transform(df['habit'])

# Features and target
X = df[['age', 'gender', 'taunts']]
y = df['habit']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Accuracy
accuracy = model.score(X_test, y_test)
print(f"Model Accuracy: {accuracy}")

# Save model + encoders using versioned filenames
model_path = models_dir / f"chai_sutta_model_{model_version}.pkl"
with open(model_path, "wb") as f:
    pickle.dump(model, f)

with open(models_dir / f"gender_encoder_{model_version}.pkl", "wb") as f:
    pickle.dump(le_gender, f)

with open(models_dir / f"habit_encoder_{model_version}.pkl", "wb") as f:
    pickle.dump(le_habit, f)

print(f"[SUCCESS] Model saved: {model_path}")