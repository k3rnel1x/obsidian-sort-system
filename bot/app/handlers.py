import asyncio
from time import tzname
import os


from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command, CommandStart

from utils import get_index




route = Router()


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
    if not os.path.isdir(f"bot/data/{str(message.date)[:10]}"):
        os.mkdir(f"bot/data/{str(message.date)[:10]}")
    file = open(f"bot/data/{str(message.date)[:10]}/{str(message.date)[11:16]}.md", "a")
    file.writelines(message.text)
    file.close()
    await message.delete()




# только фото
@route.message(F.photo & ~F.caption)
async def image(message: Message):
    day_path = f"bot/data/{str(message.date)[:10]}" ## TODO: convert to a function
    if not os.path.isdir(day_path):
        os.mkdir(day_path) 
    
    
    if len(message.photo) == 1:
        index = get_index(day_path, str(message.date)[11:16])
        
        
    else:
        index = get_index()
        
        for image_idx in range(len(message.photo)):
            photo_index = index + image_idx + 1
            file = ...
            message.bot.download(file)
            
    await message.delete()
    ... #TODO download do database 50%  


# текст и фото
@route.message(F.photo & F.caption)
async def image(message: Message):
    if not os.path.isdir(f"bot/data/{str(message.date)[:10]}"):
        os.mkdir(f"bot/data/{str(message.date)[:10]}")
    await message.bot.download(file=message.photo[-1].file_id,
                               destination=f"{message.caption}.png")
    await message.delete()
    ... #TODO download do database


# документ
@route.message(F.document & ~F.caption)
async def image(message: Message):
    if not os.path.isdir(f"bot/data/{str(message.date)[:10]}"):
        os.mkdir(f"bot/data/{str(message.date)[:10]}")
    filename = message.document.file_name.lower()
    await message.bot.download(file=message.document.file_id,
                               destination=filename)
    await message.delete()
    ... #TODO download do database



# документ и текст
@route.message(F.document & F.caption)
async def image(message: Message):
    if not os.path.isdir(f"bot/data/{str(message.date)[:10]}"):
        os.mkdir(f"bot/data/{str(message.date)[:10]}")
    filename = message.document.file_name.lower()
    await message.bot.download(file=message.document.file_id,
                               destination=f"{message.caption}{filename[filename.find("."):]}") #TODO сделать поиск с конца
    await message.delete()
    ... #TODO download do database


