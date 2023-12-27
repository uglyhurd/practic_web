from aiogram import executor,Bot,Dispatcher,types
from aiogram.types import InlineQueryResultArticle,InlineQueryResult,InputTextMessageContent
import hashlib

bot = Bot('6893180866:AAFIedT3x06EncwRD6zFBrBwh0ieNTYQJMA')
dp = Dispatcher(bot)

user_data = ''


async def strt(_):
    print('Бот запущен')
    
@dp.message_handler(commands=['start'])
async def cmd_start(message:types.Message):
    await message.answer('Введите число!')
    
    
    
    
    
@dp.message_handler()
async def text_handler(message:types.Message):
    global user_data
    user_data = message.text
    await message.reply(text='Ваши данные сохранены')


@dp.inline_handler()
async def inline_hand(inline_query:types.InlineQuery):
    
    text = inline_query.query or 'Empty'
    result_id = hashlib.md5(text.encode()).hexdigest()
    input_content = InputTextMessageContent(f'<b>{text}</b> - {user_data}',
                                            parse_mode='HTML')
    
    
    item = InlineQueryResultArticle(
        input_message_content= input_content,
        id=result_id,
        title= 'Echo,Bot!',
        description='Привет! я эхо бот'
    )
    
    await bot.answer_inline_query(results=[item],
                                  inline_query_id=inline_query.id,
                                  cache_time=1)
    






















if __name__=='__main__':
    executor.start_polling(dp, on_startup=strt, skip_updates=True)