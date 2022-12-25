import logging
from telegram import Update
from telegram.ext import ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logging.info("used command start")
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")
