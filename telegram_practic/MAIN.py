from aiogram import Bot,Dispatcher,executor,types
from aiogram.types import KeyboardButton,ReplyKeyboardMarkup,ReplyKeyboardRemove,InlineKeyboardButton,InlineKeyboardMarkup
import random
from keyboard_main import *
from aiogram.dispatcher.filters import Text
bot = Bot('6681778748:AAFwpfS-KHEax5rkix7dA7J93-BGe4Vh8tI')
dp = Dispatcher(bot)

async def start_bot(_):
    print('Бот запущен')

async def send_photo(message:types.Message):
    c = random.choice(list(dict_photos.keys()))
    await bot.send_photo(message.chat.id,
                         photo=c,
                         caption=dict_photos[c],
                         reply_markup=ikb2)


flag = False


'''kb1 = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton('/help')
b2 = KeyboardButton('/roll')
b3 = KeyboardButton('/sticker')
b5 = KeyboardButton('/photo')
b4 = KeyboardButton('/practic')
kb1.add(b1).add(b2).add(b3).add(b4).add(b5)'''

ikb1 = InlineKeyboardMarkup(row_width=3)
ik1 = InlineKeyboardButton('B', callback_data='ha')
ik2 = InlineKeyboardButton('M',callback_data='haa')
ik3 = InlineKeyboardButton('W', callback_data='hha')
ikb1.add(ik1,ik2,ik3)   


photos = ['https://i.pinimg.com/564x/85/59/40/85594085fbed95627161b87f1c81239c.jpg','https://i.pinimg.com/736x/6f/30/8e/6f308e1f28b1fd11073025e558c2e90e.jpg','https://i.pinimg.com/564x/82/ff/65/82ff657b095b46da9fdeaff312b00bbe.jpg']

dict_photos=dict(zip(photos, ['Я','Люблю','BMW']))

c = random.choice(list(dict_photos.keys()))





@dp.message_handler(commands=['start'])
async def start(message:types.Message):
    await bot.send_message(message.chat.id,text='Привет! Я бот! BMW !')
    await bot.send_photo(message.chat.id,photo='https://i.pinimg.com/564x/85/4f/8d/854f8d21f2a238ea7cd8c03e9f77aade.jpg',
                         caption='Настанет час мечты'+'❤️',
                         reply_markup=kb1)

@dp.message_handler(commands=['help'])
async def start(message:types.Message):
    await bot.send_message(message.chat.id,text='Я бот эстетики БМВ!')
    await bot.send_photo(message.chat.id,photo='https://i.pinimg.com/564x/8d/05/2c/8d052cd474e29f9d7c07bd908f117d57.jpg',
                         caption='Настанет час мечты'+'❤️')


@dp.message_handler(commands=['roll'])
async def start(message:types.Message):
    a = random.randint(0,100)
    await bot.send_message(message.chat.id,text=a)
    if a <=50:
        await bot.send_photo(message.chat.id,photo='https://i.pinimg.com/564x/45/56/89/4556893427e78159f90648dc1e00c9f7.jpg',
                         caption='Настанет час мечты'+'❤️')
    else:
        await bot.send_photo(message.chat.id,photo='https://i.pinimg.com/564x/4c/e9/31/4ce9316020b2cceaed00955bac836c02.jpg',
                         caption='Настанет час мечты'+'❤️')


@dp.message_handler(commands=['sticker'])
async def start(message:types.Message):
    await bot.send_sticker(message.chat.id,sticker='CAACAgIAAxkBAAJlxGVzg1ttQReZ45PQrQqBMht7sfioAAJaFgACo3DBS6SgvSZYEIJnMwQ')
   
@dp.message_handler(commands=['location'])
async def loc(message:types.Message):
    await bot.send_location(message.chat.id,
                            longitude=random.randint(1,99),
                            latitude=random.randint(1,99))

@dp.message_handler(commands=['photo'])
async def start(message:types.Message):
    await bot.send_photo(message.chat.id,photo='https://i.pinimg.com/564x/48/ff/73/48ff7341416ca5ee22f9816e89450149.jpg',
                         caption='Настанет час мечты'+'❤️')
    await bot.send_photo(message.chat.id,photo='https://i.pinimg.com/564x/da/7c/25/da7c255ff55c6562ca48e34dba0000c2.jpg',
                         caption='Настанет час мечты'+'❤️')



@dp.message_handler(commands=['practic'])
async def start(message:types.Message):
    await bot.send_message(message.chat.id,text='ты сможешь бро!'+'❤️')
    
@dp.message_handler(Text(equals='раномное фото BMW'))
async def bmw(message:types.Message):
    await message.answer(text='*переход к меню BMW*',
                         reply_markup=kb2)

@dp.message_handler(Text(equals='Главное Меню'))
async def qq(message:types.Message):
    await message.answer(text='Добро пожаловать в главное меню!',
                         reply_markup=kb1)


@dp.message_handler(Text(equals='Рандомное фото'))
async def random_photo(message:types.Message):
    await send_photo(message)




@dp.callback_query_handler()
async def start(callback:types.CallbackQuery):
    global c
    
    if callback.data=='bmw':
        
            
        await callback.message.answer('Настанет')
        await callback.answer('Only')
            
        
            
    elif callback.data=='one':
        await callback.message.answer('Час')
        await callback.answer('Hard')
    elif callback.data=='love':
        await callback.message.answer('Мечты')
        await callback.answer('Work')
    #elif callback.data=='next':
    elif callback.data=='next':
        c = random.choice(list(filter(lambda x:x!=c,list(dict_photos.keys()))))
        await callback.message.edit_media(types.InputMedia(media=c,
                                                            type='photo',
                                                            caption=dict_photos[c]),
                                                        reply_markup=ikb2)
    elif callback.data=='menu':
        

        await callback.message.answer(text ='Возращение в Меню',
                             reply_markup=kb1)
    
         
    #await bot.send_photo(message.chat.id,photo='https://i.pinimg.com/564x/c9/bd/c8/c9bdc820ba8dbc4a4b2eaada3edfbf1c.jpg')




if __name__=='__main__':
    executor.start_polling(dp, on_startup=start_bot,skip_updates=False  )