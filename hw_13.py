# from aiogram import Bot,Dispatcher
# from aiogram.types import Message
# from aiogram.filters import Command
# from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
# import asyncio
# # Создаем клавиатуру
# keyboard = ReplyKeyboardMarkup(
#     keyboard=[
#         [KeyboardButton(text="О нас"), KeyboardButton(text="Поддержка")]
#     ],
#     resize_keyboard=True  # Подгоняет размер кнопок под экран
# )

# TOKEN = "7582616773:AAGM6Da_CC650WEtp2QyvwGxndfyGemK9MA"
# bot = Bot(token=TOKEN)
# dp = Dispatcher()

# @dp.message(Command("start"))
# async def start_handlers(message:Message):
#     await message.answer("Привествую вас на боте aiogram 3!",reply_markup=keyboard)

# @dp.message(lambda message:message.text == "О нас")
# async def info_process(message:Message):
#     await message.answer("Мы — лучший бот! 🚀")

# @dp.message(lambda message: message.text == "Поддержка")
# async def pod_process(message:Message):
#     await message.answer("Напишите нам, если у вас есть вопросы! 💬")

# @dp.message()
# async def reverse_process(message:Message):
#     await message.answer(message.text)

# async def main():
#     await dp.start_polling(bot)

# if __name__ == '__main__':
#     asyncio.run(main())

from aiogram import Bot,Dispatcher
from aiogram.types import Message
from aiogram.filters import Command
import asyncio


TOKEN = "7582616773:AAGM6Da_CC650WEtp2QyvwGxndfyGemK9MA"
bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_handlers(message:Message):
    await message.answer("Привествую вас на боте aiogram 3\n"
                         "этот бот может отправить ваше сообщения обратно не смотря на размер")

@dp.message(Command("help"))
async def help_handlers(message:Message):
    await message.answer("Список команд которые есть в этом боте\n"
                         "/help - выводить список команд\n"
                         "/start - приветсвует вас и скажет что может этот бот")

@dp.message()
async def text_handlers(message:Message):
    await message.answer(f"вы написали - <{message.text}>")


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())

