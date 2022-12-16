from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor
from config import dp
from handlers import client, callback, extra, admin

client.register_handler_client(dp)
callback.register_handler_callback(dp)
admin.register_handler_admin(dp)
extra.register_handler_extra(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
