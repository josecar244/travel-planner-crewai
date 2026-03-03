# Backend Dockerfile for CrewAI
FROM python:3.12-slim

# Install uv for fast builds
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

# Enable bytecode compilation
ENV UV_COMPILE_BYTECODE=1

# Copy requirements
COPY requirements.txt .

# Install dependencies using uv
RUN uv pip install --system --no-cache -r requirements.txt

# Copy source code
COPY . .

# Ensure PYTHONPATH is set so that modules can be found
ENV PYTHONPATH="/app/src"

# Render provides the port via the PORT environment variable
EXPOSE 10000

# Run the application with a dynamic port
CMD ["uvicorn", "travel_crew_backend.main:app", "--host", "0.0.0.0", "--port", "10000"]