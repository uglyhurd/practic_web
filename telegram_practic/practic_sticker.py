from aiogram import types,Dispatcher,Bot,executor
from practic import TOKEN_API
import random
bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

HELP= '''
<i>/фото</i>
<i>/help</i> - <b>Помощь</b>
<i>/гифка</i> - <b>Показывает </b>
<i>/status</i> - <b>Показывает статус</b>
<i>/location</i> - <b>Показывает локацию</b>'''

async def start(_):
    print('Бот запущен')


'''@dp.message_handler(commands=['give'])
async def practic(message:types.Message):
    if '❤️' in message.text:
        await message.answer('Смотри какой крутой котик'+'🖤')
    else:
        await message.answer('Смотри какой крутой котик'+'💖')
    await bot.send_sticker(message.from_user.id, sticker='CAACAgIAAxkBAAJj5WVrMEmjzWZ7pbxxD1XXXdM3bHwkAAKVEgACEmDpS07JyM81NeDAMwQ')
@dp.message_handler()
async def practic(message:types.Message):
    if message.text =='❤️':
        await message.answer('🖤')'''
   
'''@dp.message_handler(commands=['help'])
async def rename(message:types.Message):
    
    await message.reply(text=com,parse_mode='HTML')
    '''
    
@dp.message_handler(commands=['need_help'])
async def send_sticker_id(message:types.Message):
    '''await message.answer(message.sticker.file_id)
    await bot.send_sticker(message.chat.id, sticker='CAACAgIAAxkBAAIDL2VrSMORKfLCkz57-aA14k11m0iAAAKcEgACi7PpS8OjsrKAMWZJMwQ')'''
    '''await bot.send_message(chat_id=message.chat.id,
                           text='hello world')'''
    await bot.send_message(chat_id=message.chat.id,
                           text=HELP,parse_mode='HTML')



@dp.message_handler(commands=['фото'])
async def send_image(message:types.Message):
    await bot.send_photo(chat_id=message.chat.id,
                         photo='https://avatars.mds.yandex.net/i?id=5abdf7bf0ffbec07ea73a22db05307d0b9ed23cb-6946731-images-thumbs&n=13')


@dp.message_handler(commands=['гифка'])
async def send_sticker_id(message:types.Message):
    await bot.send_sticker(message.chat.id, sticker='CAACAgIAAxkBAAJj7GVreCBzOI4Ik3uB3JQqQrvcJ8lIAAI7AAPFQw0oFaFtRLRGoS0zBA')


@dp.message_handler(commands=['help'])
async def send_sticker_id(message:types.Message):
    await message.answer('Привет, я бот Боб.')
    

@dp.message_handler(commands=['status'])
async def send_sticker_id(message:types.Message):
    await message.answer(random.randint(1,10))
      

@dp.message_handler(commands=['location'])
async def location(message:types.Message):
    await bot.send_location(chat_id=message.chat.id,
                            longitude=34,
                            latitude=74)











if __name__=='__main__':
    executor.start_polling(dp, on_startup=start)