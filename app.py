import utils
from handlers.users.start import bot_start
from handlers.users.result_handlers import show_festival_cup_result, show_holding_cup_result, show_tourism_cup_result, show_sports_cup_result, show_culture_cup_result
from handlers.users.menu_handlers import show_inline_menu, show_what_now, show_what_next, show_festival_map, show_share, show_about_info, show_events_rules, show_events_info
from handlers.users.result_handlers import show_festival_cup_result, show_holding_cup_result, show_tourism_cup_result, show_sports_cup_result, show_culture_cup_result, show_night_orientation_result, show_cycling_tourism_result, show_hiking_technique_result, show_tourist_route_result, show_sleight_of_hand_result, show_fight_for_the_man_result, show_thors_Hammer_result, show_volleyball_result, show_tug_of_war_result, show_knockers_result, show_body_art_result, show_bivouac_result, show_dranik_fest_result, show_creative_competition_result

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
