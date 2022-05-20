import logging
from aiogram import Bot, Dispatcher, executor, types

from bsbot_config import API_TOKEN


bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

@dp.message_handler(commands="Hello")
async def cmd_test1(message: types.Message):
    await message.reply("Hello! I'm Bonch-Science Bot!")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)