#!/bin/bash

echo "🛑 Stopping K-AI Pharmaceutical Chatbot..."
echo "📍 Current directory: $(pwd)"

# Navigate to deployment directory
cd deployment

echo "🔧 Stopping K-AI services..."
docker-compose -f docker-compose.yaml down

echo ""
echo "✅ K-AI has been stopped successfully!"
echo "💾 Your data and configurations are saved"
echo "🚀 Run START_K_AI_MAC.command to restart anytime"

# Keep terminal open
read -p "Press Enter to close this window..."