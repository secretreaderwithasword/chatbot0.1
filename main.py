import aiogram
import aiogram
import asyncio

from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from config import settings
bot = Bot(token=settings.TOKEN)

dp = Dispatcher()
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello world!")
async def main():
    await dp.start_polling(bot)
if __name__ == '__main__':
    #  acyncio.run(bot.send_message( 1433335116, "hello"))
     asyncio.run(main())
