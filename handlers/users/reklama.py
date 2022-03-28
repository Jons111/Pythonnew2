from aiogram import types
from data.config import kanallar
from loader import dp,db,bot
from filters import Shaxsiy

# Echo bot
@dp.message_handler(Shaxsiy(),commands='reklama',chat_id=1892438581)
async def bot_echo(message: types.Message):
    userlar = db.select_foydalanuvchilar()
    for userr in userlar:
        tg_id = userr[4]
        await bot.send_message(chat_id=tg_id,text='Reklama')

    for kanal in kanallar:
        await bot.send_message(chat_id=kanal,text='Reklama yurildi bot orqali')