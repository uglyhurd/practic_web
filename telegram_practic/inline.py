from aiogram import executor,Bot,types,Dispatcher
from practic import TOKEN_API
from aiogram.types import KeyboardButton,ReplyKeyboardMarkup,ReplyKeyboardRemove, InlineKeyboardButton,InlineKeyboardMarkup

import random
bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

ikb = InlineKeyboardMarkup(row_width=2)
ib1 = InlineKeyboardButton('Перейти', url='https://avatars.mds.yandex.net/i?id=a5c3629cc7d908a7c352bdb9a8bcd9b4c5f6b31a-11387523-images-thumbs&n=13')
ib2 = InlineKeyboardButton('Жара', url='https://avatars.mds.yandex.net/i?id=01d0a54a990500962b7aba46e4ef62bb68aab3b7-10702734-images-thumbs&n=13')
ikb.add(ib1,ib2)

async def check_start(_):
    print('Бот Запущен')
    
    
    
@dp.message_handler(commands=['start'])
async def hz(message:types.Message):
    await bot.send_message(message.chat.id, text='Привет',
                           reply_markup=ikb)
    
    
    
    
    
    
    
    
    
if __name__=='__main__':
    executor.start_polling(dp, on_startup=check_start)