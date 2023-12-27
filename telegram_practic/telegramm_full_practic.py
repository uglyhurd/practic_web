from aiogram import Bot,types,Dispatcher,executor
from practic import TOKEN_API
import random
import string

names = 0
bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


'''@dp.message_handler()
async def otvet(message:types.Message):
    
    await message.reply(random.choice(string.ascii_letters))       
'''#выводит рандомные буквы из алфовита


'''@dp.message_handler(commands=['help'])
async def biography(message:types.Message):
    await message.reply(text=names)


@dp.message_handler(commands=['description'])
async def biography(message:types.Message):
    await message.reply(random.choice(string.ascii_letters)) 
    await message.reply(text='Привет, я бот, меня недавно создали, мне 1 день.Удачи!')
    await message.delete()

'''

'''@dp.message_handler(commands=['count'])
async def value(message:types.Message):
    global names
    await message.answer(f'Значение:{names}')
    names+=1
    '''#счетчик




@dp.message_handler()
async def thing (message:types.Message):
    if '0'in message.text:
        await message.answer(text='Yes')
    else:
        await message.answer(text='No')













    






if __name__=='__main__':
    executor.start_polling(dp)