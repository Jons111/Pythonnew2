from aiogram import types
from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup
from data.config import kanallar
from utils import azolik_tekshirish
from loader import bot



class Asosiy_checking(BaseMiddleware):
    async def on_pre_process_update(self,xabar:types.Update,data:dict):
        if xabar.message:
            user_id = xabar.message.from_user.id
        elif xabar.callback_query:
            user_id = xabar.callback_query.from_user.id
        else:
            return
        matn = 'Quyidagi kanalga azo boling\n'

        daslabki_holati = True
        royxat = []
        for k in kanallar:
            holat = await azolik_tekshirish.tekshirish(user_id=user_id,kanal_link=k)
            daslabki_holati *= holat

            kanal = await bot.get_chat(k)

            if not holat:
                link = await kanal.export_invite_link()

                royxat.append(InlineKeyboardButton(text=f'{kanal.title}',url=f'{link}'))


        royxat.append(InlineKeyboardButton(text=f'Tekshirish',callback_data='salom'))
                    # (f"👉 <a href='{link}'>{kanal.title}</a>\n")
        if not daslabki_holati:
            await xabar.message.answer(matn,disable_web_page_preview=True,reply_markup=InlineKeyboardMarkup(
                inline_keyboard=[royxat]
            ))
            raise CancelHandler()