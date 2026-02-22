import os
import asyncio
import random
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart, Command
from aiohttp import web

TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Команды и ответы
tasks = ["Выпей стакан воды медленно. Считай глотки. 💧", "Сделай 10 приседаний. Ну же! 💪"]
praises = ["Неплохо. Ты сегодня мой фаворит. ✨"]
insults = ["Опять лень? Ты жалок. 👿"]

@dp.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer(f"РЕЖИМ БОГА активирован, {message.from_user.first_name}. 😈\n\nПиши /myid чтобы узнать свой номер.")

@dp.message(Command("myid"))
async def myid_cmd(message: types.Message):
    await message.answer(f"Твой ID: {message.from_user.id}")

@dp.message(Command("task"))
async def get_task(message: types.Message):
    await message.answer(random.choice(tasks))

@dp.message(Command("done"))
async def done_cmd(message: types.Message):
    await message.answer(random.choice(praises))

@dp.message(Command("lazy"))
async def lazy_cmd(message: types.Message):
    await message.answer(random.choice(insults))

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
    
