from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
import pandas as pd

app = FastAPI(title="IRIS Classifier API")

#Load Model
try:
    model = joblib.load("iris_model.joblib")
except EOFError:
    raise RuntimeError("Failed to load model: iris_model.joblib is corrupted or missing.")

#Input Schema
class IrisInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

@app.get("/")
def read_root():
    return ("message: Welcome to the IRIS Classifier API")

@app.get("/predict/")
def predict_species(data: IrisInput):
    input_df = pd.DataFrame([data.dict()])
    prediction = model.predict(input_df)[0]
    return (
            "predicted_class: "+ prediction
    )
