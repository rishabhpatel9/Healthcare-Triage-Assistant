from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

model = joblib.load("src/model.pkl")

app = FastAPI(title="Healthcare Triage Assistant API")

class PatientData(BaseModel):
    age: int
    heart_rate: int
    systolic_blood_pressure: int
    oxygen_saturation: int
    body_temperature: float
    pain_level: int
    chronic_disease_count: int
    previous_er_visits: int
    arrival_mode_ambulance: int = 0
    arrival_mode_wheelchair: int = 0

@app.post("/predict")
def predict(data: PatientData):
    
    df = pd.DataFrame([data.dict()])
    
    prediction = model.predict(df)[0]
    return {"triage_level": int(prediction)}