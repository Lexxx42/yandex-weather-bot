from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
from loader import bot
from handlers import start

if __name__ == '__main__':
    application = ApplicationBuilder().token(bot.token).build()
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)
    application.run_polling()
