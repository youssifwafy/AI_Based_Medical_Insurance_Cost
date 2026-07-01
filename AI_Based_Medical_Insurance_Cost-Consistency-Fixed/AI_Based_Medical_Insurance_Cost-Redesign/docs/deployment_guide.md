# Deployment Guide

Live app:

```text
https://youssifwafy.pythonanywhere.com/
```

## Runtime Files Required

For serving predictions, upload these files and folders:

```text
app.py
model.pickle
requirements.txt
templates/
static/
```

These files are useful for review and development:

```text
medical_cost_prediction_dataset.csv
Preprocessing_amit.py
Final_project_AMIT.ipynb
docs/
README.md
LICENSE
```

## Local Run

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

Install packages:

```bash
pip install -r requirements.txt
```

Run the app:

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5005
```

## PythonAnywhere Setup

1. Upload the project folder to PythonAnywhere.
2. Open a Bash console.
3. Create a virtual environment:

```bash
python3 -m venv ~/.virtualenvs/medical-cost-env
```

4. Activate it:

```bash
source ~/.virtualenvs/medical-cost-env/bin/activate
```

5. Install dependencies:

```bash
pip install -r requirements.txt
```

6. Go to the **Web** tab.
7. Create or configure a Flask web app.
8. Set the source code directory to the project folder.
9. Set the virtual environment path:

```text
/home/YOUR_USERNAME/.virtualenvs/medical-cost-env
```

10. Edit the WSGI configuration file:

```python
import sys

project_home = "/home/YOUR_USERNAME/AI_Based_Medical_Insurance_Cost"
if project_home not in sys.path:
    sys.path.insert(0, project_home)

from app import app as application
```

If your uploaded folder has a different name, update `project_home` to match the folder path shown in PythonAnywhere.

11. Reload the web app.
12. Visit:

```text
https://youssifwafy.pythonanywhere.com/
```

## Notes

- `model.pickle` must remain beside `app.py` unless the loading path in the app is changed.
- PythonAnywhere uses the WSGI file to run the app, so the local port `5005` is not used in production.
- If prediction fails, confirm that `model.pickle` uploaded correctly and that `scikit-learn` is installed in the active virtual environment.
- Only unpickle files that you trust.
