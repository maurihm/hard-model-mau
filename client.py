import sys
import requests

base_url = sys.argv[1] if len(sys.argv) > 1 else 'http://127.0.0.1:8000'

body = {
    "age": 64,
    "sex": 1,
    "cp": 3,
    "trestbps": 120,
    "chol": 267,
    "fbs": 0,
    "restecg": 0,
    "thalach": 99,
    "exang": 1,
    "oldpeak": 1.8,
    "slope": 1,
    "ca": 2,
    "thal": 2
}

response = requests.post(url=f"{base_url.rstrip('/')}/score", json=body)
print(response.json())
