"""This module is for available commands handlers."""
import logging
from telegram import Update
from telegram.ext import ContextTypes
from .. import keyboards


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """This function is for /start command."""
    logging.info(f"used command start by user id {update.effective_chat.id}")
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f"""
Hello {update.effective_chat.username}!
I'm a weather bot and can show you your local weather forecast!
Simply use /start and click on the button
\U00002B50Happy using :p
""", reply_markup=keyboards.keyboard_nested)


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """This function is for /help command."""
    logging.info(f"used command help by user id {update.effective_chat.id}")
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f"""
<b>This bot was created by</b> <a href="https://github.com/Lexxx42">Lexxx42</a>
Bot can accept location by clicking a location button
or by send data from user.
""", parse_mode='html')
