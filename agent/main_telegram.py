"""
Telegram bot application for the agent.
"""

import os

from dotenv import load_dotenv
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)

from agent.telegram_agent import process_telegram_message

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")


# =====================================================
# Command Handlers
# =====================================================
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle the /start command."""
    await update.message.reply_text(
        "Hello! I'm your intelligent assistant. Send me a message and I'll help you!"
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle the /help command."""
    await update.message.reply_text(
        "Just send me any message and I'll process it with AI. "
        "I can help you with various tasks!"
    )


# =====================================================
# Message Handler
# =====================================================
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle incoming text messages."""
    user_id = str(update.effective_user.id)
    username = update.effective_user.username or "Unknown"
    message_text = update.message.text

    print(f"💬 Message from {username} ({user_id}): {message_text}")

    # Process message with the agent
    response_message = process_telegram_message(user_id, message_text)
    print(f"🤖 Agent response: {response_message}")

    # response_message = f"Processing your message: {message_text}"
    # Send agent response
    await update.message.reply_text(response_message)


# =====================================================
# Error Handler
# =====================================================
async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle errors."""
    print(f"⚠️ Error: {context.error}")


# =====================================================
# Main Application
# =====================================================
def main():
    """Start the Telegram bot."""
    print("🚀 Starting Telegram bot...")

    # Create application
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    # Add handlers
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message)
    )

    # Add error handler
    application.add_error_handler(error_handler)

    # Start the bot
    print("✅ Bot is running...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
