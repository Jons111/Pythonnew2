from aiogram import types
from filters import Guruh
from loader import dp


# Echo bot
@dp.message_handler(Guruh(),text='salom')
async def bot_echo(message: types.Message):
    await message.reply(text='Salom guruhdan yozdingiz')