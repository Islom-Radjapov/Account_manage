import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

API_TOKEN = '6666656191:AAEtggl0TyzLyPeRggLlI25SDx1dD7izml4'
GROUP_CHAT_ID = -1002150404034

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Handle "hello" message
@dp.message_handler(lambda message: message.text.lower() == "5226667_daily loss_test test")
async def handle_hello(message: types.Message):
    print(123)
    await message.reply(555)

# Handle all other text messages and store the last message
@dp.message_handler(content_types=['text'])
async def handle_text(message: types.Message):
    global last_text_message
    last_text_message = message.text
    await message.reply(f"You said: {message.text}")

# Handle /last command to get the last text message
@dp.message_handler(commands=['last'])
async def get_last_message(message: types.Message):
    global last_text_message
    if last_text_message:
        await message.reply(f"The last message you sent was: {last_text_message}")
    else:
        await message.reply("No messages received yet.")

# Handle /sendtogroup command to send a message to the group
@dp.message_handler(commands=['sendtogroup'])
async def send_to_channel(message: types.Message):
    try:
        await bot.send_message(GROUP_CHAT_ID, "This is a message to the group.")
        await message.reply("Message sent to the group.")
    except Exception as e:
        await message.reply(f"Failed to send message to the group: {e}")

# Handle /sendtogroup command to send a message to the group

# Handle all other messages
@dp.message_handler()
async def echo(message: types.Message):
    await message.reply(message.text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

