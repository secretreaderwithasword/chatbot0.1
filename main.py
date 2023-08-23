import asyncio
from aiogram import Bot, Dispatcher
from hendlers import start, any_text, stickers, hello, how
from config import settings


async def main():
    bot = Bot(token=settings.TOKEN)
    dp = Dispatcher()
    dp.include_router(start.router)
    dp.include_router(stickers.router)
    dp.include_router(how.router)
    dp.include_router(hello.router)
    dp.include_router(any_text.router)


    await dp.start_polling(bot)
if __name__ == '__main__':
     asyncio.run(main())
