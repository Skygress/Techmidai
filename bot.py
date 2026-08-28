import os
import logging
import random
from datetime import datetime
from telethon import TelegramClient, events, Button
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
API_ID = os.getenv('API_ID')
API_HASH = os.getenv('API_HASH')
BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

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

# Create the client
bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

# Start command
@bot.on(events.NewMessage(pattern='/start'))
async def start(event):
    user = await event.get_sender()
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
    
    buttons = [
        [Button.inline("📰 Tech News", b"news")],
        [Button.inline("💻 Code Help", b"code")],
        [Button.inline("🛠️ AI Tools", b"tools")],
        [Button.inline("📈 Tech Trends", b"trends")]
    ]
    
    await event.respond(welcome_message, buttons=buttons)

# Help command
@bot.on(events.NewMessage(pattern='/help'))
async def help_command(event):
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
    await event.respond(help_text)

# News command
@bot.on(events.NewMessage(pattern='/news'))
async def news(event):
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
    await event.respond(message)

# Code help command
@bot.on(events.NewMessage(pattern='/code'))
async def code_help(event):
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
    await event.respond(message)

# Tools command
@bot.on(events.NewMessage(pattern='/tools'))
async def tools(event):
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
    await event.respond(message)

# Trends command
@bot.on(events.NewMessage(pattern='/trends'))
async def trends(event):
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
    await event.respond(message)

# Feedback command
@bot.on(events.NewMessage(pattern='/feedback'))
async def feedback(event):
    message = """
📝 **Feedback**

We value your opinion! Share your feedback, suggestions, or report issues.

**How to submit:**
1. Reply to this message with your feedback
2. Or send a message directly

Your feedback helps improve this bot. No personal data is stored.

👍 **Rate the bot**: Send us a message with your rating (1-5 stars) and thoughts!
    """
    await event.respond(message)

# About command
@bot.on(events.NewMessage(pattern='/about'))
async def about(event):
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
    await event.respond(message)

# Handle button callbacks
@bot.on(events.CallbackQuery)
async def button_callback(event):
    data = event.data.decode()
    
    if data == 'news':
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
        await event.answer()
        await event.edit(message)
    
    elif data == 'code':
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
        await event.answer()
        await event.edit(message)
    
    elif data == 'tools':
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
        await event.answer()
        await event.edit(message)
    
    elif data == 'trends':
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
        """
        await event.answer()
        await event.edit(message)

# Handle regular messages
@bot.on(events.NewMessage)
async def handle_message(event):
    # Ignore commands
    if event.message.text and event.message.text.startswith('/'):
        return
    
    user_message = event.message.text.lower() if event.message.text else ""
    
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
    
    await event.respond(response)

# Start the bot
def main():
    logger.info("TechMind AI Bot started successfully!")
    logger.info("Bot is running with Telethon!")
    bot.run_until_disconnected()

if __name__ == '__main__':
    if not all([API_ID, API_HASH, BOT_TOKEN]):
        logger.error("Missing environment variables! Please set API_ID, API_HASH, and TELEGRAM_BOT_TOKEN")
    else:
        main()
