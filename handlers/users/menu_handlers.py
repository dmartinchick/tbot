from typing import Text
from keyboards.inline import callback_datas
import logging
from aiogram import types
from aiogram.types import CallbackQuery
from aiogram.dispatcher.filters import Command
from aiogram.utils import callback_data
from loader import dp

# Импортируем клавиатуры
# from keyboards.inline.callback_datas import start_choice
from keyboards.inline.start_menu import kb_start_menu
from keyboards.inline.table_menu import kb_table_menu

from utils.db_api.sqlighter import SQL
from utils.misc import card

@dp.message_handler(Command("Меню"))
async def show_inline_menu(message: types.Message):
    await message.answer("О чем тебе рассказать?", reply_markup=kb_start_menu)

@dp.callback_query_handler(text_contains="what_now")
async def show_what_now(call: types.CallbackQuery):
    """ Функция возвращает пользователю текущие, а так же ближаешее меропритие

    Args:
        call (types.CallbackQuery): [description]
    """
    
    await call.answer(cache_time=360)
    callback_data = call.data
    logging.info(f"{callback_data=}")
    rq = SQL.request_what_now()

    #TODO: заменить SQL.request_what_now на промежуточную функцию, которая будет преобразовывать ответ телеграмма в карточку событи. см.try.py
    await call.message.answer(card.create_card(rq))
    

@dp.callback_query_handler(text_contains="full_schedule")
async def show_full_schedule(call: types.CallbackQuery):
    """ Показивает пользователю все расписание мероприятий

    Args:
        call (types.CallbackQuery): [description]
    """
    
    await call.answer(cache_time=360)
    callback_data = call.data
    logging.info(f"{callback_data=}")

    await call.message.answer("полное рассписание")
    # TODO: Реализвать обращение к базе данных и вывод всего расписания мероприятий

@dp.callback_query_handler(text_contains="table")
async def show_table(call: types.CallbackQuery):
    """ Реализует переход к inline меню выбора таблицы кубков

    Args:
        call (types.CallbackQuery): [description]
    """
    
    await call.answer(cache_time=360)
    callback_data = call.data
    logging.info(f"{callback_data}")

    await call.message.answer("Какой кубок тебя интересует?", reply_markup=kb_table_menu)
    # TODO: длбавить более красивое описани + картинку??

@dp.callback_query_handler(text_contains="subscriptions")
async def show_subscriptions(call: types.CallbackQuery):
    """ Реализует переход к меню управления подписками

    Args:
        call (types.CallbackQuery): [description]
    """

    await call.answer(cache_time=360)
    callback_data = call.data
    logging.info(f"{callback_data}")

    await call.message.answer("У тебя пока нет подписок, хочешь добавить?")
    
# TODO: cancel
