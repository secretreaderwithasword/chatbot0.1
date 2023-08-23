import asyncio
from aiogram import Bot, Dispatcher
from config import settings
bot = Bot(token=settings.TOKEN)

dp = Dispatcher()
async def main():
    from hendlers import dp
    await dp.start_polling(bot)
if __name__ == '__main__':
     asyncio.run(main())
