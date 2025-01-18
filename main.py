# from aiogram import Bot, Dispatcher, types
# from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
# from aiogram.filters import Command 
# import asyncio

# BOT_TOKEN = "7582616773:AAGM6Da_CC650WEtp2QyvwGxndfyGemK9MA"
# bot = Bot(token=BOT_TOKEN)

# dp = Dispatcher()

# keyboard = ReplyKeyboardMarkup(
#     keyboard = [
#         [KeyboardButton(text="Привет"), KeyboardButton(text="Пока")],
#         [KeyboardButton(text="О погоде"), KeyboardButton(text="Новости")]
#     ],
#         resize_keyboard=True
# )

# @dp.message(Command("start"))
# async def start_handler(message:types.Message):
#     await message.answer("Привет! Выберите команду:",reply_markup=keyboard)

# @dp.message()
# async def handler_buttons(message:Message):
#     if message.text == "Привет":
#         await message.answer("Привет! Рад вас видеть")
#     elif message.text == "Пока":
#         await message.answer("Досвидания будем ждать вас снова")
#     elif message.text == "О погоде":
#         await message.answer("Сегодня погода дождливая, +10С")
#     elif message.text == "Новости":
#         await message.answer("Приближаеться кратко временые дожди!")
#     else:
#         await message.answer("Вы вели что-то не так! Попробуйте снова вести")

# async def main():
#     await dp.start_polling(bot)
# if __name__ == "__main__":
#     asyncio.run(main())

from aiogram import Bot, Dispatcher, types
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import Command 
import asyncio, logging
import random
import datetime

logging.basicConfig(level=logging.INFO)

BOT_TOKEN = "7582616773:AAGM6Da_CC650WEtp2QyvwGxndfyGemK9MA"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

keyboard = ReplyKeyboardMarkup(
    keyboard = [
        [KeyboardButton(text="Что это?"),KeyboardButton(text="Кто создал это?")],
        [KeyboardButton(text="Приветсвие"),KeyboardButton(text="help")],
        [KeyboardButton(text="Рандомная цифра от (1-30)"),KeyboardButton(text="Рандомный смайлик")],
        [KeyboardButton(text="Интересный факт"),KeyboardButton(text="Время суток")],
    ],
    resize_keyboard=True
)

@dp.message(Command("start"))
async def start_handler(message:Message):
    await message.answer("Привет я второй бот! Выберите действие:", reply_markup=keyboard)

@dp.message()
async def handler_buttons(message:Message):
    if message.text == "Что это?":
        await message.answer("Чат бот который может")
    elif message.text == "Приветсвие":
         await message.answer("Здраствуйте я бот на айограме")
    # elif message.text == "Случайное число 😲":
    #     random_user = random.randint(1,100)
    #     await message.answer(f"Ваше случайное число:{random_user}")
    elif message.text == "Кто создал это?":
        await message.answer("Этого бота создал Backend разработчик")
    elif message.text == "help":
        await message.answer("Обратитесь в подержку")
    elif message.text == "Рандомная цифра от (1-30)":
         random_user = random.randint(1,30)
         await message.answer(f"Ваше рандомное число:{random_user}")
    elif message.text == "Рандомный смайлик":
         smile = ["🤣","🫢"]
         smile_random = random.choice(smile)
         await message.answer(f"Ваш рандомный смайлик {smile_random}")
    elif message.text == "Интересный факт":
         fakt = ["Утки могут спать с одним открытым глазом ","Львы спят до 20 часов в день","Дельфины дают себе имена"]
         random_fakt = random.choice(fakt)
         await message.answer(f"Факт: {random_fakt}")
    elif message.text == "Время суток":
         user_data = datetime.datetime.now()
         await message.answer(f"Время: {user_data}")
    else:
        await message.answer("Команда не распознана. Пожалуйста, выберите действие из меню")

async def main():
        await dp.start_polling(bot)
if __name__=='__main__':
    try:
         asyncio.run(main())
    except KeyboardInterrupt:
        print('Завершение работы бота.')


# Бутуп айтсан тушундуром логированиени