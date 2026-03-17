import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
import pickle
import os
from pathlib import Path

# Get the project root directory
project_root = Path(__file__).parent.parent
data_path = project_root / "data" / "chai_sutta_data.csv"
models_dir = project_root / "models"

# Create models folder if not exists
models_dir.mkdir(parents=True, exist_ok=True)

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

# Save model
model_path = models_dir / "chai_sutta_model.pkl"
gender_encoder_path = models_dir / "gender_encoder.pkl"
habit_encoder_path = models_dir / "habit_encoder.pkl"

with open(model_path, "wb") as f:
    pickle.dump(model, f)

with open(gender_encoder_path, "wb") as f:
    pickle.dump(le_gender, f)

with open(habit_encoder_path, "wb") as f:
    pickle.dump(le_habit, f)

print(f"[SUCCESS] Model saved in {models_dir} folder")