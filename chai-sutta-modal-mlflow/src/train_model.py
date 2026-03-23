import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
import pickle
from pathlib import Path

# 🔥 NEW: MLflow import
import mlflow
import mlflow.sklearn

# versioning
model_version = os.getenv("MODEL_VERSION", "v1")

# 🔥 NEW: set experiment
mlflow.set_experiment("chai-sutta-predictor")

# Get the project root directory
models_dir = Path(__file__).resolve().parents[1] / "models"
models_dir.mkdir(parents=True, exist_ok=True)

data_path = Path(__file__).resolve().parents[1] / "data" / "chai_sutta_data.csv"

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

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 🔥 NEW: start MLflow run
with mlflow.start_run(run_name=f"model_{model_version}"):

    # Train model
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)

    # Accuracy
    accuracy = model.score(X_test, y_test)
    print(f"Model Accuracy: {accuracy}")

    # 🔥 NEW: log params
    mlflow.log_param("model_type", "RandomForest")
    mlflow.log_param("random_state", 42)
    mlflow.log_param("model_version", model_version)

    # 🔥 NEW: log metrics
    mlflow.log_metric("accuracy", accuracy)

    # 🔥 NEW: log model
    mlflow.sklearn.log_model(model, "model")

    # Save model locally (existing logic)
    model_path = models_dir / f"chai_sutta_model_{model_version}.pkl"

    model_package = {
        "model": model,
        "gender_encoder": le_gender,
        "habit_encoder": le_habit,
        "version": model_version,
        "accuracy": accuracy
    }

    with open(model_path, "wb") as f:
        pickle.dump(model_package, f)

    print(f"[SUCCESS] Model package saved: {model_path}")