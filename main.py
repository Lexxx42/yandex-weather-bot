"""This module is for altering Application created by loader."""
from telegram.ext import CommandHandler, filters, MessageHandler
from handlers import start, echo
from loader import application

"""Handlers"""
start_handler = CommandHandler('start', start)
echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)

"""Adding handlers to application"""
application.add_handler(start_handler)
application.add_handler(echo_handler)
