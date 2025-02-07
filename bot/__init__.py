import os

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv 

# переменные
load_dotenv()
TOKEN = os.getenv("TOKEN")

# Создаем объекты бота и диспетчера
bot = Bot(token=TOKEN)
dp = Dispatcher()
