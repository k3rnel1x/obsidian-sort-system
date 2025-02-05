import asyncio
import logging
import os

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

from app.handlers import route

# переменные
load_dotenv()
TOKEN = os.getenv("TOKEN")



# Создаем объекты бота и диспетчера
bot = Bot(token=TOKEN)
dp = Dispatcher()



# Запуск бота
async def main():
    logging.basicConfig(level=logging.INFO)
    dp.include_router(route)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
