import asyncio
from time import tzname

from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command, CommandStart




route = Router()
msg_text = []


@route.message(CommandStart())
async def start_command(message: Message):
    msg_del = await message.answer("Запуск бота")
    await asyncio.sleep(1.2)
    await message.delete()
    await msg_del.edit_text("Бот работает")
    #TODO create db to save all msg id and del all history in chat exсept first

# обрабатываем все сообщения

# только текст
@route.message(F.text)
async def default_text_message(message: Message):
    msg_text.append(message.text)
    await message.delete()
    #TODO only text


# только фото
@route.message(F.photo & ~F.caption)
async def image(message: Message):
    await message.bot.download(file=message.photo[-1].file_id, destination="onlyimg.png")
    await message.delete()
    ... #TODO download do database


# текст и фото
@route.message(F.photo & F.caption)
async def image(message: Message):
    await message.bot.download(file=message.photo[-1].file_id,
                               destination=f"{message.caption}.png")
    await message.delete()
    ... #TODO download do database


# документ
@route.message(F.document & ~F.caption)
async def image(message: Message):
    filename = message.document.file_name.lower()
    await message.bot.download(file=message.document.file_id,
                               destination=filename)
    await message.delete()
    ... #TODO download do database



# документ и текст
@route.message(F.document & F.caption)
async def image(message: Message):
    filename = message.document.file_name.lower()
    await message.bot.download(file=message.document.file_id,
                               destination=f"{message.caption}{filename[filename.find("."):]}") #TODO сделать поиск с конца
    await message.delete()
    ... #TODO download do database


