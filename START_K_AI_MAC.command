#!/bin/bash

echo "🚀 Starting K-AI Pharmaceutical Chatbot..."
echo "📍 Current directory: $(pwd)"

# Check if Docker is running
if ! docker info > /dev/null 2>&1; then
    echo "❌ Docker is not running. Please start Docker Desktop and try again."
    exit 1
fi

echo "✅ Docker is running"

# Navigate to deployment directory
cd deployment

echo "🔧 Starting K-AI services..."
docker-compose -f docker-compose.yaml up -d

echo "⏳ Waiting for services to start..."
sleep 15

echo "🌐 Opening K-AI in your browser..."
open "http://localhost:5173"

echo ""
echo "🎉 K-AI Pharmaceutical Chatbot is now running!"
echo "📱 Access your chatbot at: http://localhost:5173"
echo ""
echo "📋 To stop K-AI later, run:"
echo "   docker-compose -f deployment/docker-compose.yaml down"
echo ""
echo "💡 Your OpenRouter API key is already configured"
echo "📚 Ready to chat about pharmaceutical SOPs and GMP!"

# Keep terminal open
read -p "Press Enter to close this window..."