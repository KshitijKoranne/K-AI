# Deploy K-AI to Render (Free Tier)

## 🚀 Quick Deployment Steps

### 1. Create GitHub Repository
```bash
cd /Users/kshitij/Desktop/Purushartha/K-AI/DocsGPT
git init
git add .
git commit -m "K-AI Pharmaceutical Chatbot ready for Render deployment"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/k-ai-docsgpt.git
git push -u origin main
```

### 2. Deploy on Render
1. **Go to** [render.com](https://render.com)
2. **Sign up/Login** with GitHub
3. **Click "New +"** → **"Web Service"**
4. **Connect your GitHub repo** `k-ai-docsgpt`
5. **Use these settings:**
   - **Build Command:** `docker build -t k-ai .`
   - **Start Command:** `docker-compose up`
   - **Environment:** Docker

### 3. Environment Variables
Add these in Render dashboard:
```
API_KEY=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
LLM_PROVIDER=openai  
LLM_NAME=meta-llama/llama-3.2-3b-instruct:free
OPENAI_BASE_URL=https://openrouter.ai/api/v1
VITE_API_STREAMING=true
```

### 4. Add Databases
1. **Create MongoDB** (free tier)
2. **Create Redis** (free tier) 
3. **Link to your web service**

## 🌐 Result
- **Live URL:** `https://k-ai-pharma.onrender.com`
- **Demo ready** - share this URL anywhere
- **No downloads** needed for demos
- **Professional pharmaceutical chatbot**

## 📋 Free Tier Limits
- ✅ 100GB bandwidth/month (plenty for demos)
- ✅ Always-on service
- ✅ Custom domain support
- ✅ SSL certificate included

## 🎯 Demo Process
1. **Share the URL:** `https://k-ai-pharma.onrender.com`  
2. **Upload SOPs** via Sources button
3. **Ask pharmaceutical questions**
4. **Works on any device** - no installation needed