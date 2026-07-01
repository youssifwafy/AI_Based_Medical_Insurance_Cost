# Project Workflow

This document explains the role of each major file without changing the project code.

## File Roles

| File | Role |
|---|---|
| `medical_cost_prediction_dataset.csv` | Original dataset. |
| `Preprocessing_amit.py` | Python preprocessing/export file. |
| `Final_project_AMIT.ipynb` | Final model-training and model-comparison notebook. |
| `model.pickle` | Saved trained model used by the Flask app. |
| `app.py` | Flask application and `/predict` endpoint. |
| `templates/index.html` | Web form and frontend interaction. |
| `static/styles.css` | Styling for the web interface. |

## Recommended Review Order

1. Open `README.md` for the project overview.
2. Review `medical_cost_prediction_dataset.csv` as the original source data.
3. Review `Preprocessing_amit.py` for preprocessing/export work.
4. Review `Final_project_AMIT.ipynb` for model training and comparison.
5. Run `app.py` to test the Flask app locally.
6. Use `docs/deployment_guide.md` for PythonAnywhere deployment notes.

## Runtime Files

The deployed Flask app mainly needs:

```text
app.py
model.pickle
requirements.txt
templates/
static/
```

The dataset, preprocessing script, notebook, and docs are still important for review, reproducibility, and project explanation.
