from aiogram import executor,Bot,types,Dispatcher
from practic import TOKEN_API
from aiogram.types import KeyboardButton,ReplyKeyboardMarkup,ReplyKeyboardRemove
import random
bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

async def check_start(_):
    print('Бот Запущен')
    
    
    
@dp.message_handler()
async def hz(message:types.Message):
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#if __name__=='__main__':
    executor.start_polling(dp, on_startup=check_start)