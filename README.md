# Sai's Telegram Bot - FastAPI Edition 🤖

A cute and expressive Telegram bot powered by Google's Gemini AI, built with FastAPI for serverless deployment on Vercel.

## Features

- **FastAPI Framework**: High-performance async web framework
- **Serverless Ready**: Optimized for Vercel deployment
- **Webhook Mode**: Efficient real-time message handling
- **Gemini AI Integration**: Uses Google's Gemini 2.0 Flash model for intelligent responses
- **Personalized Responses**: Special knowledge about Sai Mahendra with cute, expressive replies (no emojis)
- **Command Support**: Various commands for different interactions
- **Context Awareness**: Reads from `re.txt` for reference information about Sai
- **Error Handling**: Robust error handling with logging

## Setup Instructions

### Prerequisites

- Python 3.7 or higher
- A Telegram Bot Token (get from @BotFather on Telegram)
- Google Gemini API Key

### Installation

1. **Clone or download the project**
   ```bash
   cd d:\telegrambot
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   
   Edit the `.env` file and add your tokens:
   ```
   BOT_ID=your_telegram_bot_token_here
   GEMINI_API=your_gemini_api_key_here
   ```

   **How to get these tokens:**
   
   - **Telegram Bot Token**: 
     1. Message @BotFather on Telegram
     2. Send `/newbot`
     3. Follow the instructions
     4. Copy the token provided
   
   - **Gemini API Key**:
     1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
     2. Create a new API key
     3. Copy the key

5. **Update reference file (optional)**
   
   Edit `re.txt` to add more information about Sai that the bot can reference when users ask about him.

### Local Development

1. **Activate the virtual environment**
   ```bash
   .\venv\Scripts\Activate.ps1
   ```

2. **Install FastAPI dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the FastAPI development server**
   ```bash
   uvicorn api.index:app --reload --port 8000
   ```

4. **Test the endpoints**
   - Health check: `http://localhost:8000/`
   - Webhook info: `http://localhost:8000/webhook_info`
   - Run test suite: `python test_fastapi.py`

### Vercel Deployment

1. **Push to GitHub** and connect to Vercel
2. **Configure environment variables** in Vercel dashboard:
   - `BOT_ID` = your Telegram bot token
   - `GEMINI_API` = your Gemini API key
   - `WEBHOOK_URL` = your Vercel app URL
3. **Set webhook** by visiting: `https://your-app.vercel.app/set_webhook`

📖 **See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed deployment instructions**

## Available Commands

- `/start` - Welcome message and bot introduction
- `/help` - Show available commands
- `/about_sai` - Get information about Sai Mahendra

## Bot Behavior

- **About Sai**: When users ask about Sai, Sai Mahendra, or related questions, the bot responds with cute, expressive messages based on information from `re.txt`
- **General Chat**: For other messages, the bot uses Gemini AI to provide helpful and friendly responses
- **No Emojis**: The bot is designed to be expressive through words, not emojis
- **Error Handling**: If something goes wrong, the bot provides friendly error messages

## File Structure

```
telegrambot/
├── bot.py              # Main bot application
├── .env                # Environment variables (your tokens)
├── re.txt              # Reference information about Sai
├── requirements.txt    # Python dependencies
├── README.md           # This file
└── venv/              # Virtual environment (created after setup)
```

## Development Notes

- The bot uses async/await for handling multiple users
- Logging is configured to help with debugging
- The system instruction ensures consistent personality when responding about Sai
- Error handling includes both Telegram API and Gemini API errors

## Troubleshooting

1. **Bot not responding**: Check if your `BOT_ID` token is correct
2. **AI responses not working**: Verify your `GEMINI_API` key is valid
3. **Import errors**: Make sure virtual environment is activated and dependencies are installed
4. **File not found errors**: Ensure `re.txt` exists in the same directory as `bot.py`

## Portfolio Notes

This bot demonstrates:
- Integration with multiple APIs (Telegram Bot API, Google Gemini API)
- Environment variable management
- Async programming in Python
- Error handling and logging
- Object-oriented programming
- File I/O operations
- Virtual environment usage

Perfect for showcasing full-stack development skills with AI integration!

---

Created by Sai Mahendra - God Tier Programmer 💻