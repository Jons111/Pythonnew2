from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Taomlar😂'),
            KeyboardButton(text='Ichimliklar')
        ],
        [
            KeyboardButton(text='Shirinliklar'),
            KeyboardButton(text='Salatlar')
        ],
        [
            KeyboardButton(text='Kontakt',request_contact=True),
            KeyboardButton(text='lokatsiya',request_location=True),
        ],
        [
            KeyboardButton(text='Murojat',),
        ]
    ],
    resize_keyboard=True
)