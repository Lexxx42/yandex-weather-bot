"""This module is for nested keyboard building."""
from telegram import ReplyKeyboardMarkup, KeyboardButton

keyboard_nested = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Share your location", request_location=True),
        ],
    ],
    resize_keyboard=True
)
