import logging
import telegram
import TOKEN

bot = telegram.Bot(TOKEN.BOT_TOKEN)

logging.basicConfig(
    format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
    handlers=[
        logging.FileHandler("my_log.log", mode='w'),
        logging.StreamHandler()],
    level=logging.INFO,
)
