# Sai's Telegram Bot - FastAPI + Vercel Deployment 🚀

A cute and expressive Telegram bot powered by Google's Gemini AI, now optimized for serverless deployment on Vercel using FastAPI.

## 🏗️ Architecture

- **FastAPI**: High-performance async web framework
- **Vercel**: Serverless deployment platform
- **Webhook Mode**: Efficient real-time message handling
- **Gemini AI**: Google's latest AI model for intelligent responses

## 📁 Project Structure

```
telegrambot/
├── api/
│   └── index.py          # Main FastAPI application
├── re.txt                # Sai's profile information
├── .env                  # Environment variables (local)
├── .env.example          # Environment variables template
├── vercel.json           # Vercel deployment configuration
├── requirements.txt      # Python dependencies
├── README.md            # This file
└── DEPLOYMENT.md        # Deployment guide
```

## 🚀 Quick Deployment Guide

### Prerequisites

1. **Vercel Account**: Sign up at [vercel.com](https://vercel.com)
2. **Telegram Bot Token**: Get from @BotFather on Telegram
3. **Gemini API Key**: Get from [Google AI Studio](https://makersuite.google.com/app/apikey)

### Step 1: Deploy to Vercel

1. **Push to GitHub**:
   ```bash
   git init
   git add .
   git commit -m "Initial commit - FastAPI Telegram bot"
   git branch -M main
   git remote add origin https://github.com/yourusername/your-repo-name.git
   git push -u origin main
   ```

2. **Deploy on Vercel**:
   - Go to [vercel.com/dashboard](https://vercel.com/dashboard)
   - Click "New Project"
   - Import your GitHub repository
   - Vercel will auto-detect the configuration from `vercel.json`

### Step 2: Configure Environment Variables

In your Vercel project dashboard, go to **Settings** → **Environment Variables** and add:

```
BOT_ID = your_telegram_bot_token_here
GEMINI_API = your_gemini_api_key_here  
WEBHOOK_URL = https://your-project-name.vercel.app
```

### Step 3: Set Up Webhook

After deployment, visit your webhook setup endpoint:
```
https://your-project-name.vercel.app/set_webhook
```

This will automatically configure Telegram to send updates to your bot.

## 🔧 Local Development

### Setup

1. **Clone and install dependencies**:
   ```bash
   git clone <your-repo>
   cd telegrambot
   python -m venv venv
   # Windows
   .\venv\Scripts\activate
   # Linux/Mac  
   source venv/bin/activate
   
   pip install -r requirements.txt
   ```

2. **Configure environment**:
   ```bash
   cp .env.example .env
   # Edit .env with your tokens
   ```

3. **Run locally**:
   ```bash
   uvicorn api.index:app --reload --port 8000
   ```

4. **Test endpoints**:
   - Health check: `http://localhost:8000/`
   - Webhook info: `http://localhost:8000/webhook_info`

## 📡 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Health check |
| `/webhook` | POST | Telegram webhook handler |
| `/set_webhook` | GET | Set webhook URL |
| `/webhook_info` | GET | Get current webhook info |

## 🤖 Bot Features

### Commands
- `/start` - Welcome message and bot introduction
- `/help` - Show available commands  
- `/about_sai` - Get information about Sai Mahendra

### Smart Features
- **Sai Detection**: Automatically detects questions about Sai Mahendra
- **Context Awareness**: Uses `re.txt` for detailed responses
- **Gemini AI**: Powered by Google's latest AI model
- **No Emojis**: Cute and expressive through words only

## 🔍 Monitoring & Debugging

### Check Webhook Status
```bash
curl https://your-project-name.vercel.app/webhook_info
```

### View Logs
- Go to Vercel Dashboard → Your Project → Functions tab
- Click on any function to view real-time logs

### Common Issues

1. **Webhook not receiving updates**:
   - Check if webhook URL is set correctly
   - Ensure environment variables are configured
   - Visit `/set_webhook` endpoint

2. **Gemini API errors**:
   - Verify API key is valid
   - Check quota limits
   - Review logs for specific error messages

3. **File not found (re.txt)**:
   - Ensure `re.txt` is in the root directory
   - Check file encoding (UTF-8)

## 🚀 Advanced Configuration

### Custom Webhook URL
```python
# Set custom webhook programmatically
import requests
response = requests.get(
    "https://your-project-name.vercel.app/set_webhook?webhook_url=https://your-custom-domain.com"
)
```

### Environment Variables
```bash
# Required
BOT_ID=your_telegram_bot_token
GEMINI_API=your_gemini_api_key

# Optional  
WEBHOOK_URL=https://your-custom-domain.com
```

## 📊 Performance

- **Cold Start**: ~1-2 seconds (typical for serverless)
- **Response Time**: ~200-500ms for simple queries
- **Gemini API**: ~1-3 seconds for AI responses
- **Concurrent Users**: Unlimited (serverless auto-scaling)

## 🔐 Security

- Environment variables are securely stored in Vercel
- HTTPS-only webhook endpoints
- Input validation and error handling
- Rate limiting handled by Telegram

## 💡 Development Tips

1. **Local Testing**: Use ngrok to expose local server for webhook testing
2. **Debugging**: Check Vercel function logs for detailed error messages
3. **Updates**: Any git push to main branch triggers automatic redeployment
4. **Rollback**: Use Vercel dashboard to rollback to previous deployments

---

## 🎯 Next Steps

1. **Deploy**: Follow the deployment guide above
2. **Test**: Send messages to your bot on Telegram
3. **Monitor**: Check logs and webhook status
4. **Customize**: Modify `re.txt` to update Sai's information
5. **Scale**: Add more features to the FastAPI app

Your bot is now ready for production use! 🎉

---

**Created by Sai Mahendra - God Tier Programmer** ⚡