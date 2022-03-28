from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

tasdiq = ReplyKeyboardMarkup(

    keyboard=[
        [
            KeyboardButton(text='Tasdiqlash'),
            KeyboardButton(text='Bekor qilish')
        ]
    ],
    resize_keyboard=True
)