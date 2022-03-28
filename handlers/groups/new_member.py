from aiogram import types
from aiogram.types import ContentType

from filters import Guruh
from loader import dp, bot


# Echo bot
@dp.message_handler(Guruh(),content_types=ContentType.NEW_CHAT_MEMBERS)
async def bot_echo(message: types.Message):
    ism = message.new_chat_members[0].username
    s = message.message_id
    await bot.delete_message(chat_id='@salom23443',message_id=s)

    await message.answer(text=f'guruhga hush kelibsiz {ism}')


@dp.message_handler(Guruh(),content_types=ContentType.PHOTO)
async def bot_echo(message: types.Message):
    ism = message.from_user.first_name
    rasm_id = message.photo[-1].file_id
    u = message.from_user

    await message.reply(text=f'rasm yubormang {ism}')
    await bot.kick_chat_member(chat_id='@salom23443',user_id=u,)

@dp.message_handler(Guruh(),content_types=ContentType.LEFT_CHAT_MEMBER)
async def bot_echo(message: types.Message):
    ism = message.left_chat_member.first_name
    xabar_id = message.message_id
    await bot.delete_message(chat_id='@salom23443',message_id=xabar_id)
    await message.answer(text=f'guruhni tark etdi {ism}')