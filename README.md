# 🏥 AI-Based Medical Insurance Cost Prediction


Predict a person's **annual medical insurance cost** using demographic, lifestyle, and health information through a Machine Learning model deployed as a Flask web application.

🔗 **Live Demo:** https://youssifwafy.pythonanywhere.com

---

# 📌 Project Overview

Medical insurance costs depend on many factors such as age, BMI, smoking habits, previous medical expenses, and insurance coverage.

This project builds a complete Machine Learning pipeline that:

- 🧹 Cleans and preprocesses the dataset
- 📊 Performs Exploratory Data Analysis (EDA)
- 🤖 Trains multiple regression models
- 🏆 Selects the best-performing model
- 🌐 Deploys the model using Flask
- 💰 Predicts annual medical insurance costs through a web interface

---

# 🚀 How It Works

```text
Dataset
   │
   ▼
Preprocessing
   │
   ▼
Split data -> train, test, validation
   │
   ▼
Feature Scaling
   │
   ▼
Train Multiple Models
   │
   ▼
Choose Best Model
   │
   ▼
Save model.pickle
   │
   ▼
Flask Web Application
   │
   ▼
User Prediction
```

---

# 📂 Dataset

**File**

```
medical_cost_prediction_dataset.csv
```

### Dataset Information

| Property | Value |
|----------|-------|
| Records | 5,000 |
| Features | 20 |
| Target | annual_medical_cost |

### Original Features

- age
- gender
- bmi
- smoker
- diabetes
- hypertension
- heart_disease
- asthma
- physical_activity_level
- daily_steps
- sleep_hours
- stress_level
- doctor_visits_per_year
- hospital_admissions
- medication_count
- insurance_type
- insurance_coverage_pct
- city_type
- previous_year_cost

---

# 🧹 Data Preprocessing

Implemented in:

```
Preporcessing_amit.py
```

## 1️⃣ Dataset Inspection

Before preprocessing, the dataset was inspected using:

```python
df.shape
df.info()
df.dtypes
df.isnull().sum()
```

### Findings

- Dataset contains **5,000 rows**
- Five columns are categorical
- Only **insurance_type** contains missing values

| Column | Missing Values |
|---------|---------------|
| insurance_type | 1,048 (≈21%) |

---

## 2️⃣ Encoding Categorical Features

Categorical variables were converted into numerical values using manual mapping with `.replace()`.

| Feature | Encoding |
|----------|-----------|
| Gender | Male → 0, Female → 1 |
| Smoker | No → 0, Yes → 1 |
| Physical Activity | Low → 0, Medium → 1, High → 2 |
| City Type | Rural → 0, Semi-Urban → 1, Urban → 2 |
| Insurance Type | Government → 0, Private → 1 |

Each encoding step was verified using:

```python
value_counts()
```

---

## 3️⃣ Missing Value Handling

The **insurance_type** column contained missing values.

Since it is categorical, **Mode Imputation** was applied:

```
Most Frequent Category → Private
```

This filled all missing values while preserving the dataset size.

---

## 4️⃣ Correlation Analysis

After converting every feature to numeric, the correlation matrix was calculated.

Features with almost **no relationship** to the target were removed.

| Feature | Correlation |
|----------|------------|
| daily_steps | 0.002 |
| asthma | 0.009 |
| sleep_hours | -0.005 |

These columns were dropped to reduce unnecessary noise.

---

## Final Dataset

✔ No missing values

✔ All features numeric

✔ 17 columns remaining

- 16 Features
- 1 Target

---

# 🤖 Model Training

Implemented in:

```
Model_Training_amit.ipynb
```

## Exploratory Data Analysis

The notebook includes visualizations such as:

- 📈 Distribution of medical costs
- 🚬 Cost vs Smoker Status
- 👤 Age vs Medical Cost

---

## Train / Validation / Test Split

| Dataset | Samples |
|----------|---------|
| Train | 2,680 |
| Validation | 1,320 |
| Test | 1,000 |

---

## Feature Scaling

Numerical features were standardized using

```python
StandardScaler
```

The scaler was **fit only on the training data** to avoid data leakage.

---

# 📊 Model Comparison

| Model | R² Score | RMSE |
|--------|---------:|------:|
| Linear Regression | 0.9082 | 1364.40 |
| Support Vector Regressor | -0.1257 | 4811.99 |
| Decision Tree Regressor | 0.9461 | 636.16 |
| KNN Regressor | 0.5164 | 909.93 |
| ⭐ Random Forest Regressor | **0.9781** | **≈1058** |

---

# 🏆 Final Model

**Random Forest Regressor**

### Performance

- ✅ R² Score ≈ **0.978**
- ✅ RMSE ≈ **1058**

The trained model is exported as:

```
model.pickle
```

---

# 🌐 Flask Web Application

Implemented in:

```
app.py
```

## Routes

### Home Page

```
GET /
```

Displays the prediction form.

---

### Prediction Endpoint

```
POST /predict
```

Returns:

```json
{
  "predicted_cost": 8423.15
}
```

---

## Feature Order

```
age
gender
bmi
city_type
smoker
physical_activity_level
stress_level
diabetes
hypertension
heart_disease
doctor_visits_per_year
hospital_admissions
medication_count
insurance_type
insurance_coverage_pct
previous_year_cost
```

---

# 📁 Project Structure

```
AI_Based_Medical_Insurance_Cost/
├── app.py
├── model.pickle
├── medical_cost_prediction_dataset.csv
├── Preprocessing_amit.py
├── Model_Training_amit.ipynb
├── requirements.txt
├── README.md
├── LICENSE
├── docs/
│   ├── data_dictionary.md
│   ├── deployment_guide.md
│   └── model_card.md
├── static/
│   └── styles.css
└── templates/
    └── index.html
```
---

# 🛠 Technologies Used

- Jupyter
- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-Learn
- Flask
- Pickle

---


# 👨‍💻 Team Members
- Youssif Wafy
- Saif Hatem
- Mohamed Medhat
- Ahmed Walid
- Abdelrahman Noaman
---

