from aiogram import Dispatcher,types,Bot,executor
from practic import TOKEN_API

bot = Bot(TOKEN_API)

dp = Dispatcher(bot)


async def startup(_):
    print('Бот Был запущен')


@dp.message_handler(commands=['start'])
async def command(message:types.Message):
    await message.answer('<em>привет</em>   <b>че делаешь</b>',parse_mode='HTML')
@dp.message_handler(commands=['emoji'])
async def command(message:types.Message):
    await message.reply('<em>привет</em>   <b>че делаешь</b>',parse_mode='HTML')
    await bot.send_sticker(message.from_user.id,sticker='CAACAgIAAxkBAAJj5WVrMEmjzWZ7pbxxD1XXXdM3bHwkAAKVEgACEmDpS07JyM81NeDAMwQ')
    await message.delete()

@dp.message_handler()
async def command(message:types.Message):
    await message.answer(message.text+'💘')
    
    



if __name__=='__main__':
    executor.start_polling(dp,on_startup=startup)
    
    
#on_startup выводит в консоль что либо и дает знать, что бот работает четко

#parse_mod служит как изменение щрифта или вида текста