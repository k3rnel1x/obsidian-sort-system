import asyncio

from aiogram import Router, F, Bot
from aiogram.types import Message
from aiogram.filters import Command, Filter, CommandStart



route = Router()
mes_text = []


@route.message(CommandStart())
async def start_command(message: Message):
    msg_del = await message.answer("Запуск бота")
    await asyncio.sleep(1.5)
    await message.delete()
    await msg_del.edit_text("Бот работает")


@route.message()
async def default_text_message(message: Message):
    mes_text.append(message.text)
    await message.delete()



