"""This module is for getting bot token from .env file."""
import os
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')
token_yandex_weather = os.getenv('token_yandex_weather')