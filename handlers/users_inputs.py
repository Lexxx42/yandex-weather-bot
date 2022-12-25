"""This module is for available message handlers."""
import logging
from telegram import Update
from telegram.ext import ContextTypes


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logging.info(f"echo to user id {update.effective_chat.id}")
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)


async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logging.info(f"unknown command from id {update.effective_chat.id}")
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")
