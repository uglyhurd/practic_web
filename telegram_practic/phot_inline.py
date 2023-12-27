from aiogram import types,Bot,executor,Dispatcher
from aiogram.types import InlineQuery,InlineQueryResultArticle,InputContactMessageContent,InputTextMessageContent
import hashlib
import uuid
bot = Bot('6893180866:AAFIedT3x06EncwRD6zFBrBwh0ieNTYQJMA')
dp = Dispatcher(bot)


async def strt(_):
    print('Бот запущен')



@dp.message_handler(commands=['start'])
async def star(message:types.Message):
    await bot.send_message(message.chat.id, text='Привет')
    
    
    
@dp.inline_handler()
async def inlin(inline_query:types.InlineQuery):
    text = inline_query.query or 'Empty' #получение текста от пользоваетля
    input_content_bold = types.InputTextMessageContent(message_text=f'*{text}*',
                                                       parse_mode='markdown') #формируем контент ответного сообщения
    input_content_i = types.InputTextMessageContent(message_text=f'_{text}_',
                                                       parse_mode='markdown') #формируем контент ответного сообщения
    
    item_1 = types.InlineQueryResultArticle(
        id=str(uuid.uuid4()),
        input_message_content=input_content_bold,
        title='Bold',
        description=text,
        thumb_url='https://mykaleidoscope.ru/x/uploads/posts/2022-10/1666142103_28-mykaleidoscope-ru-p-dvoistvennoe-chuvstvo-krasivo-32.jpg'     
    )
    
    item_2 = types.InlineQueryResultArticle(
        id=str(uuid.uuid4()),
        input_message_content=input_content_i,
        title='It',
        description=text,
        thumb_url='https://polinka.top/uploads/posts/2023-06/1686002564_polinka-top-p-kartinki-obmanki-vkontakte-17.jpg' 
    
    )




    await bot.answer_inline_query(inline_query_id=inline_query.id,
                                  results=[item_1,item_2],
                                  cache_time=1)















if __name__=='__main__':
    executor.start_polling(dp,skip_updates=True,on_startup=strt)