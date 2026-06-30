import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import math

app = Flask(__name__)
model = pickle.load(open('model.pickle','rb')) # waiting for the model

# Field order must match the order of the model.
FEATURE_ORDER = [
    "age", "gender", "bmi", "smoker", "diabetes", "hypertension",
    "heart_disease", "physical_activity_level", "stress_level",
    "doctor_visits_per_year", "hospital_admissions", "medication_count",
    "insurance_type", "insurance_coverage_pct", "city_type",
    "previous_year_cost",
]
@app.route('/')
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json(force=True)
    row = [[float(data.get(f, 0)) for f in FEATURE_ORDER]]
    predicted_cost = float(model.predict(row)[0])
    return jsonify({"predicted_cost": round(predicted_cost, 2)})



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5005)