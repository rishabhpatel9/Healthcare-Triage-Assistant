# Healthcare Triage Assistant

![Python](https://img.shields.io/badge/python-3.10+-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-API-green)
![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-red)
![Docker](https://img.shields.io/badge/Docker-Deployment-blue)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow)

> End-to-end ML deployment project predicting patient triage levels using FastAPI, Streamlit, and Docker.

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

## Features

- Predicts triage levels (Routine, Urgent, Emergency, Self-care/Non-urgent)
- FastAPI backend with RESTful API endpoints
- Streamlit frontend with segmented controls and color-codedoutputs
- Dockerized setup with `docker-compose` for easy deployment
- Interactive API documentation (`/docs`) for API exploration

---

## Project Structure

```bash
Healthcare-Triage-Assistant/
├── src/
│   ├── api.py          # FastAPI backend
│   ├── model.pkl       # Trained ML model
├── app/
│   └── streamlit_app.py # Streamlit frontend
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md
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

* Backend → `http://localhost:8000`
* Frontend → `http://localhost:8501`

---

## Releases

This project uses GitHub Releases to track milestones. (Yet to implement)

* **v1.0.0** → First working version with FastAPI + Streamlit
* **v1.1.0** → Added segmented controls and color-coded triage output
* **v2.0.0** → Dockerized deployment

---

## API Documentation

Once backend is running, visit:

* Swagger UI → `http://localhost:8000/docs`
* Redoc → `http://localhost:8000/redoc`

---

## Contributing

Contributions are welcome!

* Fork the repo
* Create a feature branch
* Submit a pull request

---

## Future Work

* Integrate hospital database for real patient records
* Add authentication & role-based access
* Improve model accuracy with larger datasets
