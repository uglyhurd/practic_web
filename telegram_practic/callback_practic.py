from aiogram import executor,Bot,types,Dispatcher
from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup,KeyboardButton,ReplyKeyboardMarkup,ReplyKeyboardRemove
import random
bot = Bot('6434032409:AAEZG1YIMg7w_T5ad-ScMb7GYPazMcN5kac')
dp=Dispatcher(bot)


async def start_pol(_):
    print('Бот запущен')

number = 0  
def get_inline():
    ikb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton('Incrise', callback_data= 'btn_im' ), InlineKeyboardButton('Decrease', callback_data='btn_decr')], [InlineKeyboardButton('Random', callback_data='btn_random')] 
    ])

    return ikb


@dp.message_handler(commands=['start'])
async def start(message:types.Message): 
    await message.answer(f'Текущее число:{number}',
                         reply_markup=get_inline())


@dp.callback_query_handler(lambda callback_query: callback_query.data.startswith('btn'))
async def tap(callback:types.CallbackQuery):
    global number 
    if callback.data=='btn_decr':
        number+=1
        await callback.message.edit_text(f'Текущее число:{number}',
                                         reply_markup=get_inline())
    elif callback.data=='btn_im':
        number-=1
        await callback.message.edit_text(f'Текущее число:{number}',
                                         reply_markup=get_inline())
    elif callback.data =='btn_random':
        number = random.randint(1,100)
        await callback.message.edit_text(f'Текущее число:{number}',
                                         reply_markup=get_inline())
        
    



















if __name__=='__main__':
    executor.start_polling(dp,on_startup= start_pol, skip_updates=True)
    