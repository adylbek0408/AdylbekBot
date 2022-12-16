from config import bot, dp, ADMINS
from aiogram import types, Dispatcher
import random


async def game(message: types.Message):
    if message.from_user.id in ADMINS:
        if message.text.startswith('game'):
            emojies = ['🏀', '⚽️', '🎲', '🎰', '🎯', '🎳']
            emoji = random.choice(emojies)
            await bot.send_dice(message.from_user.id, emoji=emoji)
    else:
        await message.answer('ты не админ')


def register_handler_admin(dp: Dispatcher):
    dp.register_message_handler(game)
