# hard-model-mau — Heart Disease Prediction (Deploy ML Model)

Práctica **W6 – Deploy Machine Learning Model** (adsoft): modelo `RandomForestClassifier`
servido con **FastAPI**, empaquetado en **Docker** y desplegado en **Render**.

Dataset: [Heart Disease Dataset (Kaggle)](https://www.kaggle.com/datasets/johnsmith88/heart-disease-dataset)

## Estructura

```text
├── data/heart-disease.csv        # dataset
├── model/train.py                # entrenamiento
├── model/heart-disease-v1.joblib # modelo entrenado
├── app.py                        # API FastAPI (POST /score)
├── client.py                     # cliente de prueba
├── requirements.txt
└── Dockerfile
```

## Uso local

```bash
python3 -m venv ml-env
source ml-env/bin/activate
pip install -r requirements.txt
python model/train.py
uvicorn app:app --reload
```

Docs interactivas: http://127.0.0.1:8000/docs

```bash
python client.py                       # local
python client.py https://<servicio>.onrender.com   # Render
```

## Docker

```bash
docker build -t maurihm/fastapiml .
docker run -d --name heart-disease-serving -p 80:80 maurihm/fastapiml
docker login
docker push maurihm/fastapiml
```

## Render

Dashboard → **New + → Web Service → Existing Image** →
`docker.io/maurihm/fastapiml:latest` → Deploy.

## Prueba rápida con curl

```bash
curl -X POST "https://<servicio>.onrender.com/score" \
  -H "Content-Type: application/json" \
  -d '{"age":64,"sex":1,"cp":3,"trestbps":120,"chol":267,"fbs":0,"restecg":0,"thalach":99,"exang":1,"oldpeak":1.8,"slope":1,"ca":2,"thal":2}'
```
