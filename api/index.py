import os
import logging
from typing import Dict, Any
import asyncio
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
import google.generativeai as genai
from dotenv import load_dotenv
import httpx

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="Sai's Telegram Bot", version="1.0.0")

class SaiBot:
    def __init__(self):
        self.bot_token = os.getenv('BOT_ID')
        self.gemini_api_key = os.getenv('GEMINI_API')
        self.webhook_url = os.getenv('WEBHOOK_URL', '')
        
        if not self.bot_token or not self.gemini_api_key:
            raise ValueError("BOT_ID and GEMINI_API must be set in environment variables")
        
        # Configure Gemini API
        genai.configure(api_key=self.gemini_api_key)
        self.model = genai.GenerativeModel('gemini-2.0-flash')
        
        # Load reference information about Sai
        self.load_sai_info()
        
        # System instruction for Gemini
        self.system_instruction = f"""
        You are a cute and expressive assistant without emojis.
When asked about Sai or Sai Mahendra, reply warmly, playfully, and based on {self.sai_info}.
Keep answers under 3 lines, concise and friendly.
Always be helpful, engaging, and respond in multiple languages when possible.
        """
    
    def load_sai_info(self):
        """Load information about Sai from re.txt file"""
        try:
            # Try different possible paths
            possible_paths = ['re.txt', '../re.txt', './re.txt']
            for path in possible_paths:
                try:
                    with open(path, 'r', encoding='utf-8') as file:
                        self.sai_info = file.read().strip()
                        logger.info(f"Loaded Sai info from {path}")
                        return
                except FileNotFoundError:
                    continue
            
            # If no file found, use default
            self.sai_info = """
            Bejawada Sai Mahendra is a young, brilliant student developer who is passionate about technology and innovation. 
            He's a god-tier programmer with exceptional talent for coding and problem-solving. Currently pursuing BTech CSE 4th year 
            and BBA 2nd year at KLEF with excellent academics (CSE CGPA: 9.45, BBA CGPA: 8.5). 
            Skills include C, Java, Python, React.js, Express.js, sql and what not. Notable projects include Skillcert (full-stack microservices) 
            and Generative AI realtime video integration and more. He loves anime and is always exploring new technologies.
            """
            logger.warning("re.txt file not found, using default info")
            
        except Exception as e:
            self.sai_info = "Sai Mahendra is a talented programmer"
            logger.error(f"Error loading Sai info: {e}")
    
    async def send_message(self, chat_id: int, text: str):
        """Send message to Telegram chat"""
        url = f"https://api.telegram.org/bot{self.bot_token}/sendMessage"
        payload = {
            "chat_id": chat_id,
            "text": text,
            "parse_mode": "HTML"
        }
        
        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(url, json=payload, timeout=10.0)
                response.raise_for_status()
                return response.json()
            except Exception as e:
                logger.error(f"Error sending message: {e}")
                raise
    
    async def send_document(self, chat_id: int, document_url: str, caption: str = None):
        """Send document/PDF to Telegram chat"""
        url = f"https://api.telegram.org/bot{self.bot_token}/sendDocument"
        payload = {
            "chat_id": chat_id,
            "document": document_url,
        }
        if caption:
            payload["caption"] = caption
            payload["parse_mode"] = "HTML"
        
        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(url, json=payload, timeout=30.0)
                response.raise_for_status()
                return response.json()
            except Exception as e:
                logger.error(f"Error sending document: {e}")
                # Fallback to sending a message with the link
                await self.send_message(chat_id, f"📄 Here's Sai's resume: {document_url}")
                raise
    
    async def generate_gemini_response(self, prompt: str) -> str:
        """Generate response using Gemini API"""
        try:
            response = self.model.generate_content(prompt)
            if response.text:
                return response.text
            else:
                logger.warning("Gemini returned empty response")
                return "Hmm, I'm not sure how to respond to that. Could you try asking in a different way?"
        except Exception as e:
            logger.error(f"Gemini API error: {e}")
            error_str = str(e).lower()
            if "404" in error_str or "not found" in error_str:
                return "My AI brain needs an update! The developer should check the Gemini model configuration."
            elif "api key" in error_str or "authentication" in error_str:
                return "There's an issue with my API credentials. Please check with my developer!"
            elif "quota" in error_str or "limit" in error_str:
                return "I've been thinking too much today! Please try again in a few minutes."
            else:
                return "Sorry, I'm having trouble connecting to my brain right now. Please try again later!"
    
    async def handle_start_command(self, chat_id: int):
        """Handle /start command"""
        welcome_message = """
 <h1>Hello visitor </h1><br><p>I am telegram bot created by sai mahendra, you can ask me anything about him i will try to tell about his work and details as per data i trained for 
        """
        await self.send_message(chat_id, welcome_message.strip())
    
    async def handle_help_command(self, chat_id: int):
        """Handle /help command"""
        help_text = """
📋 <b>Available commands:</b>
• /start - Start the bot and get a welcome message
• /help - Show this help message  
• /about_sai - Just some self info about me
• /resume - Get Sai's resume PDF
        """
        await self.send_message(chat_id, help_text.strip())
    
    async def handle_about_sai_command(self, chat_id: int):
        """Handle /about_sai command"""
        response = await self.generate_gemini_response(
            "Tell me about Sai Mahendra, the programmer. Be cute and expressive but don't use emojis."
        )
        await self.send_message(chat_id, response)
    
    async def handle_resume_command(self, chat_id: int):
        """Handle /resume command - sends Sai's resume PDF"""
        resume_url = "https://raw.githubusercontent.com/saimahendra282/telegram_bot/main/allpurposefin.pdf"
        await self.send_document(chat_id, resume_url)
    
    async def handle_message(self, chat_id: int, message_text: str):
        """Handle regular text messages"""
        logger.info(f"Received message: {message_text}")
        
        # Check if the message is asking about Sai
        sai_keywords = ['sai', 'sai mahendra', 'who is sai', 'about sai', 'tell me about sai', 'bejawada sai mahendra', 'mahendra']
        is_about_sai = any(keyword in message_text.lower() for keyword in sai_keywords)
        
        if is_about_sai:
            prompt = f"The user is asking about Sai: '{message_text}'. {self.system_instruction}"
        else:
            prompt = f"{self.system_instruction}\n\nUser message: {message_text}"
        
        try:
            response = await self.generate_gemini_response(prompt)
            await self.send_message(chat_id, response)
        except Exception as e:
            logger.error(f"Error generating response: {e}")
            await self.send_message(chat_id, "Oops! Something went wrong while I was thinking. Please try again in a moment.")

# Initialize bot
bot = SaiBot()

@app.get("/")
async def root():
    """Health check endpoint"""
    return {"status": "Sai's Telegram Bot is running!", "version": "1.0.0"}

@app.post("/webhook")
async def webhook(request: Request):
    """Handle incoming webhook from Telegram"""
    try:
        data = await request.json()
        logger.info(f"Received webhook data: {data}")
        
        # Check if it's a message update
        if 'message' not in data:
            return JSONResponse({"status": "ok"})
        
        message = data['message']
        chat_id = message['chat']['id']
        
        # Handle commands
        if 'text' in message:
            text = message['text']
            
            if text.startswith('/start'):
                await bot.handle_start_command(chat_id)
            elif text.startswith('/help'):
                await bot.handle_help_command(chat_id)
            elif text.startswith('/about_sai'):
                await bot.handle_about_sai_command(chat_id)
            elif text.startswith('/resume'):
                await bot.handle_resume_command(chat_id)
            else:
                await bot.handle_message(chat_id, text)
        
        return JSONResponse({"status": "ok"})
        
    except Exception as e:
        logger.error(f"Webhook error: {e}")
        return JSONResponse({"status": "error", "message": str(e)}, status_code=500)

@app.get("/set_webhook")
async def set_webhook(webhook_url: str = None):
    """Set webhook URL for the bot"""
    if not webhook_url:
        webhook_url = bot.webhook_url
    
    if not webhook_url:
        raise HTTPException(status_code=400, detail="Webhook URL not provided")
    
    url = f"https://api.telegram.org/bot{bot.bot_token}/setWebhook"
    payload = {"url": f"{webhook_url}/webhook"}
    
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(url, json=payload)
            response.raise_for_status()
            result = response.json()
            logger.info(f"Webhook set successfully: {result}")
            return result
        except Exception as e:
            logger.error(f"Error setting webhook: {e}")
            raise HTTPException(status_code=500, detail=str(e))

@app.get("/webhook_info")
async def get_webhook_info():
    """Get current webhook information"""
    url = f"https://api.telegram.org/bot{bot.bot_token}/getWebhookInfo"
    
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            logger.error(f"Error getting webhook info: {e}")
            raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=6969)