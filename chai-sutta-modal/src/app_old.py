from flask import Flask, request, jsonify, render_template_string
import pickle
import numpy as np
import os
from pathlib import Path

app = Flask(__name__)

# Get the absolute path to models directory
BASE_DIR = Path(__file__).parent.parent
MODELS_DIR = BASE_DIR / "models"

# Load model & encoders with error handling
try:
    model = pickle.load(open(MODELS_DIR / "chai_sutta_model.pkl", "rb"))
    le_gender = pickle.load(open(MODELS_DIR / "gender_encoder.pkl", "rb"))
    le_habit = pickle.load(open(MODELS_DIR / "habit_encoder.pkl", "rb"))
    print("✅ Models loaded successfully")
except FileNotFoundError as e:
    print(f"❌ Error loading models: {e}")
    raise

# Simple HTML UI
HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>Chai Sutta Predictor</title>
</head>
<body>
    <h2>☕🚬 Chai Sutta Predictor</h2>
    <form method="post" action="/predict_form">
        Age: <input type="number" name="age" required><br><br>
        
        Gender:
        <select name="gender">
            <option value="male">Male</option>
            <option value="female">Female</option>
        </select><br><br>
        
        Taunts: <input type="number" name="taunts" required><br><br>
        
        <input type="submit" value="Predict">
    </form>

    {% if prediction %}
        <h3>Prediction: {{ prediction }}</h3>
    {% endif %}
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML_PAGE)

@app.route("/predict_form", methods=["POST"])
def predict_form():
    try:
        age = int(request.form["age"])
        gender = request.form["gender"]
        taunts = int(request.form["taunts"])

        # Encode gender
        gender_encoded = le_gender.transform([gender])[0]

        # Predict
        prediction = model.predict([[age, gender_encoded, taunts]])
        result = le_habit.inverse_transform(prediction)[0]

        return render_template_string(HTML_PAGE, prediction=result)
    except Exception as e:
        return render_template_string(HTML_PAGE, prediction=f"Error: {str(e)}")

# API endpoint (optional for future use)
@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json

        age = data["age"]
        gender = data["gender"]
        taunts = data["taunts"]

        gender_encoded = le_gender.transform([gender])[0]
        prediction = model.predict([[age, gender_encoded, taunts]])
        result = le_habit.inverse_transform(prediction)

        return jsonify({"prediction": result[0]})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)