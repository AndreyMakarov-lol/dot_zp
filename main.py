import asyncio
from pydantic_settings import BaseSettings
from pydantic import Field
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command


# работа с переменной окружения
class AppSettings(BaseSettings):
    token: str

    class Config:
        env_file = ".env"


settings = AppSettings()

# инициализируем бота

bot = Bot(token=settings.token)
dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer('Здорова')


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
