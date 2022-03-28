from aiogram import types
from googletrans import Translator
from loader import dp

tarjimon = Translator()

# Echo bot
@dp.message_handler()
async def bot_echo(message: types.Message):
    til = tarjimon.detect(message.text).lang
    matn = message.text
    kim = message.from_user.username

    print(f'{kim} ushbu foydalanuvchi {matn}')
    if til =='uz':
        tarjima_qilish =tarjimon.translate(text=matn,dest='en',src='uz').text
        await message.answer(text=f'{tarjima_qilish}')
    elif til=='ru':
        tarjima_qilish = tarjimon.translate(text=matn, dest='uz', src='ru').text
        await message.answer(text=f'{tarjima_qilish}')