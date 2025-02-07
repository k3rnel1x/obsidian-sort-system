import asyncio
import logging
import os, sys, shutil

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

from app.handlers import route
from __init__ import bot, dp


sys.path.insert(0, "./")
shutil.rmtree("bot/data")
os.mkdir("bot/data")

# Запуск бота
async def main():
    logging.basicConfig(level=logging.INFO)
    dp.include_router(route)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
