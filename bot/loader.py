"""This module is for creating the Application and logging mask."""
import logging
from .tokens import BOT_TOKEN
from telegram.ext import ApplicationBuilder

logging.basicConfig(
    format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
    handlers=[
        logging.FileHandler("my_log.log", mode='w'),
        logging.StreamHandler()],
    level=logging.INFO,
)

application = ApplicationBuilder().token(BOT_TOKEN).build()
