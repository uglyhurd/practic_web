from aiogram import Dispatcher,types,Bot,executor


bot = Bot('6893180866:AAFIedT3x06EncwRD6zFBrBwh0ieNTYQJMA')
dp = Dispatcher(bot)

@dp.message_handler()


    

async def echo(message:types.Message):
    if len(message.text.split())>=2:
        

        await message.answer(text=message.text)
    
if __name__=='__main__':
    executor.start_polling(dp)

    
