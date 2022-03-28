from aiogram import types
from aiogram.types import CallbackQuery
from keyboards.default.Menu_tugmalar import menu
from loader import dp


# Echo bot
@dp.callback_query_handler(text='viloyat1')
async def bot_echo(query: CallbackQuery):
        await query.message.answer(text='Toshkent shaxridagi filiyalga hush kelibsiz',reply_markup=menu)
