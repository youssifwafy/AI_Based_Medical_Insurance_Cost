# Medical Cost Prediction MVP

End-to-end regression prototype to predict `annual_medical_cost` from `medical_cost_prediction_dataset.csv`.

The project is designed for quick deployment to PythonAnywhere and uses only these direct project dependencies:

- pandas
- numpy
- scikit-learn
- seaborn
- matplotlib
- flask

Model persistence uses Python's standard-library `pickle` module.

## Project Structure

```text
medical_cost_mvp/
├── app.py                         # Flask API for PythonAnywhere
├── train.py                       # Main training command
├── generate_eda.py                # EDA-only command
├── predict_example.py             # Local prediction example
├── requirements.txt               # Direct dependencies
├── README.md
├── data/
│   └── medical_cost_prediction_dataset.csv  # Place dataset here
├── reports/
│   ├── model_comparison.csv
│   ├── model_comparison.json
│   ├── summary_statistics.csv
│   ├── data_quality_report.csv
│   ├── outlier_prevalence.csv
│   └── figures/
├── model_artifacts/
│   ├── best_model_pipeline.pkl    # Pickled best sklearn Pipeline
│   ├── model_metadata.json
│   └── candidate_models/          # Pickled candidate pipelines
└── src/
    ├── config.py
    ├── preprocessing.py
    ├── eda.py
    ├── modeling.py
    ├── evaluation.py
    ├── model_saving.py
    └── inference.py
```

## Setup

```bash
python -m venv .venv
source .venv/bin/activate      # macOS/Linux
# .venv\Scriptsctivate      # Windows PowerShell
pip install -r requirements.txt
```

Place the dataset here:

```text
data/medical_cost_prediction_dataset.csv
```

## Train All Models

```bash
python train.py --data data/medical_cost_prediction_dataset.csv
```

This runs EDA, trains all candidate models, evaluates them, and saves the best model.

To skip EDA:

```bash
python train.py --data data/medical_cost_prediction_dataset.csv --skip-eda
```

## Run EDA Only

```bash
python generate_eda.py --data data/medical_cost_prediction_dataset.csv
```

Generated Seaborn plots:

1. Target distribution histogram with KDE
2. Missing-value bar chart
3. Correlation heatmap
4. Age vs cost scatter plot by smoker status
5. Cost by smoker status box plot
6. IQR outlier prevalence chart

## Preprocessing Strategy

The preprocessing is implemented in `src/preprocessing.py` and saved inside the fitted sklearn Pipeline.

### Missing values

- Numerical features: median imputation
- Categorical features: most-frequent imputation
- Binary features: most-frequent imputation

This avoids dropping rows and keeps the API safe for production predictions.

### Outliers

Numerical outliers are capped using IQR limits learned from the training fold only:

```text
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR
```

Rows are not dropped because production systems must still return a prediction for valid records.

### Encoding

Categorical features are one-hot encoded with `handle_unknown="ignore"` so unseen production categories do not crash inference.

### Scaling

- Linear Regression, Ridge, and Lasso use standardized numerical features.
- Random Forest and Gradient Boosting do not require scaling.

### Feature engineering

Created features:

- `comorbidity_count`
- `is_obese`
- `age_bmi_interaction`
- `previous_cost_per_visit`
- `lifestyle_risk_score`
- `smoker_with_diabetes`

These are simple, explainable MVP features that may improve predictive power.

## Models Included

- Linear Regression
- Ridge Regression
- Lasso Regression
- Random Forest Regressor
- Gradient Boosting Regressor

Best model selection rule:

1. Lowest RMSE
2. Lowest MAE
3. Highest R²

## Outputs After Training

```text
reports/model_comparison.csv
reports/model_comparison.json
reports/summary_statistics.csv
reports/data_quality_report.csv
reports/outlier_prevalence.csv
reports/figures/*.png
model_artifacts/best_model_pipeline.pkl
model_artifacts/model_metadata.json
model_artifacts/candidate_models/*.pkl
```

`best_model_pipeline.pkl` contains both preprocessing and the trained estimator.

## Local Prediction Example

```bash
python predict_example.py
```

Or call the inference utility directly:

```python
from src.inference import predict_single

payload = {
    "age": 45,
    "bmi": 31.2,
    "daily_steps": 5200,
    "sleep_hours": 6.5,
    "stress_level": 7,
    "doctor_visits_per_year": 5,
    "hospital_admissions": 1,
    "medication_count": 2,
    "insurance_coverage_pct": 80,
    "previous_year_cost": 6200,
    "gender": "Male",
    "smoker": "No",
    "physical_activity_level": "Medium",
    "insurance_type": "Private",
    "city_type": "Urban",
    "diabetes": 0,
    "hypertension": 1,
    "heart_disease": 0,
    "asthma": 0,
}

prediction = predict_single(payload)
print(prediction)
```

## Run Flask API Locally

```bash
flask --app app run --debug
```

Health endpoint:

```bash
curl http://127.0.0.1:5000/health
```

Prediction endpoint:

```bash
curl -X POST http://127.0.0.1:5000/predict   -H "Content-Type: application/json"   -d '{
    "age": 45,
    "bmi": 31.2,
    "daily_steps": 5200,
    "sleep_hours": 6.5,
    "stress_level": 7,
    "doctor_visits_per_year": 5,
    "hospital_admissions": 1,
    "medication_count": 2,
    "insurance_coverage_pct": 80,
    "previous_year_cost": 6200,
    "gender": "Male",
    "smoker": "No",
    "physical_activity_level": "Medium",
    "insurance_type": "Private",
    "city_type": "Urban",
    "diabetes": 0,
    "hypertension": 1,
    "heart_disease": 0,
    "asthma": 0
  }'
```

## PythonAnywhere Deployment Checklist

Upload these files/folders:

```text
app.py
requirements.txt
src/
model_artifacts/best_model_pipeline.pkl
model_artifacts/model_metadata.json
```

Optional audit files:

```text
reports/model_comparison.csv
reports/model_comparison.json
reports/figures/*.png
```

The training dataset is not required for inference unless you plan to retrain on PythonAnywhere.

### PythonAnywhere steps

1. Open a Bash console on PythonAnywhere.
2. Upload the project folder.
3. Create or activate a virtual environment.
4. Install dependencies:

```bash
pip install -r requirements.txt
```

5. Go to the Web tab.
6. Create or configure a Flask web app.
7. Set the source code directory to this project folder.
8. Set the virtual environment path.
9. Edit the WSGI file.
10. Reload the web app.

Example WSGI file:

```python
import sys
project_home = "/home/YOUR_USERNAME/medical_cost_mvp"
if project_home not in sys.path:
    sys.path.insert(0, project_home)

from app import app as application
```

## Important Production Notes

- Pickle files can execute code when loaded. Only load `.pkl` files generated by your own trusted training workflow.
- Keep training and deployment package versions aligned.
- Validate API inputs before prediction.
- Add authentication, rate limiting, and logging before public exposure.
- Retrain periodically when patient/customer profiles or cost patterns change.
