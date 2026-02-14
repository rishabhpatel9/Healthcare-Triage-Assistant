# Use official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose ports for FastAPI (8000) and Streamlit (8501)
EXPOSE 8000
EXPOSE 8501

# Default command runs both backend and frontend
CMD uvicorn src.api:app --host 0.0.0.0 --port 8000 & \
    streamlit run app/streamlit_app.py --server.port 10000 --server.headless true