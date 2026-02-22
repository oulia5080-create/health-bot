import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

TOKEN = "7968560155:AAEm877vCj-M3X_N6I8S8n8V8Wz80v7O_mY"
ADMIN_ID = 1923651743

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("😈 РЕЖИМ БОГА активирован!\nБот-надзиратель на связи.")
    if message.from_user.id != ADMIN_ID:
        await bot.send_message(ADMIN_ID, f"📈 Новая жертва: {message.from_user.first_name}")

@dp.message(Command("admin"))
async def admin(message: types.Message):
    await message.answer("Слушаю, Хозяйка. Я в сети! 💎")

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
    
