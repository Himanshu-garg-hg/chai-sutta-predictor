# ☕🚬 Chai-Sutta Predictor (End-to-End MLOps Project)

---

## 📌 Overview

This project demonstrates a **complete MLOps flow**:

```
Dataset → Model Training → Model Artifact (.pkl) → Flask API → Docker Container
```

You will:

* Train a Machine Learning model
* Save it as a `.pkl` file
* Serve it using a Flask API
* Containerize using Docker

---

# 🧱 Project Structure

```
chai-sutta-ml/
│
├── data/
│   └── chai_sutta_data.csv
│
├── models/
│   ├── chai_sutta_model.pkl
│   ├── gender_encoder.pkl
│   └── habit_encoder.pkl
│
├── src/
│   ├── train_model.py
│   └── app.py
│
├── requirements.txt
├── Dockerfile
└── README.md
```

---

# ⚙️ Step 1: Setup Environment

```bash
python -m venv venv
source venv/Scripts/activate

# 📦 Step 2: Install Dependencies

```bash
pip install pandas scikit-learn flask numpy
```

---

# 📊 Step 3: Dataset

Example (`data/chai_sutta_data.csv`):

```
age,gender,taunts,habit
24,male,1,chai
32,male,5,both
45,male,0,chai
30,female,1,chai
28,female,12,chai
```

---

# 🤖 Step 4: Train Model

```bash
cd src
python train_model.py
```

### ✅ Output:

```
models/
├── chai_sutta_model.pkl
├── gender_encoder.pkl
└── habit_encoder.pkl
```

---

# 🧠 Why Encoders?

| File               | Purpose                       |
| ------------------ | ----------------------------- |
| gender_encoder.pkl | Convert male/female → numbers |
| habit_encoder.pkl  | Convert prediction → label    |

👉 Model only understands numbers, not text.

---

# 🌐 Step 5: Run Flask API

```bash
cd src
python app.py
```

Open browser:

```
http://127.0.0.1:5000
```

### Features:

* Input form (age, gender, taunts)
* Prediction shown on same page
* `/predict` API also available

---

# 🐳 Step 6: Docker Setup

## 1️⃣ Create `requirements.txt`

```
flask
numpy
scikit-learn
pandas
```

---

## 2️⃣ Create `Dockerfile`

```
FROM python:3.9-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "src/app.py"]
```

---

## 3️⃣ Fix Paths in `app.py`

```python
model = pickle.load(open("models/chai_sutta_model.pkl", "rb"))
le_gender = pickle.load(open("models/gender_encoder.pkl", "rb"))
le_habit = pickle.load(open("models/habit_encoder.pkl", "rb"))
```

---

# 🚀 Step 7: Build Docker Image

```bash
docker build -t chai-sutta-app .
```

---

# ▶️ Step 8: Run Container

```bash
docker run -p 5000:5000 chai-sutta-app
```

---

# 🌐 Step 9: Access Application

```
http://localhost:5000
```

---

# 🧠 Key Learnings (MLOps Concepts)

## 🔹 Model vs Encoder

* Model → prediction logic
* Encoder → data translation layer

👉 Both are required in production

---

## 🔹 Why NOT train inside Docker?

❌ Slow builds
❌ Resource waste
❌ Not scalable

---

## 🔹 Best Practice

```
Train Model → Save (.pkl) → Deploy API → Serve
```

---

## 🔹 MLOps Flow

```
[Data Scientist]
   ↓
Train Model
   ↓
Save Model (.pkl)
   ↓
[DevOps/MLOps]
   ↓
Build API
   ↓
Dockerize
   ↓
Deploy
```

---

# 🚀 Future Enhancements

* Use Azure Blob / S3 for model storage
* Add CI/CD pipeline (Azure DevOps / GitHub Actions)
* Deploy to Kubernetes / AKS
* Add monitoring (Prometheus + Grafana)
* Use MLflow for model versioning

---

# 🎯 Final Output

You now have:

✅ Trained ML model
✅ Saved model artifacts
✅ Working Flask API
✅ Dockerized application

---

# 💥 Next Steps

* Push image to registry (ACR / Docker Hub)
* Deploy on Kubernetes (AKS)
* Add auto-scaling & monitoring

---

## 👨‍💻 Summary

This project converts a simple ML idea into a **production-ready deployable service** using DevOps + MLOps practices.

👉 “Model banana easy hai, production me chalana real skill hai” 😄
