import asyncio
from aiogram import Bot, Dispatcher

from app.handlers import router


print("Сука ты")

async def main():
    bot = Bot(token='7554317573:AAFCXn2wtoExmUb46OZjwDa8gbirtPAMZFI')
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run((main()))
    except KeyboardInterrupt:
        print("СПИТ")