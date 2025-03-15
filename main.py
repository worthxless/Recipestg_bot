import asyncio
from aiogram import Bot, Dispatcher

from CONSTANTS import BOT_TOKEN
from app.database.database import init_db, engine
from app.handlers import router



async def main():
    init_db(engine)
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run((main()))
    except KeyboardInterrupt:
        print("СПИТ")