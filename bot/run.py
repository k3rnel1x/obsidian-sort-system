import asyncio
import logging
import os

from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import CommandStart, Command


from dotenv import load_dotenv
load_dotenv()

# Укажите свой токен
TOKEN = os.getenv("TOKEN")

print(TOKEN)

# Создаем объекты бота и диспетчера
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Обработчик команды /start
@dp.message(CommandStart())
async def start_handler(message: Message):
    await message.answer("Привет!")

# Обработчик команды /help
@dp.message(Command("help"))
async def help_handler(message: Message):
    await message.answer("помощь")













# Запуск бота
async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
