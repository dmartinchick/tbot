import data
from aiogram.types.message import Message
from data.config import ADMINS
from datetime import datetime
from typing import Text

from aiogram.dispatcher.filters.builtin import CommandSettings
from aiogram.types.user import User
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

@dp.message_handler(commands=['Меню','menu'], commands_prefix=['⠀','/'])
async def show_inline_menu(message: types.Message):
    await message.answer("О чем тебе рассказать?", reply_markup=kb_start_menu)


@dp.message_handler(Command("f_admin_microlabML2160"))
async def show_inline_admin_panel(message: types.Message):
    """Функция вызова меню администратора

    Args:
        message (types.Message): [description]
    """
    message_user = str(User.get_current()['id'])
    
    if message_user in ADMINS:
        await message.answer("Меню администратора")
    else:
        await message.answer("К сожелению данное меню доступно только администратору")


@dp.callback_query_handler(text_contains="what_now")
async def show_what_now(call: types.CallbackQuery):
    """ Функция возвращает пользователю текущие, а так же ближаешее меропритие

    Args:
        call (types.CallbackQuery): [description]
    """
    
    await call.answer(cache_time=360)
    callback_data = call.data
    logging.info(f"{callback_data=}")
    # rq = SQL.request_what_now()

    # Получение самого раннего и самого познего события фестиваля
    dt_start = SQL.find_date_start()
    dt_end = SQL.find_date_end()
    # tdate = datetime.now().strftime('%d.%m %H:%M')
    tdate = datetime(2021, 6, 18, 19, 40).strftime('%d.%m %H:%M')
    if tdate < dt_start:
        await call.message.answer("😁 Фестиваль еще не начался, \nвозвращайся сюда 18 июня!")
    elif tdate > dt_end:
        await call.message.answer("☹ К сожелению, фестиваль уже прошел.\nУвидимся в следующем году! 😁")
    else:
        await call.message.answer(text='🤓 Сейча проходит 🤓')
        
        # обращение к базе данных и получение данных
        rq = SQL.what_now()
        # запуск циклаобработки текущих событий
        for event in rq:
            # парсинг данных    
            event_name = event[0]
            time_start = event[1].strftime('%d.%m %H:%M')
            time_end = event[2].strftime('%d.%m %H:%M')
            address = event[3]
            contains = event[4]
            
            # отправка сообщения с информацией о конкурсе
            await call.message.answer_photo(photo=open(address,'rb'),caption="❗" + event_name)
            # TODO: Реализовать ссылку на подробную информацию о конкурсе
        
        # TODO: Реализовать отображения ближайшего мерпрития



    #TODO: заменить SQL.request_what_now на промежуточную функцию, которая будет преобразовывать ответ телеграмма в карточку событи. см.try.py
    

@dp.callback_query_handler(text_contains="full_schedule")
async def show_full_schedule(call: types.CallbackQuery):
    """ Показивает пользователю все расписание мероприятий

    Args:
        call (types.CallbackQuery): [description]
    """
    
    await call.answer(cache_time=360)
    callback_data = call.data
    logging.info(f"{callback_data=}")

    await call.message.answer(card.full_schedule())
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

    await call.message.answer("Ещё в разработке")


@dp.callback_query_handler(text_contains='share')
async def show_share(call: types.CallbackQuery):
    """Реализует отображения ссылку на телеграм

    Args:
        call (types.CallbackQuery): [description]
    """

    await call.answer(cache_time=360)
    callback_data = call.data
    logging.info(f"{callback_data}")

    await call.message.answer_photo(photo=open(r'data\img\share.jpg', 'rb'), caption="Отсканируй QR-код")


@dp.callback_query_handler(text_contains='about')
async def show_about_info(call: types.CallbackQuery):
    """Выводит информацию о естивале, а также положение по терислету

    Args:
        call (types.CallbackQuery): [description]
    """

    await call.answer(cache_time=360)
    callback_data = call.data
    logging.info(f"{callback_data}")

    await call.message.answer_document(document=open(r'data\docs\svarog2021_rule.pdf','rb'),caption='Положение туристического фестиваля Сварог 2021')

# TODO: cancel
