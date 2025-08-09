#!/usr/bin/env python3
"""
K-AI Simple Demo Server - Pharmaceutical Chatbot MVP
Lightweight version for Render deployment without database dependencies
"""

import os
from flask import Flask, render_template_string, request, jsonify
import openai

app = Flask(__name__)

# Configure OpenRouter
openai.api_key = os.getenv('API_KEY', 'your_openrouter_api_key_here')
openai.base_url = os.getenv('OPENAI_BASE_URL', 'https://openrouter.ai/api/v1')

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>K-AI Pharmaceutical Chatbot</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body { font-family: Arial, sans-serif; margin: 0; padding: 20px; background: #f5f5f5; }
        .container { max-width: 800px; margin: 0 auto; background: white; border-radius: 10px; padding: 20px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
        .header { text-align: center; color: #2c3e50; margin-bottom: 30px; }
        .header h1 { color: #e74c3c; margin: 0; }
        .header p { color: #666; margin: 10px 0 0 0; }
        .chat-box { height: 400px; border: 1px solid #ddd; border-radius: 5px; padding: 15px; overflow-y: auto; background: #fafafa; margin-bottom: 20px; }
        .message { margin-bottom: 15px; padding: 10px; border-radius: 5px; }
        .user { background: #3498db; color: white; text-align: right; }
        .assistant { background: #e8f5e9; color: #2e7d32; }
        .input-group { display: flex; gap: 10px; }
        .input-group input { flex: 1; padding: 12px; border: 1px solid #ddd; border-radius: 5px; font-size: 16px; }
        .input-group button { padding: 12px 20px; background: #e74c3c; color: white; border: none; border-radius: 5px; cursor: pointer; font-size: 16px; }
        .input-group button:hover { background: #c0392b; }
        .loading { color: #666; font-style: italic; }
        .examples { background: #f8f9fa; padding: 15px; border-radius: 5px; margin-bottom: 20px; }
        .examples h3 { margin-top: 0; color: #e74c3c; }
        .examples ul { margin: 10px 0; }
        .examples li { margin: 5px 0; cursor: pointer; color: #3498db; }
        .examples li:hover { text-decoration: underline; }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>K-AI Pharmaceutical Chatbot</h1>
            <p>Your intelligent assistant for pharmaceutical SOPs, GMP guidelines, and regulatory compliance</p>
        </div>
        
        <div class="examples">
            <h3>💊 Sample Questions:</h3>
            <ul>
                <li onclick="askQuestion('What does GMP stand for in pharmaceutical industry?')">What does GMP stand for in pharmaceutical industry?</li>
                <li onclick="askQuestion('Explain the key principles of Good Manufacturing Practices')">Explain the key principles of Good Manufacturing Practices</li>
                <li onclick="askQuestion('What are the requirements for pharmaceutical documentation?')">What are the requirements for pharmaceutical documentation?</li>
                <li onclick="askQuestion('How should pharmaceutical equipment be validated?')">How should pharmaceutical equipment be validated?</li>
            </ul>
        </div>
        
        <div id="chat-box" class="chat-box">
            <div class="message assistant">
                <strong>K-AI:</strong> Hello! I'm your pharmaceutical compliance assistant. Ask me about GMP, SOPs, regulatory requirements, or any pharmaceutical manufacturing questions.
            </div>
        </div>
        
        <div class="input-group">
            <input type="text" id="user-input" placeholder="Ask about pharmaceutical SOPs, GMP, validation..." onkeypress="if(event.key==='Enter') sendMessage()">
            <button onclick="sendMessage()">Send</button>
        </div>
    </div>

    <script>
        function askQuestion(question) {
            document.getElementById('user-input').value = question;
            sendMessage();
        }

        async function sendMessage() {
            const input = document.getElementById('user-input');
            const chatBox = document.getElementById('chat-box');
            const message = input.value.trim();
            
            if (!message) return;
            
            // Add user message
            chatBox.innerHTML += `<div class="message user"><strong>You:</strong> ${message}</div>`;
            input.value = '';
            
            // Add loading message
            chatBox.innerHTML += `<div class="message assistant loading" id="loading"><strong>K-AI:</strong> Analyzing pharmaceutical data...</div>`;
            chatBox.scrollTop = chatBox.scrollHeight;
            
            try {
                const response = await fetch('/chat', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({message: message})
                });
                
                const data = await response.json();
                
                // Remove loading message
                document.getElementById('loading').remove();
                
                // Add AI response
                chatBox.innerHTML += `<div class="message assistant"><strong>K-AI:</strong> ${data.response}</div>`;
                
            } catch (error) {
                document.getElementById('loading').remove();
                chatBox.innerHTML += `<div class="message assistant"><strong>K-AI:</strong> Sorry, I'm experiencing technical difficulties. Please try again.</div>`;
            }
            
            chatBox.scrollTop = chatBox.scrollHeight;
        }
    </script>
</body>
</html>
'''

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        user_message = data.get('message', '')
        
        # Create pharmaceutical context prompt
        system_prompt = """You are K-AI, a pharmaceutical compliance expert specializing in:
        - Good Manufacturing Practices (GMP)
        - Standard Operating Procedures (SOPs)
        - Pharmaceutical regulatory compliance
        - Drug manufacturing processes
        - Quality assurance and validation
        - FDA, EMA, and international pharmaceutical regulations
        
        Provide accurate, professional responses about pharmaceutical topics. If asked about non-pharmaceutical topics, politely redirect to pharmaceutical matters."""
        
        # Call OpenRouter API
        response = openai.chat.completions.create(
            model=os.getenv('LLM_NAME', 'meta-llama/llama-3.2-3b-instruct:free'),
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message}
            ],
            max_tokens=500,
            temperature=0.7
        )
        
        return jsonify({
            'response': response.choices[0].message.content.strip()
        })
        
    except Exception as e:
        return jsonify({
            'response': f'I apologize, but I encountered an error: {str(e)}. Please check if the OpenRouter API key is configured correctly.'
        }), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port, debug=False)