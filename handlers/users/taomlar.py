from aiogram import types
from aiogram.types import InputFile

from loader import dp,bot
from keyboards.default.taomlar_buttons import taomlar

# Echo bot
@dp.message_handler(text='Taomlar😂')
async def bot_echo(message: types.Message):
    await message.answer(text='Quyidagi taomlardan birini tanlang',reply_markup = taomlar)

@dp.message_handler(text='Osh')
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzil = 'AgACAgIAAxkBAAIBfmIoQ7Vn7hDEN0jMXxO5B1vrYfLJAAIeuTEblVpBSWarIHpQ93DKAQADAgADeAADIwQ'
    await bot.send_photo(chat_id=user_id,photo=rasm_manzil,caption='Taom narxi : 17000 \n'
                                                                   'Manzil 🌕: Toshkent')