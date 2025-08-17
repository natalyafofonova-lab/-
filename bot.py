import os
from aiogram import Bot, Dispatcher, executor, types

TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

users = {}
referrals = {}

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    user_id = message.from_user.id
    args = message.get_args()

    if user_id not in users:
        users[user_id] = 0
        if args.isdigit():
            ref_id = int(args)
            if ref_id != user_id:
                users[ref_id] = users.get(ref_id, 0) + 1

    link = f"https://t.me/{(await bot.get_me()).username}?start={user_id}"
    await message.answer(
        f"Привет 👋\n\nТвоя ссылка для приглашений:\n{link}\n\n⭐ У тебя {users[user_id]} звёзд"
    )

@dp.message_handler(commands=['stars'])
async def stars(message: types.Message):
    user_id = message.from_user.id
    stars = users.get(user_id, 0)
    await message.answer(f"У тебя ⭐ {stars} звёзд")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
