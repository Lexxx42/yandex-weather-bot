"""This module is for available message handlers."""
import logging
from telegram import Update
from telegram.ext import ContextTypes, CallbackContext
from .. import apis


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """This function is echo on any message from user."""
    logging.info(f"echo to user id {update.effective_chat.id}")
    await context.bot.send_message(chat_id=update.effective_chat.id, text="""
✨List of available commands:
/start - some info about bot
""")


async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """This function is echo on wrong command."""
    logging.info(f"unknown command from id {update.effective_chat.id}")
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f"""
Unknown command {update.message.text}\n
✨List of available commands:
/start - some info about bot
/caps - testing command
""")


async def location(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """This function is for handling user location."""
    current_pos = (update.message.location.latitude, update.message.location.longitude)
    logging.info(f"coordinates {current_pos[0], current_pos[1]}")
    yandex_weather = apis.get_weather_yandex(current_pos[0], current_pos[1])
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f"""
🌈 Your location is:
country: {yandex_weather['location']['country']}, region: {yandex_weather['location']['region']},
city: {yandex_weather['location']['city']}, district: {yandex_weather['location']['district']}

Weather now:
🌡 temperature: {yandex_weather['fact']['temp']} °C
🤔 feels like: {yandex_weather['fact']['feels_like']} °C
⚡️ condition: {yandex_weather['fact']['condition']}
💨 atmospheric pressure: {yandex_weather['fact']['pressure_mm']} mm Hg
🌬 wind speed: {yandex_weather['fact']['wind_speed']} m/sec
💧 humidity: {yandex_weather['fact']['humidity']} %
""")
