# AI-Based Medical Insurance Cost Prediction

This repository contains a machine learning regression project for predicting `annual_medical_cost` from medical insurance cost data. It includes the original dataset, a preprocessing Python file, the final model-training notebook, a saved `pickle` model, and a Flask web application deployed on PythonAnywhere.

Live app:

```text
https://youssifwafy.pythonanywhere.com/
```

This project is for educational and portfolio use. It is not a medical, clinical, insurance, or financial decision system.

## Project Files

| File or Folder | Purpose |
|---|---|
| `medical_cost_prediction_dataset.csv` | Original dataset file. |
| `final_project_amit.py` | Python preprocessing/export file. |
| `Final_project_AMIT.ipynb` | Final notebook used for model training and comparison. |
| `model.pickle` | Saved trained model used by the Flask app. |
| `app.py` | Flask backend for serving the web app and prediction endpoint. |
| `templates/index.html` | Frontend HTML page. |
| `static/styles.css` | Frontend styling. |
| `requirements.txt` | Python dependencies. |
| `docs/` | Project documentation. |
| `LICENSE` | MIT open-source license. |

## Repository Structure

```text
AI_Based_Medical_Insurance_Cost-Redesign/
├── app.py
├── model.pickle
├── medical_cost_prediction_dataset.csv
├── final_project_amit.py
├── Final_project_AMIT.ipynb
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

## Features Used by the Flask App

The Flask prediction endpoint sends these 16 encoded numeric inputs to `model.pickle`, in this exact order:

| Order | Feature |
|---:|---|
| 1 | `age` |
| 2 | `gender` |
| 3 | `bmi` |
| 4 | `smoker` |
| 5 | `diabetes` |
| 6 | `hypertension` |
| 7 | `heart_disease` |
| 8 | `physical_activity_level` |
| 9 | `stress_level` |
| 10 | `doctor_visits_per_year` |
| 11 | `hospital_admissions` |
| 12 | `medication_count` |
| 13 | `insurance_type` |
| 14 | `insurance_coverage_pct` |
| 15 | `city_type` |
| 16 | `previous_year_cost` |

The original dataset also contains `daily_steps`, `sleep_hours`, and `asthma`. The notebook drops these before model training after correlation review.

## Model Summary

The notebook compares five regression models:

| Model | R2 Score | RMSE |
|---|---:|---:|
| Linear Regression | 0.908316 | 2136.403636 |
| SVR | -0.124513 | 7481.998714 |
| Decision Tree Regressor | 0.946225 | 1636.159729 |
| KNN Regressor | 0.515739 | 4909.926732 |
| Random Forest Regressor | 0.978364 | 1037.836005 |

The selected model is a **Random Forest Regressor**. The final saved model cell reports:

| Final Saved Model | R2 Score | RMSE |
|---|---:|---:|
| Random Forest Regressor | 0.977492 | 1058.538119 |

Because the final Random Forest model is created without a fixed `random_state`, exact values may vary if the notebook is re-run.

## Installation

Create and activate a virtual environment:

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

macOS/Linux:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run Locally

From the project folder:

```bash
python app.py
```

Then open:

```text
http://127.0.0.1:5005
```

## API Example

The `/predict` endpoint accepts JSON input and returns a predicted annual medical cost.

```json
{
  "age": 45,
  "gender": 0,
  "bmi": 28.5,
  "smoker": 1,
  "diabetes": 0,
  "hypertension": 1,
  "heart_disease": 0,
  "physical_activity_level": 1,
  "stress_level": 6,
  "doctor_visits_per_year": 4,
  "hospital_admissions": 1,
  "medication_count": 2,
  "insurance_type": 1,
  "insurance_coverage_pct": 80,
  "city_type": 2,
  "previous_year_cost": 7000
}
```

Example response:

```json
{
  "predicted_cost": 5300.25
}
```

## Documentation

Additional documentation is available in the `docs/` folder:

- `docs/data_dictionary.md`
- `docs/model_card.md`
- `docs/deployment_guide.md`

## Important Notes

- The original dataset remains at `medical_cost_prediction_dataset.csv`.
- The Python preprocessing/export file remains `final_project_amit.py`.
- The model-training notebook remains `Final_project_AMIT.ipynb`.
- The saved model expects already encoded numeric inputs.
- `pickle` is part of Python's standard library and does not need to be installed separately.
- Only load pickle files that you trust.

## License

This project is released under the MIT License. See `LICENSE` for details.
