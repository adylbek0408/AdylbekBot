from aiogram import types, Dispatcher
from config import bot, dp

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


# @dp.callback_query_handler(text="button_call_1")
async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("NEXT 2", callback_data="button_call_2")
    markup.add(button_call_1)

    question = "Сколько направление в Geek Tech"
    answers = [
        "5",
        "3",
        "2",
        "6",
        "4",
        "7",
    ]

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=5,
        explanation="Стыдно не знать",
        open_period=5,
        reply_markup=markup
    )


async def quiz_3(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("NEXT 2", callback_data="button_call_3")
    markup.add(button_call_1)

    question = "в каком году началась 2 мировая война"
    answers = [
        "1999",
        "2020",
        "1894",
        "1941",
        "2000",
    ]

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=3,
        explanation="Стыдно не знать",
        open_period=5,
        reply_markup=markup
    )


def register_handler_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2, text="button_call_1")
    dp.register_callback_query_handler(quiz_3, text="button_call_2")
