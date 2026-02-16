from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
import requests
import os

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

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"

@app.post("/predict")
def predict(data: PatientData):
    df = pd.DataFrame([data.dict()])
    df = df.reindex(columns=model.feature_names_in_, fill_value=0)
    prediction = model.predict(df)[0]
    #return {"triage_level": int(prediction)}
    triage_level = int(prediction)

    # Ask OpenRouter for layman explanation
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    prompt = f"""
    A healthcare triage model decided the patient should be '{triage_level}'.
    Inputs: {data.model_dump()}.
    Explain in simple layman terms why this decision makes sense.
    Do not talk about parameter weights or technical details.
    """

    body = {
        "model": "openai/gpt-3.5-turbo",  
        "messages": [
            {"role": "system", "content": "You are a helpful medical explainer."},
            {"role": "user", "content": prompt}
        ]
    }

    try:
        response = requests.post(OPENROUTER_URL, headers=headers, json=body)
        explanation = response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        explanation = f"Explanation service error: {e}"

    return {"triage_level": triage_level, "explanation": explanation}
