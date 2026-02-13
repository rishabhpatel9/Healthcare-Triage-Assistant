import streamlit as st
import requests

st.markdown("<h1 style='text-align: center;'>Healthcare Triage Assistant</h1>", unsafe_allow_html=True)

# Input form
with st.form("triage_form"):
    age = st.number_input("Age", min_value=0, max_value=120)
    heart_rate = st.number_input("Heart Rate", min_value=30, max_value=220)
    systolic_bp = st.number_input("Systolic Blood Pressure", min_value=50, max_value=250)
    oxygen = st.number_input("Oxygen Saturation (%)", min_value=50, max_value=100)
    temperature = st.number_input("Body Temperature (°C)", min_value=30.0, max_value=45.0)
    chronic = st.number_input("Chronic Disease Count", min_value=0, max_value=10)
    visits = st.number_input("Previous ER Visits", min_value=0, max_value=20)
    pain = st.slider("Pain Level (0-10)", 0, 10)
    arrival = st.segmented_control("Arrival Mode", options=["walk_in", "ambulance", "wheelchair"], default="walk_in")
    submitted = st.form_submit_button("Predict Triage Level")

# Encode arrival mode
arrival_walk_in = 1 if arrival == "walk_in" else 0
arrival_ambulance = 1 if arrival == "ambulance" else 0
arrival_wheelchair = 1 if arrival == "wheelchair" else 0

if submitted:
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

    #st.write("### Patient Summary")
    #st.json(payload)

    response = requests.post("http://backend:8000/predict", json=payload)
    triage_level = response.json()['triage_level']
    #st.success(f"Triage Level: {triage_level}")

    if triage_level == 0:
        st.success("🟢 Routine Case (Level 0)")
    elif triage_level == 1:
        st.warning("🟡 Urgent Case (Level 1)")
    elif triage_level == 2:
        st.error("🔴 Emergency Case (Level 2)")
    elif triage_level == 3:
        st.info("🔵 Self-care Case (Level 3)")
