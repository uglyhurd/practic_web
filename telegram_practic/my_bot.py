from aiogram import executor,Bot,types,Dispatcher
from practic import TOKEN_API
from aiogram.types import KeyboardButton,ReplyKeyboardMarkup,ReplyKeyboardRemove
import random
bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

async def check_start(_):
    print('Бот Запущен')

ky1 = ReplyKeyboardMarkup(resize_keyboard=True)



b6 = KeyboardButton('❤️  ')
ky1.add(KeyboardButton('/discraption')).add(KeyboardButton('/sticker')).add(KeyboardButton('/photo')).add(KeyboardButton('/roll')).add(KeyboardButton('/location')).add(b6)
#ky2 = 


com = '''
/discraption - Описание бота
/roll - Рандомное число от 1 до 100
/sticker - Отправить рандомный стикер
/photo - Отправить рандомное фото
/location - Оправить локацию
/❤️ - отправиь стикер'''

@dp.message_handler(commands=['start'])
async def start_bot(message:types.Message):
    await bot.send_message(message.chat.id, text='Привет! Я бот Боб' + com,
                           reply_markup=ky1)


@dp.message_handler(commands=['discraption'])
async def start_bot(message:types.Message):
    await bot.send_message(message.chat.id, text='Я бот Боб, меня создали 5 минут назад')

@dp.message_handler(commands=['roll'])
async def start_bot(message:types.Message):
    await bot.send_message(message.chat.id, text=
                           random.randint(0,100))

@dp.message_handler(commands=['sticker'])
async def start_bot(message:types.Message):
    await bot.send_sticker(message.chat.id, sticker='CAACAgIAAxkBAAJkA2VsRWwJXh_u6LGPNI6PVJz_uX9OAAIEFwACz-rpS91lsZs3aeduMwQ')
    


@dp.message_handler(commands=['photo'])
async def start_bot(message:types.Message):
    await bot.send_photo(message.chat.id, photo='https://avatars.mds.yandex.net/i?id=c8fbc22d76a4897bf0837f0de1d062a30577438d-9857494-images-thumbs&n=13')
    
    
    
@dp.message_handler(commands=['location'])
async def start_bot(message:types.Message):
    await bot.send_location(message.chat.id,
                            latitude=45,
                            longitude=34)



@dp.message_handler()
async def start_bot(message:types.Message):
    if message.text == '❤️':
        await bot.send_sticker(message.chat.id, sticker='CAACAgIAAxkBAAJkBWVsSR6g9hWQo9hF6u8r31QlsI5BAALlFQACUVdJSMTr8mMEO59CMwQ')








if __name__=='__main__':
    executor.start_polling(dp, on_startup=check_start)