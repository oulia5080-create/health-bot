import os
import asyncio
import random
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart, Command
from aiohttp import web

TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher()

tasks = [
    "Съешь мандаринку! 🍊",
    "Посмотри в окно и найди 3 птицы. 🐦",
    "Сделай 10 приседаний. 💪",
    "Выпей стакан воды. 💧"
]

@dp.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer("Бот здоровья на связи! Напиши /task, чтобы получить задание.")

@dp.message(Command("task"))
async def get_task(message: types.Message):
    task = random.choice(tasks)
    await message.answer(task)

async def handle(request):
    return web.Response(text="Bot is running")

async def main():
    app = web.Application()
    app.router.add_get("/", handle)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', 10000)
    asyncio.create_task(site.start())
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
    
