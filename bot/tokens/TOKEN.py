"""This module is for getting bot token from .env file."""
import os
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')
TOKEN_YANDEX_WEATHER = os.getenv('TOKEN_YANDEX_WEATHER')
