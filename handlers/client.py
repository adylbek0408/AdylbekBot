from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import bot, dp
from aiogram import types, Dispatcher


# @dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer('hello!')


# @dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("NEXT 1", callback_data="button_call_1")
    markup.add(button_call_1)

    question = "В каком году открылся Geek Tech"
    answers = [
        '2017',
        '2020',
        '2018',
        '2021',
        '2019',
    ]

    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="Стыдно не знать",
        open_period=5,
        reply_markup=markup
    )


async def pin_message(message: types.Message):
    if message.reply_to_message:
        await bot.pin_chat_message(message.chat.id, message.reply_to_message.message_id)
    else:
        await message.answer('сообщение должно быть ответом!')


# @dp.message_handler(commands=['mem'])
async def mem(message: types.Message):
    photo = open('media/cbd531ca07e7148162e6077a9bc714ea.jpg', 'rb')
    await bot.send_photo(message.from_user.id, photo=photo)


def register_handler_client(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start'])
    dp.register_message_handler(mem, commands=['mem'])
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_message_handler(pin_message, commands=['pin'], commands_prefix='!/')
