from aiogram import executor,Bot,types,Dispatcher
from practic import TOKEN_API
from aiogram.types import KeyboardButton,ReplyKeyboardMarkup,ReplyKeyboardRemove
import random
bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

async def check_start(_):
    print('Бот Запущен')

ky1 = ReplyKeyboardMarkup(resize_keyboard=True)



ky1.add(KeyboardButton('/help')).add(KeyboardButton('/orange')).add(KeyboardButton('/location'))
#ky2 = 


com = '''
/help - Описание бота
/orange - Отправить апельсин
/location - рандомное местоположение
'''


@dp.message_handler(commands=['start'])
async def start_bot(message:types.Message):
    await bot.send_message(message.chat.id, text='Привет! Я бот Боб' + com,
                           reply_markup=ky1)

@dp.message_handler(commands=['help'])
async def start_bot(message:types.Message):
    await bot.send_message(message.chat.id, text='Привет! Я бот Боб')

@dp.message_handler(commands=['orange'])
async def start_bot(message:types.Message):
    await bot.send_photo(message.chat.id, photo='https://avatars.mds.yandex.net/i?id=c4b7d433f7f59e9813a4ea04bdb7e1dd7f3a1276-10766948-images-thumbs&n=13')
    
    
@dp.message_handler(commands=['location'])
async def start_bot(message:types.Message):
    await bot.send_location(message.chat.id, longitude=random.randint(1,99), latitude=random.randint(1,99))

if __name__=='__main__':
    executor.start_polling(dp, on_startup=check_start)