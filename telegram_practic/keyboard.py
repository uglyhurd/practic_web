from aiogram import Dispatcher,types,executor,Bot
from practic import TOKEN_API
from aiogram.types import ReplyKeyboardMarkup,KeyboardButton,ReplyKeyboardRemove    

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

async def start(_):
    print('Бот запущен')

'''kb = ReplyKeyboardMarkup(resize_keyboard=True)
b1= KeyboardButton('/help')
b2 = KeyboardButton('/photo')
b3 = KeyboardButton('/description')

kb.add(b1).insert(b2).add(b3)'''



commands= '''<b>/help</b> - <em>список команд</em>
<b>/start</b> - <em>Старт бота</em>
<b>/description</b> - <em>Описание</em>
<b>/photo</b> - <em>Отправка фото</em>
'''




@dp.message_handler(commands=['start'])
async def help_commands(message:types.Message):
    await bot.send_message(message.chat.id,
                           text=commands,
                           parse_mode='HTML')



@dp.message_handler(commands=['help'])
async def start_commands(message:types.Message):
    await bot.send_message(message.chat.id,
                           text='Добро пожаловать в Бот',
                           parse_mode='HTML') 
                           #reply_markup=ReplyKeyboardRemove())

@dp.message_handler(commands=['description'])
async def discription_commands(message:types.Message):
    await bot.send_message(message.chat.id,
                           text='Я бот Боб',
                           parse_mode='HTML')


@dp.message_handler(commands=['photo'])
async def photo_commands(message:types.Message):
    await bot.send_photo(message.chat.id,
                        photo='https://avatars.mds.yandex.net/i?id=0a15435c7a57ca4dd29de9c114e30c73109d1173-10310451-images-thumbs&n=13')














if __name__=='__main__':
    executor.start_polling(dp,skip_updates=True,on_startup=start )