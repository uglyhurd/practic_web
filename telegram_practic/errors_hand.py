import asyncio
from aiogram.utils.exceptions import BotBlocked
from aiogram import executor,Bot,types,Dispatcher
from practic import TOKEN_API
from aiogram.types import KeyboardButton,ReplyKeyboardMarkup,ReplyKeyboardRemove
import random
bot = Bot('6434032409:AAEZG1YIMg7w_T5ad-ScMb7GYPazMcN5kac')
dp = Dispatcher(bot)

async def check_start(_):
    print('Бот Запущен')
  
  
   
@dp.message_handler(commands=['start'])
async def hz(message:types.Message):
    await asyncio.sleep(10)
    await message.answer('Привет')
    
    
    
@dp.errors_handler(exception=BotBlocked)
async def error(update:types.Update, exception:BotBlocked):
    print('Нельяз отпроавить сообщение')
    return True
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
if __name__=='__main__':
    executor.start_polling(dp, on_startup=check_start)