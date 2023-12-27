from aiogram import types,Bot,Dispatcher,executor
from practic import TOKEN_API







elp = '''/help - список команд
/start-начало'''


bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


@dp.message_handler(commands=['help'])
async def test(message:types.Message):
    await message.reply(text=elp)
    
    
@dp.message_handler(commands=['start'])
async def test(message:types.Message):
    await message.answer(text='добро пожаловать')
    await message.delete()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
if __name__=='__main__':
    executor.start_polling(dp)