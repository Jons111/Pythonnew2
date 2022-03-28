from aiogram import types
from aiogram.types import ContentType
from filters import Shaxsiy
from loader import dp


# Echo bot
@dp.message_handler(content_types=ContentType.DOCUMENT)
async def bot_echo(message: types.Message):
    await  message.document.download()
    await message.answer(text='botga dacument yuborildi')

@dp.message_handler(content_types=ContentType.STICKER)
async def bot_echo(message: types.Message):
    await message.sticker.download()
    await message.answer(text='Botga sticker yuborildi')

@dp.message_handler(content_types=ContentType.VIDEO)
async def bot_echo(message: types.Message):
    await message.video.download()
    await message.answer(text='Botga video yuborildi')

@dp.message_handler(Shaxsiy(),content_types=ContentType.PHOTO)
async def bot_echo(message: types.Message):
    rasm_id = message.photo[-1].file_id
    await message.answer(text=f'Botga rasm yuborildi shu idda {rasm_id}')