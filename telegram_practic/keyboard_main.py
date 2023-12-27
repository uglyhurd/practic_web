from aiogram.types import KeyboardButton,ReplyKeyboardMarkup,ReplyKeyboardRemove,InlineKeyboardButton,InlineKeyboardMarkup
kb1 = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton('/help')
b2 = KeyboardButton('/roll')
b3 = KeyboardButton('/sticker')
b5 = KeyboardButton('/photo')
b4 = KeyboardButton('/practic')
b5 = KeyboardButton('/location')
b6 = KeyboardButton('раномное фото BMW')
kb1.add(b1).add(b2).add(b3).add(b4).add(b5).add(b6)


kb2 = ReplyKeyboardMarkup(resize_keyboard=True)
b12 = KeyboardButton('Главное Меню')
b22 = KeyboardButton('Рандомное фото')

kb2.insert(b12).add(b22)


ikb2 = InlineKeyboardMarkup(row_width=2)
ikb3 = InlineKeyboardButton('BMW', callback_data='bmw')
ikb4 = InlineKeyboardButton('One', callback_data='one')

ikb5 = InlineKeyboardButton('Love', callback_data='love')
ikb6 = InlineKeyboardButton('Следующее Фото', callback_data='next')
ikb7 = InlineKeyboardButton('Вернуться в Меню', callback_data='menu')
ikb2.add(ikb3,ikb4,ikb5,ikb6,ikb7)
