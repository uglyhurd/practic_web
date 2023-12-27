from aiogram import types,Dispatcher,Bot, executor
from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup, ReplyKeyboardRemove,ReplyKeyboardMarkup, KeyboardButton
from practic import TOKEN_API

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


async def start_bot(_):
    print('Бот запущен')


kb = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton('/help')
b2 = KeyboardButton('/vote')
#b3 = KeyboardButton('')
#b4 = KeyboardButton('')
kb.add(b1).add(b2)


ikb = InlineKeyboardMarkup(row_width=3)

ib1 = InlineKeyboardButton('Перейти', callback_data='не норм')
ib2 = InlineKeyboardButton('Жара', callback_data='норм')
ib3 = InlineKeyboardButton('LF', callback_data='топ')
ikb.add(ib1,ib2,ib3)
@dp.message_handler(commands=['start'])
async def start(message:types.Message):
    await bot.send_message(message.chat.id,text = 'Привет', reply_markup=kb)


@dp.message_handler(commands=['help'])
async def help(message:types.Message):
    await bot.send_message(message.chat.id, text='Привет! Я Боб!')




@dp.message_handler(commands=['vote'])
async def vote(message:types.Message):
    await bot.send_photo(message.chat.id, photo='https://www.lavanguardia.com/files/og_thumbnail/uploads/2023/01/20/63cabf196beff.jpeg',
                         caption='Тупа я')
    await bot.send_message(message.chat.id,text='Как дела',
                           reply_markup=ikb)



@dp.callback_query_handler()
async def callback(callback:types.CallbackQuery):
    if callback.data=='не норм':
         await callback.answer('очень жаль, пошел нахуй')
    else:
        callback.answer('Красавичк')




if __name__=='__main__':
    executor.start_polling(dp,on_startup=start_bot,skip_updates=True)