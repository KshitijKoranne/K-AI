# Multi-stage Dockerfile for K-AI Pharmaceutical Chatbot
FROM node:18-alpine as frontend-builder

WORKDIR /app/frontend
COPY frontend/package*.json ./
RUN npm ci
COPY frontend/ ./
RUN npm run build

FROM python:3.11-slim as backend

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy and install Python dependencies
COPY application/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY application/ ./
COPY --from=frontend-builder /app/frontend/dist ./static

# Expose port
EXPOSE 7091

# Start command
CMD ["gunicorn", "--bind", "0.0.0.0:7091", "--workers", "4", "--timeout", "120", "app:app"]