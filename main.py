import os
import asyncio
import random
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart, Command
from aiohttp import web

TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = 1923651743  # Твой ID теперь здесь
bot = Bot(token=TOKEN)
dp = Dispatcher()

# База фраз
tasks = [
    "Выпей стакан воды медленно. Считай глотки. 💧",
    "Сделай 10 приседаний. Ну же! 💪",
    "Пять минут тишины. Убери телефон, просто сиди. 🧘‍♀️",
    "Разминка шеи. 10 раз влево, 10 раз вправо. Живо!"
]
praises = ["Неплохо. Ты сегодня мой фаворит. ✨", "Хвалю. Можешь, когда хочешь! 🔥"]
insults = ["Опять лень? Ты жалок. 👿", "Дима бы уже сделал, а ты? Слабак. 🙄"]

@dp.message(CommandStart())
async def start_cmd(message: types.Message):
    user_name = message.from_user.first_name
    # Приветствие пользователя
    await message.answer(f"😈 РЕЖИМ БОГА активирован, {user_name}!\n\nЭто бот-надзиратель для очистки мозгов. Здесь нет жалости, только дисциплина.\n\nКоманды:\n/task — получить задание\n/done — отчитаться")
    
    # Уведомление тебе (Админу)
    if message.from_user.id != ADMIN_ID:
        await bot.send_message(ADMIN_ID, f"📈 **Хозяйка, новая жертва в сети!**\nИмя: {user_name}\nID: {message.from_user.id}\nНачинаю обработку... 😈")

@dp.message(Command("admin"))
async def admin_check(message: types.Message):
    if message.from_user.id == ADMIN_ID:
        await message.answer("Слушаю, Хозяйка. Система работает исправно. Все под контролем. 💎")
    else:
        await message.answer("У тебя нет прав доступа к божественным настройкам. Брысь! ⚡️")

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
    
