import os
import joblib
import redis
from fastapi import FastAPI
from pydantic import BaseModel

MODEL_PATH = os.getenv("MODEL_PATH", "/models/model.joblib")
REDIS_HOST = os.getenv("REDIS_HOST", "base")
REDIS_PORT = int(os.getenv("REDIS_PORT", "6379"))
CLASSES = ["setosa", "versicolor", "virginica"]

app = FastAPI(title="Iris inference")
model = joblib.load(MODEL_PATH)
r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)

class Flower(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict")
def predict(f: Flower):
    x = [[f.sepal_length, f.sepal_width, f.petal_length, f.petal_width]]
    classe = CLASSES[int(model.predict(x)[0])]
    r.incr("predictions:total")
    r.hincrby("predictions:par_classe", classe, 1)
    return {"class": classe}

@app.get("/stats")
def stats():
    par_classe = r.hgetall("predictions:par_classe")
    return {
        "total": int(r.get("predictions:total") or 0),
        "par_classe": {k: int(v) for k, v in par_classe.items()},
    }