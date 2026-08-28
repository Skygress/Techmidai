import os
import logging
import random
from datetime import datetime
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters, CallbackContext
from dotenv import load_dotenv

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

# Tech and AI related responses
TECH_FACTS = [
    "🤖 The first AI program was written in 1951 by Christopher Strachey.",
    "💻 The first computer virus was created in 1983.",
    "📱 The first smartphone was IBM Simon, released in 1992.",
    "🌐 The World Wide Web was invented by Tim Berners-Lee in 1989.",
    "🧠 AI can now diagnose diseases better than some doctors.",
    "🎮 The first video game was 'Tennis for Two' in 1958.",
    "🔗 Blockchain technology was introduced in 2008 by Satoshi Nakamoto.",
    "☁️ Cloud computing started in the 1960s with time-sharing."
]

AI_TOOLS = [
    "🤖 **ChatGPT** - Advanced conversational AI",
    "🎨 **Midjourney** - AI art generation",
    "📊 **TensorFlow** - Open-source ML framework",
    "🐍 **PyTorch** - Machine learning library",
    "💬 **Claude** - Anthropic's AI assistant",
    "🧠 **Hugging Face** - AI model hub",
    "📝 **Jasper AI** - AI writing assistant",
    "🎵 **Suno AI** - AI music generation"
]

PROGRAMMING_TIPS = [
    "💡 Always write clean, readable code. Future you will thank you!",
    "🔧 Use version control (Git) for all your projects.",
    "📝 Document your code thoroughly.",
    "🧪 Write unit tests for critical functions.",
    "🚀 Optimize performance, but don't prematurely optimize.",
    "📚 Never stop learning - tech evolves daily!",
    "🤝 Contribute to open-source projects.",
    "💻 Practice coding daily, even for 30 minutes."
]

# Start command
def start(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    welcome_message = f"""
👋 Hello {user.first_name}! Welcome to **TechMind AI**!

🤖 Your AI-powered tech companion for:
• 📰 Latest tech & AI news
• 💻 Programming help & tips
• 🛠️ AI tools & resources
• 📊 Tech trends & insights

Use /help to see all available commands!

⚠️ **Disclaimer**: This bot provides general tech information and does not give financial, legal, or medical advice.
    """
    
    keyboard = [
        [InlineKeyboardButton("📰 Tech News", callback_data='news')],
        [InlineKeyboardButton("💻 Code Help", callback_data='code')],
        [InlineKeyboardButton("🛠️ AI Tools", callback_data='tools')],
        [InlineKeyboardButton("📈 Tech Trends", callback_data='trends')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    update.message.reply_text(
        welcome_message,
        reply_markup=reply_markup,
        parse_mode='Markdown'
    )

# Help command
def help_command(update: Update, context: CallbackContext) -> None:
    help_text = """
📚 **Available Commands:**

/start - Start the bot
/help - Show this help message
/news - Get latest tech & AI news
/code - Get programming tips
/tools - Discover AI & tech tools
/trends - Current tech trends
/about - About this bot
/feedback - Send feedback about the bot

💡 **Quick Tips:**
• Use the buttons in messages for quick actions
• All responses are AI-generated for educational purposes
• No personal data is stored

**Privacy Policy:** We don't store any user data. All interactions are anonymous.
    """
    update.message.reply_text(help_text, parse_mode='Markdown')

# News command
def news(update: Update, context: CallbackContext) -> None:
    news_items = [
        "🚀 **AI Breakthrough**: New language model achieves human-level reasoning",
        "📱 **Tech Update**: Smartphone sales surge with AI-powered features",
        "🔬 **Research**: Quantum computing reaches new milestone",
        "💡 **Innovation**: Scientists develop self-healing electronic materials",
        "🤖 **AI Ethics**: New framework for responsible AI development released",
        "🌍 **Sustainability**: Tech giants commit to carbon neutrality by 2030"
    ]
    
    selected_news = random.choice(news_items)
    
    message = f"""
📰 **Tech & AI News Update**

{selected_news}

📅 {datetime.now().strftime('%B %d, %Y')}

🔄 Use /news to get another update!

⚠️ **Note**: News is simulated for demonstration purposes.
    """
    update.message.reply_text(message, parse_mode='Markdown')

# Code help command
def code_help(update: Update, context: CallbackContext) -> None:
    tip = random.choice(PROGRAMMING_TIPS)
    
    message = f"""
💻 **Programming Help**

{tip}

🛠️ **Popular Tech Stacks:**
• **Frontend**: React, Vue, Angular
• **Backend**: Python, Node.js, Java
• **AI/ML**: TensorFlow, PyTorch, scikit-learn
• **Mobile**: React Native, Flutter, Swift

💡 Need specific help? Use /feedback to ask questions!
    """
    update.message.reply_text(message, parse_mode='Markdown')

# Tools command
def tools(update: Update, context: CallbackContext) -> None:
    tools_list = "\n".join(AI_TOOLS)
    
    message = f"""
🛠️ **Essential AI & Tech Tools**

{tools_list}

🔧 **Development Tools:**
• VS Code - Popular code editor
• Docker - Containerization
• GitHub - Version control
• Postman - API testing

📚 **Learning Resources:**
• Coursera, edX, Udacity
• Stack Overflow, GitHub
• Medium, Dev.to

⚠️ **Note**: These tools are for educational purposes.
    """
    update.message.reply_text(message, parse_mode='Markdown')

# Trends command
def trends(update: Update, context: CallbackContext) -> None:
    trends_list = """
📈 **Current Tech Trends (2026)**

🤖 **AI & ML:**
• Large Language Models (LLMs)
• Generative AI in creative fields
• AI-powered automation
• Ethical AI development

💻 **Development:**
• Web3 technologies
• Serverless computing
• Edge AI
• Progressive Web Apps

🔐 **Cybersecurity:**
• Zero-trust architecture
• AI in threat detection
• Quantum-safe encryption

🌍 **Green Tech:**
• Sustainable computing
• Energy-efficient AI
• Carbon-neutral data centers
    """
    
    message = f"""
{trends_list}

💡 Stay updated with /news for the latest developments!

⚠️ **Disclaimer**: Trends are for informational purposes only.
    """
    update.message.reply_text(message, parse_mode='Markdown')

# Feedback command
def feedback(update: Update, context: CallbackContext) -> None:
    message = """
📝 **Feedback**

We value your opinion! Share your feedback, suggestions, or report issues.

**How to submit:**
1. Reply to this message with your feedback
2. Or send a message directly

Your feedback helps improve this bot. No personal data is stored.

👍 **Rate the bot**: Send us a message with your rating (1-5 stars) and thoughts!
    """
    update.message.reply_text(message, parse_mode='Markdown')

# About command
def about(update: Update, context: CallbackContext) -> None:
    message = """
🤖 **About TechMind AI**

**TechMind AI** is your AI-powered tech companion created to help you:
• Stay updated with tech trends
• Learn about AI and programming
• Discover useful tools and resources

📌 **Features:**
• AI-generated tech insights
• Programming tips and tricks
• Curated AI tools list
• Tech trends analysis

🔒 **Privacy First:**
• No data storage
• Anonymous interactions
• No third-party sharing

👨‍💻 **Created by**: Tech enthusiasts for the community

📧 **Contact**: Use /feedback for any queries
    """
    update.message.reply_text(message, parse_mode='Markdown')

# Handle button callbacks
def button_callback(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    
    if query.data == 'news':
        news_items = [
            "🚀 **AI Breakthrough**: New language model achieves human-level reasoning",
            "📱 **Tech Update**: Smartphone sales surge with AI-powered features",
            "🔬 **Research**: Quantum computing reaches new milestone",
            "💡 **Innovation**: Scientists develop self-healing electronic materials",
            "🤖 **AI Ethics**: New framework for responsible AI development released",
            "🌍 **Sustainability**: Tech giants commit to carbon neutrality by 2030"
        ]
        selected_news = random.choice(news_items)
        message = f"""
📰 **Tech & AI News Update**

{selected_news}

📅 {datetime.now().strftime('%B %d, %Y')}

🔄 Use /news to get another update!
        """
        query.edit_message_text(message, parse_mode='Markdown')
    
    elif query.data == 'code':
        tip = random.choice(PROGRAMMING_TIPS)
        message = f"""
💻 **Programming Help**

{tip}

🛠️ **Popular Tech Stacks:**
• **Frontend**: React, Vue, Angular
• **Backend**: Python, Node.js, Java
• **AI/ML**: TensorFlow, PyTorch, scikit-learn
• **Mobile**: React Native, Flutter, Swift
        """
        query.edit_message_text(message, parse_mode='Markdown')
    
    elif query.data == 'tools':
        tools_list = "\n".join(AI_TOOLS)
        message = f"""
🛠️ **Essential AI & Tech Tools**

{tools_list}

🔧 **Development Tools:**
• VS Code - Popular code editor
• Docker - Containerization
• GitHub - Version control
• Postman - API testing
        """
        query.edit_message_text(message, parse_mode='Markdown')
    
    elif query.data == 'trends':
        message = """
📈 **Current Tech Trends (2026)**

🤖 **AI & ML:**
• Large Language Models (LLMs)
• Generative AI in creative fields
• AI-powered automation
• Ethical AI development

💻 **Development:**
• Web3 technologies
• Serverless computing
• Edge AI
• Progressive Web Apps

🔐 **Cybersecurity:**
• Zero-trust architecture
• AI in threat detection
• Quantum-safe encryption

🌍 **Green Tech:**
• Sustainable computing
• Energy-efficient AI
• Carbon-neutral data centers
        """
        query.edit_message_text(message, parse_mode='Markdown')

# Handle regular messages
def handle_message(update: Update, context: CallbackContext) -> None:
    if not update.message or not update.message.text:
        return
    
    user_message = update.message.text.lower()
    
    if 'hello' in user_message or 'hi' in user_message:
        response = "👋 Hello! I'm TechMind AI. Use /help to see what I can do!"
    elif 'thanks' in user_message or 'thank' in user_message:
        response = "You're welcome! 😊 Always happy to help with tech!"
    elif 'python' in user_message or 'code' in user_message:
        response = "🐍 Python is great! Use /code for programming tips!"
    elif 'ai' in user_message or 'artificial' in user_message:
        response = "🤖 AI is fascinating! Check /tools for AI resources!"
    elif 'news' in user_message:
        response = "📰 Use /news to get the latest tech updates!"
    else:
        response = """🤔 I'm here for tech and AI discussions! Use /help to see my capabilities.

⚠️ **Note**: I'm an educational bot and don't provide commercial services, financial advice, or engage in spam."""
    
    update.message.reply_text(response, parse_mode='Markdown')

# Error handler
def error_handler(update: Update, context: CallbackContext) -> None:
    logger.error(f"Update {update} caused error {context.error}")

# Main function
def main() -> None:
    """Start the bot."""
    if not TOKEN:
        logger.error("No token provided! Please set TELEGRAM_BOT_TOKEN in .env")
        return
    
    # Create Updater with older compatible version
    updater = Updater(TOKEN)
    dp = updater.dispatcher

    # Command handlers
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("news", news))
    dp.add_handler(CommandHandler("code", code_help))
    dp.add_handler(CommandHandler("tools", tools))
    dp.add_handler(CommandHandler("trends", trends))
    dp.add_handler(CommandHandler("feedback", feedback))
    dp.add_handler(CommandHandler("about", about))
    
    # Callback handler for buttons
    dp.add_handler(CallbackQueryHandler(button_callback))
    
    # Message handler for non-command messages
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))
    
    # Error handler
    dp.add_error_handler(error_handler)

    # Start the bot
    logger.info("TechMind AI Bot started successfully!")
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
