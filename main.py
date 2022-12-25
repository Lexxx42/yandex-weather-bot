from telegram.ext import CommandHandler
from handlers import start
from loader import application

start_handler = CommandHandler('start', start)
application.add_handler(start_handler)
