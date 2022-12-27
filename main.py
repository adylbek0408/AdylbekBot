import asyncio

from aiogram.utils import executor
from config import dp
import logging
from handlers import client, callback, extra, admin, fsmAdminMentor,notifications
from database.bot_db import sql_create
from database import bot_db

bot_db.register_handlers_bot_db(dp)
fsmAdminMentor.register_handlers_fsm_anketa(dp)
client.register_handler_client(dp)
callback.register_handler_callback(dp)
admin.register_handler_admin(dp)
notifications.register_handlers_notification(dp)

extra.register_handler_extra(dp)


async def on_startup(_):
    asyncio.create_task(notifications.scheduler())
    sql_create()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)