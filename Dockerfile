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

# Set environment variables with defaults
ENV PYTHONPATH="/app"
ENV PORT=10000
ENV API_KEY="your_openrouter_api_key_here"
ENV LLM_PROVIDER="openai"
ENV LLM_NAME="meta-llama/llama-3.2-3b-instruct:free"
ENV OPENAI_BASE_URL="https://openrouter.ai/api/v1"
ENV MONGO_URI="mongodb://localhost:27017/docsgpt"
ENV CELERY_BROKER_URL="redis://localhost:6379/0"
ENV CELERY_RESULT_BACKEND="redis://localhost:6379/1"
ENV CACHE_REDIS_URL="redis://localhost:6379/2"

# Expose port
EXPOSE 10000

# Create a simple startup script
RUN echo '#!/bin/bash\n\
echo "Starting K-AI Pharmaceutical Chatbot..."\n\
echo "Port: ${PORT}"\n\
echo "API Provider: ${LLM_PROVIDER}"\n\
gunicorn --bind 0.0.0.0:${PORT} --workers 1 --max-requests 50 --timeout 300 --preload application.app:app\n\
' > /app/start.sh && chmod +x /app/start.sh

# Start command
CMD ["/app/start.sh"]