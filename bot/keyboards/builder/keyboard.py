"""This module is for nested keyboard building."""
from telegram import ReplyKeyboardMarkup, KeyboardButton

keyboard_nested = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Weather forecast from Yandex", request_location=True),
        ],
    ],
    resize_keyboard=True, one_time_keyboard=True, input_field_placeholder="Please use the button."
)
