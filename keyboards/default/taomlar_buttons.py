from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

taomlar = ReplyKeyboardMarkup(

    keyboard=[
        [
            KeyboardButton(text='Osh'),

        ],
        [
            KeyboardButton(text='Lag\'mon')
        ],
        [
            KeyboardButton(text='Kabob')
        ],
        [
            KeyboardButton(text='Pitsa')
        ],
        [
            KeyboardButton(text='Ortga'),
            KeyboardButton(text='Menu'),
        ]
    ]
)