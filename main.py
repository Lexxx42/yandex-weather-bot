"""This module is for altering Application created by loader."""
from telegram.ext import CommandHandler, InlineQueryHandler, filters, MessageHandler
from loader import application
from handlers import start, echo, caps
from keyboards import inline_caps


"""Handlers"""
start_handler = CommandHandler('start', start)
echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
caps_handler = CommandHandler('caps', caps)
inline_caps_handler = InlineQueryHandler(inline_caps)

"""Adding handlers to application"""
application.add_handler(start_handler)
application.add_handler(echo_handler)
application.add_handler(caps_handler)
application.add_handler(inline_caps_handler)
