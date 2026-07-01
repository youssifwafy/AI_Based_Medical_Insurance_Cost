# Model Card

## Model Details

| Item | Description |
|---|---|
| Project | AI-Based Medical Insurance Cost Prediction |
| Problem type | Regression |
| Target | `annual_medical_cost` |
| Selected model | Random Forest Regressor |
| Model file | `model.pickle` |
| Framework | scikit-learn |
| Interface | Flask web app |
| Live app | https://youssifwafy.pythonanywhere.com/ |

## Intended Use

This model is intended for educational demonstration and portfolio presentation. It estimates annual medical cost from encoded demographic, lifestyle, medical-condition, insurance, and previous-cost inputs.

It should not be used for real medical, clinical, financial, underwriting, or insurance decisions.

## Project Files

- `medical_cost_prediction_dataset.csv`: original dataset.
- `final_project_amit.py`: preprocessing/export file.
- `Model_Training_amit.ipynb`: model-training notebook.
- `model.pickle`: saved trained model used by the Flask app.

## Model Comparison

The notebook reports the following comparison:

| Model | R2 Score | RMSE |
|---|---:|---:|
| Linear Regression | 0.908316 | 2136.403636 |
| SVR | -0.124513 | 7481.998714 |
| Decision Tree Regressor | 0.946225 | 1636.159729 |
| KNN Regressor | 0.515739 | 4909.926732 |
| Random Forest Regressor | 0.978364 | 1037.836005 |

The final saved Random Forest training cell reports:

| Metric | Value |
|---|---:|
| R2 Score | 0.977492 |
| RMSE | 1058.538119 |

## Why Random Forest Was Selected

Random Forest Regressor achieved the strongest reported performance among the tested models. It can capture non-linear relationships between cost and risk factors better than a simple linear model, while usually being more stable than a single decision tree.

## Limitations

- The model is trained and evaluated on a single dataset split.
- There is no documented external validation dataset.
- The Random Forest model is created without a fixed `random_state`, so retraining may produce slightly different results.
- The saved pickle appears to contain the estimator only, not a complete preprocessing pipeline.
- The model expects manually encoded inputs.
- Fairness, subgroup performance, and bias checks are not documented.
- Real-world medical and insurance cost prediction requires stronger governance, privacy review, validation, and explainability.

## Recommended Future Improvements

- Save a full scikit-learn pipeline including preprocessing.
- Add MAE to the model comparison.
- Add cross-validation.
- Add feature importance analysis.
- Add input validation for categorical values.
- Add a reproducible training script with a fixed random seed.
- Add tests for `/predict` and for feature order consistency.
