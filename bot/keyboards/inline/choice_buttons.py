import logging
from telegram import InlineKeyboardButton, Update
from telegram.ext import ContextTypes

keyboard_inline = [
    [
        InlineKeyboardButton("Option 1", callback_data="1"),
        InlineKeyboardButton("Option 2", callback_data="2"),
    ],
    [InlineKeyboardButton("Option 3", callback_data="3")],
]


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Parses the CallbackQuery and updates the message text."""
    query = update.callback_query
    await query.answer()
    logging.info(f"inline keyboard click by user {update.effective_user.id}, click = {query.data}")
    await query.edit_message_text(text=f"Selected option: {query.data}")
