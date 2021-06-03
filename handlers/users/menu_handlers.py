from keyboards.inline import callback_datas
import logging
from aiogram import types
from aiogram.types import CallbackQuery
from aiogram.dispatcher.filters import Command
from aiogram.utils import callback_data
from loader import dp

# from keyboards.inline.callback_datas import start_choice
from keyboards.inline.choise_start_menu import choise_start_menu

@dp.message_handler(Command("Меню"))
async def show_inline_menu(message: types.Message):
    await message.answer("О чем тебе рассказать?", reply_markup=choise_start_menu)

@dp.callback_query_handler(text_contains="what_now")
async def show_waht_now(call: types.CallbackQuery):
    await call.answer(cache_time=360)
    callback_data = call.data
    logging.info(f"{callback_data=}")

    await call.message.answer("Ща я покажу что сейчас просиходит")