import asyncio

from aiogram import Router, F, Bot
from aiogram.types import Message
from aiogram.filters import Command, Filter, CommandStart



route = Router()
msg_text = []


@route.message(CommandStart())
async def start_command(message: Message):
    msg_del = await message.answer("Запуск бота")
    await asyncio.sleep(1.2)
    await message.delete()
    await msg_del.edit_text("Бот работает")
    #TODO create db to save all msg id and del all history in chat exсept first


@route.message(lambda message: message.text)
async def default_text_message(message: Message):
    msg_text.append(message.text)
    await message.delete()
    #TODO only text


@route.message(lambda message: message.photo)
async def image(message: Message):
    await message.bot.download(file=message.photo[-1].file_id, destination="1.png")
    ... #TODO download do database


