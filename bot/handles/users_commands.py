"""This module is for available commands handlers."""
import logging
from telegram import Update, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from .. import keyboards


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """This function is for /start command."""
    logging.info(f"used command start by user id {update.effective_chat.id}")
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f"""
Hello {update.effective_chat.username}!
I'm a weather bot and can show you your local weather forecast!
simply use /weather and I''show it
\U00002B50Happy using :p
""", reply_markup=InlineKeyboardMarkup(keyboards.keyboard_inline))


async def caps(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """This function is for /caps command."""
    text_caps = ' '.join(context.args).upper()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)
