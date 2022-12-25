"""This module is for altering Application created by loader."""
from telegram.ext import CommandHandler, InlineQueryHandler, filters, MessageHandler, CallbackQueryHandler
from .loader import application
from .handles import start, echo, caps, unknown
from .keyboards import inline_caps, button

"""Handlers"""
# Commands.
start_handler = CommandHandler('start', start)
caps_handler = CommandHandler('caps', caps)
# Messages.
echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND) & filters.ChatType.PRIVATE, echo)
# Inline.
inline_caps_handler = InlineQueryHandler(inline_caps)
# Other.
unknown_handler = MessageHandler(filters.COMMAND, unknown)

"""Adding handlers to application"""
application.add_handler(start_handler)
application.add_handler(caps_handler)
application.add_handler(echo_handler)
application.add_handler(inline_caps_handler)
application.add_handler(unknown_handler)
application.add_handler(CallbackQueryHandler(button))
