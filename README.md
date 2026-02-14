# Healthcare Triage Assistant

![Python](https://img.shields.io/badge/python-3.10+-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-API-green)
![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-red)
![Docker](https://img.shields.io/badge/Docker-Deployment-blue)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow)

End-to-end ML deployment project predicting patient triage levels using FastAPI, Streamlit, and Docker.

**You can now test the app and inspect the API deployed on Render!** 

**Streamlit app**: [Healthcare Triage Assistant Frontend](https://healthcare-triage-assistant.onrender.com/)
**Inspect the API:** [API Docs](https://healthcare-triage-assistant-backend.onrender.com/docs)

*Note: The frontend and backend services may take a moment to start if inactive, as they sleep after 15 minutes of no use. Thanks for your patience!*

---

## Overview

The Healthcare Triage Assistant is a ML project designed to support emergency departments by predicting patient triage levels based on vital signs, symptoms, and arrival mode.

It demonstrates the full ML lifecycle:

- Data wrangling & feature engineering
- Model training & evaluation
- FastAPI backend for serving predictions
- Streamlit frontend with intuitive hospital friendly UI
- Dockerized deployment for portability

---

## Dataset

This project uses the [Synthetic Medical Triage Priority Dataset](https://www.kaggle.com/datasets/emirhanakku/synthetic-medical-triage-priority-dataset/) from Kaggle for model development and evaluation.

---

## Project Features

- Predicts triage levels (Routine, Urgent, Emergency, Self-care/Non-urgent)
- FastAPI backend with RESTful API endpoints
- Streamlit frontend with segmented controls and color-codedoutputs
- Dockerized setup with `docker-compose` for easy deployment
- Interactive API documentation (`/docs`) for API exploration

---

## Project Structure

```bash
Healthcare-Triage-Assistant/
├── app/
│   └── streamlit_app.py                    # Streamlit frontend
├── data/
│   └── raw/
│       └──synthetic_medical_triage.csv     # Raw dataset
├── notebooks/
│   └── cleandata.ipynb                    # Data cleaning & Model training
├── src/
│   ├── api.py                              # FastAPI backend
│   └── model.pkl                           # Trained ML model
├── .dockerignore
├── docker-compose.yml                      # Docker Compose configuration
├── Dockerfile                              # Docker definition
├── LICENSE
├── README.md
└── requirements.txt
```

---

## Installation

Clone the repo:

```bash
git clone https://github.com/rishabhpatel9/Healthcare-Triage-Assistant.git
cd Healthcare-Triage-Assistant
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run FastAPI backend:

```bash
uvicorn src.api:app --reload
```

Run Streamlit frontend:

```bash
streamlit run app/streamlit_app.py
```

---

## Deployment with Docker

Build and run with docker-compose:

```bash
docker-compose up --build
```

Use Streamlit app frontend → `http://localhost:8501`

---

## API Documentation

Once backend is running, visit:

* API Documentation → `http://localhost:8000/docs`
* Redoc → `http://localhost:8000/redoc`

---

## Model Training Features

The triage classifier was trained on patient intake data with the following features:

- **Age** → Patient’s age in years
- **Heart Rate** → Beats per minute
- **Systolic Blood Pressure** → mmHg
- **Oxygen Saturation (SpO₂)** → Percentage
- **Body Temperature** → Patient's body temperature (°C)
- **Chronic Disease Count** → Number of chronic conditions
- **Previous ER Visits** → Number of prior emergency room visits
- **Pain Level** → Self-reported scale (0–10)
- **Arrival Mode** → Walk-in, Ambulance, Referral


### Target Variable - Triage Level
Ouput shown as:
  - 🟢 Routine  
  - 🟡 Urgent  
  - 🔴 Emergency  
  - 🔵 Self-care / Non-urgent

---
## Releases

This project uses GitHub Releases to track milestones.

* **v1.0.0** → First working version with FastAPI + Streamlit
* **v1.0.1** → Minor fixes
* **v1.1.0** → Dockerized deployment
* **v1.2.0** → Split docker frontend and backend for deployment + project deployed on Render for visitors to test/inspect

---

## Future Work

* Implement GenAI for explaining predictions to first line (potentially non-clinical) healthcare staff why the model made a certain triage prediction
* Improve model accuracy with larger datasets
* Integrate hospital database for real patient records
* Add authentication & role-based access control

---
## Contributing

Contributions are welcome!

* Fork the repo
* Create a feature branch
* Submit a pull request