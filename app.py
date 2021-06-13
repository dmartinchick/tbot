import utils
from handlers.users.start import bot_start
from handlers.users.menu_handlers import show_inline_menu, show_what_now, show_share, show_about_info, show_inline_admin_panel, show_events_rules, show_events_info
from utils.db_api import sqlighter

from aiogram import executor

import middlewares, filters, handlers

from loader import dp
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands


async def on_startup(dispatcher):
    # Устанавливаем дефолтные команды
    await set_default_commands(dispatcher)

    # Уведомляет про запуск
    await on_startup_notify(dispatcher)
    

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
