"""This module is for altering Application created by loader."""
from telegram.ext import CommandHandler, filters, MessageHandler
from .loader import application
from .handles import start, echo, unknown

"""Handlers"""
# Commands.
start_handler = CommandHandler('start', start)
# Messages.
echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND) & filters.ChatType.PRIVATE, echo)
# Other.
unknown_handler = MessageHandler(filters.COMMAND, unknown)

"""Adding handlers to application"""
application.add_handler(start_handler)
application.add_handler(echo_handler)
application.add_handler(unknown_handler)
