from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup
son = 5

viloyatlar_buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Tashkent",callback_data='viloyat1'),
            InlineKeyboardButton(text='Farg\'ona',callback_data='viloyat2')
        ],
[
            InlineKeyboardButton(text="Andijon",callback_data='viloyat3'),
            InlineKeyboardButton(text='Marg\'ilon',callback_data='viloyat4')
        ],
[
            InlineKeyboardButton(text="Buxoro",callback_data='viloyat5'),
            InlineKeyboardButton(text='Samarqand',callback_data='viloyat6')
        ],
[
            InlineKeyboardButton(text="Ulashish",switch_inline_query=''),
            InlineKeyboardButton(text='Hamkorlarimiz',url='https://t.me/UstozShogird')
        ]
    ]
)