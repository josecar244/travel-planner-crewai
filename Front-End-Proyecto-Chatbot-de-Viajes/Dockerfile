# Frontend Dockerfile for Streamlit
FROM python:3.12-slim

WORKDIR /app

# Install streamlit and dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY . .

# Expose Streamlit's default port
EXPOSE 8501

# Streamlit config (optional but good for VPS)
ENV STREAMLIT_SERVER_PORT=8501
ENV STREAMLIT_SERVER_ADDRESS=0.0.0.0

# Run Streamlit (targeting src/app.py)
CMD ["streamlit", "run", "src/app.py"]
