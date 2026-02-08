import streamlit as st
import requests

st.title("Healthcare Triage Assistant")

# Input form
age = st.number_input("Age", min_value=0, max_value=120)
heart_rate = st.number_input("Heart Rate", min_value=30, max_value=220)
systolic_bp = st.number_input("Systolic Blood Pressure", min_value=50, max_value=250)
oxygen = st.number_input("Oxygen Saturation (%)", min_value=50, max_value=100)
temperature = st.number_input("Body Temperature (°C)", min_value=30.0, max_value=45.0)
pain = st.slider("Pain Level (0-10)", 0, 10)
chronic = st.number_input("Chronic Disease Count", min_value=0, max_value=10)
visits = st.number_input("Previous ER Visits", min_value=0, max_value=20)
arrival = st.selectbox("Arrival Mode", ["walk_in", "ambulance", "wheelchair"])

# Encode arrival mode
arrival_ambulance = 1 if arrival == "ambulance" else 0
arrival_wheelchair = 1 if arrival == "wheelchair" else 0

if st.button("Predict Triage Level"):
    payload = {
        "age": age,
        "heart_rate": heart_rate,
        "systolic_blood_pressure": systolic_bp,
        "oxygen_saturation": oxygen,
        "body_temperature": temperature,
        "pain_level": pain,
        "chronic_disease_count": chronic,
        "previous_er_visits": visits,
        "arrival_mode_ambulance": arrival_ambulance,
        "arrival_mode_wheelchair": arrival_wheelchair
    }
    response = requests.post("http://127.0.0.1:8000/predict", json=payload)
    st.success(f"Triage Level: {response.json()['triage_level']}")
