"""This module is for available message handlers."""
import logging
from telegram import Update
from telegram.ext import ContextTypes, CallbackContext
from .. import apis


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


async def location(update: Update, context: CallbackContext):
    current_pos = (update.message.location.latitude, update.message.location.longitude)
    logging.info(f"coordinates {current_pos[0], current_pos[1]}")
    await apis.get_weather_yandex(current_pos[0], current_pos[1])
    return current_pos
