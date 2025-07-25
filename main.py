
import os
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("ربات فانوس بزودی در دسترس شما قرار می‌گیرد.")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
