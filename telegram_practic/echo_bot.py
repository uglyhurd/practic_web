import hashlib


from aiogram import Dispatcher,types,executor,Bot
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

from aiogram.types import InlineQueryResultArticle,InputTextMessageContent 


maket = CallbackData('ikb','action')
bot = Bot('6893180866:AAFIedT3x06EncwRD6zFBrBwh0ieNTYQJMA')
dp = Dispatcher(bot)


ikb = InlineKeyboardMarkup(row_width=2)
b1 = InlineKeyboardButton('Хорошо!', callback_data=maket.new('good'))
b2 = InlineKeyboardButton('Плохо(', callback_data=maket.new('bad'))
ikb.add(b1).add(b2)



async def start_p(_):
    print('Бот запущен')





@dp.message_handler(commands=['start'])
async def start(message:types.Message):
    await message.answer(text='Привет! Как дела?',
                           reply_markup=ikb)


@dp.callback_query_handler(maket.filter(action='bad'))
async def callback(callback:types.CallbackQuery):
   
    await callback.answer('Плохо.')


@dp.callback_query_handler(maket.filter(action='good'))
async def callback1(callback:types.CallbackQuery):
   
    await callback.answer('Отлично.')









@dp.inline_handler()
async def inline(inline_query:types.InlineQuery):
    text = inline_query.query or 'Echo' #получение текста от пользоваетля
    input_content = InputTextMessageContent(text) #формируем контент ответного сообщения
    result_id: str = hashlib.md5(text.encode()).hexdigest() #сделали уникальный id
    
    if text=='photo':
        input_content = InputTextMessageContent('This is photo')
    
    item = InlineQueryResultArticle(
        input_message_content=input_content,
        id=result_id,
        title=text,
    )
    
    
    await bot.answer_inline_query(inline_query_id=inline_query.id,
                                  results=[item]
                                  )
    
    
                                






if __name__=='__main__':
    executor.start_polling(dp,on_startup=start_p, skip_updates=True )