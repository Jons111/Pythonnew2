from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.inline.viloyatlar_inline import viloyatlar_buttons
from loader import dp, db
from keyboards.default.Menu_tugmalar import menu
from filters import Shaxsiy
@dp.message_handler(Shaxsiy(),CommandStart())
async def bot_start(message: types.Message):
    name = message.from_user.first_name
    fam = message.from_user.last_name
    username = message.from_user.username
    tg_idd = message.from_user.id

    db.user_qoshish(ism=name,fam=fam,username=username,tg_id = tg_idd)

    await message.answer(f"Salom, {message.from_user.full_name} botga hush kelibsiz!",reply_markup=viloyatlar_buttons)

@dp.message_handler(text = 'Menu')
async def bot_start(message: types.Message):
    await message.answer(text='Bosh menuga hush kelibsiz',reply_markup=menu)