import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

API_TOKEN = '7382465275:AAHMwFNC8mQWrYX0Bgkm8b9krQ3NLis-xPA'
GROUP_CHAT_ID = -1002197406833

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Handle "hello" message
@dp.message_handler(lambda message: message.text.lower() == "5226667_daily loss_test test")
async def handle_hello(message: types.Message):
    print(123)
    a = bot.get_chat(529408795)
    await message.reply(a)


# Handle /sendtogroup command to send a message to the group

# Handle all other messages
@dp.message_handler()
async def echo(message: types.Message):
    await message.reply(message.text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)