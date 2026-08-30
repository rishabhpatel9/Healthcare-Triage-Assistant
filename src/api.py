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
    df = pd.DataFrame([data.model_dump()])
    df = df.reindex(columns=model.feature_names_in_, fill_value=0)
    prediction = model.predict(df)[0]
    triage_level = int(prediction)

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
    "model": "nvidia/nemotron-3.5-lightning:free",  # single model string
    "messages": [
        {
            "role": "system",
            "content": (
                "You are a healthcare triage explainer."
                "The triage level is already decided by another model."
                "Do not re-evaluate inputs."
                "Explain briefly in layman terms why this level makes sense."
                "Respond in at most 2 sentences."
                "Triage scale: 0=Routine (least severe), 1=Urgent, "
                "2=Emergency (most severe), 3=Self-care."
            )
        },
        {
            "role": "user",
            "content": f"Triage Level: {triage_level}. Patient summary: {data.model_dump()}"
        }
    ]
}


    try:
        response = requests.post(OPENROUTER_URL, headers=headers, json=payload, timeout=15)
        if response.status_code != 200:
            print(f"[ERROR] OpenRouter returned status {response.status_code}: {response.text}", flush=True)
        res_data = response.json()
        explanation = res_data["choices"][0]["message"]["content"]
    except Exception as e:
        print(f"[ERROR] Failed to fetch explanation from OpenRouter: {e}", flush=True)
        if 'response' in locals() and hasattr(response, 'text'):
            print(f"[ERROR] Raw response content: {response.text}", flush=True)
        explanation = f"Explanation service error: {e}"

    return {"triage_level": triage_level, "explanation": explanation}

