# K-AI Pharmaceutical Chatbot - Render Deployment
FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy and install Python dependencies
COPY application/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code with proper structure
COPY application/ ./application/

# Create indexes and vectors directories
RUN mkdir -p indexes vectors inputs

# Set environment variables
ENV PYTHONPATH="/app"
ENV PORT=7091

# Expose port
EXPOSE 7091

# Start command - optimized for low memory
CMD ["gunicorn", "--bind", "0.0.0.0:$PORT", "--workers", "1", "--max-requests", "100", "--timeout", "120", "--preload", "application.app:app"]