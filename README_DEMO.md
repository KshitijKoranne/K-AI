# K-AI Pharmaceutical Chatbot - Demo Instructions

## 🚀 Quick Start

### On Mac:
1. **Double-click** `START_K_AI_MAC.command`
2. **Wait 15 seconds** for services to start
3. **Browser opens automatically** at http://localhost:5173
4. **Start chatting** about pharmaceutical topics!

### On Windows:
1. **Double-click** `START_K_AI_WINDOWS.bat` 
2. **Wait 15 seconds** for services to start
3. **Browser opens automatically** at http://localhost:5173
4. **Start chatting** about pharmaceutical topics!

## 📋 Prerequisites

- **Docker Desktop** must be installed and running
- **8GB RAM** minimum (works on MacBook Air M1)
- **Internet connection** for OpenRouter API

## 🧪 Demo Questions

Try asking K-AI:
- "What does GMP stand for in pharma industry?"
- "What are Good Manufacturing Practices?"
- "Explain pharmaceutical validation procedures"
- "What are the key requirements for GMP documentation?"

## 📚 Document Upload

1. Click **"Sources"** button at bottom of chat
2. Upload your **PDF or DOCX** pharmaceutical SOPs
3. Ask questions about your specific documents
4. K-AI will search through your SOPs to answer

## 🛑 Stopping K-AI

### Mac:
- Double-click `STOP_K_AI.command`

### Windows:
- Run: `docker-compose -f deployment/docker-compose.yaml down`

## 🔧 Technical Details

- **Model**: Llama 3.2 3B via OpenRouter API
- **Database**: MongoDB for document storage
- **Vector Database**: Built-in for document search
- **API**: Your OpenRouter key is pre-configured
- **No local models** - everything runs through OpenRouter

## 📞 Support

- **Access URL**: http://localhost:5173
- **Configured for**: Pharmaceutical SOP documents
- **Production Ready**: Can handle 700+ SOP documents