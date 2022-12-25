import logging
import TOKEN
import telegram
from telegram.ext import ApplicationBuilder

logging.basicConfig(
    format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
    handlers=[
        logging.FileHandler("my_log.log", mode='w'),
        logging.StreamHandler()],
    level=logging.INFO,
)

bot = telegram.Bot(TOKEN.BOT_TOKEN)
application = ApplicationBuilder().token(TOKEN.BOT_TOKEN).build()
