"""This module is for available message handlers."""
import logging
from telegram import Update
from telegram.ext import ContextTypes


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """This function is echo on any message from user."""
    logging.info(f"echo to user id {update.effective_chat.id}")
    await context.bot.send_message(chat_id=update.effective_chat.id, text="""
✨List of available commands:
/start - some info about bot
""")


async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """This function is echo on wrong command."""
    logging.info(f"unknown command from id {update.effective_chat.id}")
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f"""
Unknown command {update.message.text}\n
✨List of available commands:
/start - some info about bot
/caps - testing command
""")
