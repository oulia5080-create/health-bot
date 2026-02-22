import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiohttp import web

# Твой токен
TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer("Бот здоровья на связи! Теперь я не отключусь. 🚀")

# Костыль для Render, чтобы он не выключал бота
async def handle(request):
    return web.Response(text="Bot is running!")

async def main():
    # Запускаем веб-сервер для "галочки" Render
    app = web.Application()
    app.router.add_get("/", handle)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', os.getenv("PORT", "10000"))
    
    asyncio.create_task(site.start())
    
    # Запускаем бота
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
