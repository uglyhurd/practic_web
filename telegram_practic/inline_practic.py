from aiogram import Dispatcher,executor,Bot,types
from aiogram.types import KeyboardButton,ReplyKeyboardMarkup,ReplyKeyboardRemove,InlineKeyboardButton,InlineKeyboardMarkup
from practic import TOKEN_API


bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

kb = ReplyKeyboardMarkup(resize_keyboard=True)
kb1 = KeyboardButton('/links')
ikb = InlineKeyboardMarkup(row_width=2)
b1 = InlineKeyboardButton('Z', url='https://sun9-52.userapi.com/impg/dVYOMyepA799WAxD4f7BDKB__ZcxzzGepOBZPw/Y70prqzeyvo.jpg?size=1280x720&quality=95&sign=de2f54c50725b71f76598a30a9641147&c_uniq_tag=GQ4ILaEKMoEnQjkKzw_i16fMmmrkscEqI4mQazmXFWo&type=album')
b2 = InlineKeyboardButton('O', url='https://pp.userapi.com/c628726/v628726399/1586f/lAGSIWADuqk.jpg')
b3 = InlineKeyboardButton('V', url='https://i.pinimg.com/564x/54/e6/09/54e60976dd68012310355dd4bdcc41fb.jpg')
ikb.add(b1).add(b2).add(b3)
kb.add(kb1)


async def start(_):
    print('бот запущен')


@dp.message_handler(commands=['start'])
async def start_game(message:types.Message):
    await bot.send_message(message.chat.id, text='начало бота. Привет! Меня зовут бот Боб.',
                           reply_markup=kb)




@dp.message_handler(commands=['links'])
async def start_game(message:types.Message):
    await bot.send_message(message.chat.id, text='начало бота. Привет! Меня зовут бот Боб.',
                           reply_markup=ikb)








































if __name__=='__main__':
    executor.start_polling(dp, on_startup=start)