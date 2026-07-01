# Data Dictionary

The original dataset file is `medical_cost_prediction_dataset.csv`. The target variable is `annual_medical_cost`.

## Target

| Column | Type | Description |
|---|---|---|
| `annual_medical_cost` | Numeric | Annual medical cost predicted by the regression model. |

## Original Dataset Columns

| Column | Type | Notes |
|---|---|---|
| `age` | Numeric | Patient age in years. |
| `gender` | Categorical | Encoded in preprocessing as `Male = 0`, `Female = 1`. |
| `bmi` | Numeric | Body Mass Index. |
| `smoker` | Categorical | Encoded as `No = 0`, `Yes = 1`. |
| `diabetes` | Binary | `0 = No`, `1 = Yes`. |
| `hypertension` | Binary | `0 = No`, `1 = Yes`. |
| `heart_disease` | Binary | `0 = No`, `1 = Yes`. |
| `asthma` | Binary | Present in the original dataset. Dropped before model training in the notebook. |
| `physical_activity_level` | Categorical/ordinal | Encoded as `Low = 0`, `Medium = 1`, `High = 2`. |
| `daily_steps` | Numeric | Present in the original dataset. Dropped before model training in the notebook. |
| `sleep_hours` | Numeric | Present in the original dataset. Dropped before model training in the notebook. |
| `stress_level` | Numeric/ordinal | Stress level score. |
| `doctor_visits_per_year` | Numeric | Number of yearly doctor visits. |
| `hospital_admissions` | Numeric | Number of yearly hospital admissions. |
| `medication_count` | Numeric | Number of medications. |
| `insurance_type` | Categorical | Encoded in preprocessing. Raw data may include `Government`, `Private`, and `None`. |
| `insurance_coverage_pct` | Numeric | Insurance coverage percentage. |
| `city_type` | Categorical/ordinal | Encoded as `Rural = 0`, `Semi-Urban = 1`, `Urban = 2`. |
| `previous_year_cost` | Numeric | Previous annual medical cost. |

## Flask Prediction Inputs

The deployed Flask app sends 16 encoded numeric features to `model.pickle`:

```text
age, gender, bmi, smoker, diabetes, hypertension, heart_disease,
physical_activity_level, stress_level, doctor_visits_per_year,
hospital_admissions, medication_count, insurance_type,
insurance_coverage_pct, city_type, previous_year_cost
```

## File Roles

- `medical_cost_prediction_dataset.csv` is the original dataset.
- `Preporcessing_amit.py` is the Python preprocessing/export file.
- `Model_Training_amit.ipynb` is the final model-training notebook.
