from typing import Text
from keyboards.inline import callback_datas
import logging
from aiogram import types
from aiogram.types import CallbackQuery
from aiogram.dispatcher.filters import Command
from aiogram.utils import callback_data
from loader import dp

# from keyboards.inline.callback_datas import start_choice
from keyboards.inline.start_menu import kb_start_menu
from keyboards.inline.table_menu import kb_table_menu

@dp.message_handler(Command("Меню"))
async def show_inline_menu(message: types.Message):
    await message.answer("О чем тебе рассказать?", reply_markup=kb_start_menu)

@dp.callback_query_handler(text_contains="what_now")
async def show_waht_now(call: types.CallbackQuery):
    await call.answer(cache_time=360)
    callback_data = call.data
    logging.info(f"{callback_data=}")

    await call.message.answer("Ща я покажу что сейчас просиходит")
    # TODO: реализавать функцию показа действующих событий и ближайших


@dp.callback_query_handler(text_contains="full_schedule")
async def show_waht_now(call: types.CallbackQuery):
    await call.answer(cache_time=360)
    callback_data = call.data
    logging.info(f"{callback_data=}")

    await call.message.answer("Ща я покажу что сейчас просиходит")
    # TODO: Реализвать обращение к базе данных и вывод всего расписания мероприятий

@dp.callback_query_handler(text_contains="table")
async def show_table(call: types.CallbackQuery):
    await call.answer(cache_time=360)
    callback_data = call.data
    logging.info(f"{callback_data}")

    await call.message.answer("Какой кубок тебя интересует?", reply_markup=kb_table_menu)
    # TODO: длбавить более красивое описани + картинку??

@dp.callback_query_handler(text_contains="subscriptions")
async def show_subscriptions(call: types.CallbackQuery):
    await call.answer(cache_time=360)
    callback_data = call.data
    logging.info(f"{callback_data}")

    await call.message.answer("У тебя пока нет подписок, хочешь добавить?")
    # TODO: Реализовать менеджер подписок
# TODO: cancel
