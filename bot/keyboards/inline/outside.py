"""This module is for inline mode outside of bot."""
import logging
from telegram import Update
from telegram.ext import ContextTypes
from telegram import InlineQueryResultArticle, InputTextMessageContent


async def inline_caps(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """This function is for inline callbacks from outside of bot."""
    query = update.inline_query.query
    logging.info(f"inline outside {update.effective_user.id}")
    if not query:
        return
    results = [InlineQueryResultArticle(
        id=query.upper(),
        title='CAPS',
        input_message_content=InputTextMessageContent(query.upper())
    )]
    await context.bot.answer_inline_query(update.inline_query.id, results)
