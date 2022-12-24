import asyncio
from loader import bot, logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler


async def main():
    async with bot:
        print(await bot.get_me())
        print((await bot.get_updates())[0])
        await bot.send_message(text='Hi John!', chat_id=601278313)


if __name__ == '__main__':
    asyncio.run(main())
