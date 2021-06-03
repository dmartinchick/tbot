import logging

# from aiogram import Dispatcher
from loader import dp
from data.config import ADMINS


async def on_startup_notify(dp):
    for admin in ADMINS:
        try:
            await dp.bot.send_message(admin, "Бот Запущен")

        except Exception as err:
            logging.exception(err)
