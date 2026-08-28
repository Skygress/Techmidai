import os
import logging
from flask import Flask, request
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes
from dotenv import load_dotenv
import random
from datetime import datetime

# Load environment variables
load_dotenv()

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Bot token from environment
TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
WEBHOOK_URL = os.getenv('WEBHOOK_URL', 'https://your-app.railway.app/webhook')

# Create Flask app
app = Flask(__name__)

# Create bot application
application = Application.builder().token(TOKEN).build()

# Add all the command handlers (same as before)
# ... (copy all the command functions from bot.py here) ...

# Webhook endpoint
@app.route('/webhook', methods=['POST'])
async def webhook():
    """Handle incoming updates via webhook."""
    try:
        update = Update.de_json(request.get_json(force=True), application.bot)
        await application.process_update(update)
        return 'OK', 200
    except Exception as e:
        logger.error(f"Error in webhook: {e}")
        return 'Error', 500

@app.route('/')
def index():
    return "TechMind AI Bot is running!"

if __name__ == '__main__':
    # Set webhook
    application.run_webhook(
        listen="0.0.0.0",
        port=int(os.environ.get('PORT', 8080)),
        url_path=TOKEN,
        webhook_url=f"{WEBHOOK_URL}/{TOKEN}"
    )
