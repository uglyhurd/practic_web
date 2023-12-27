#from aiogram import Bot, types, Dispatcher, executor
'''from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
'''

TOKEN_API = '6893180866:AAFIedT3x06EncwRD6zFBrBwh0ieNTYQJMA'

'''bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(text=message.text)

if __name__ == '__main__':
    executor.start_polling(dp)'''
 
'''from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

#from config import TOKEN

TOKEN = '6893180866:AAFIedT3x06EncwRD6zFBrBwh0ieNTYQJMA'
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!\nНапиши мне что-нибудь!")


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Напиши мне что-нибудь, и я отпрпавлю этот текст тебе в ответ!")


@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)


if __name__ == '__main__':
    executor.start_polling(dp)'''