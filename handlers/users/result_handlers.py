from aiogram.types.message import Message
from aiogram.types import CallbackQuery
from aiogram import types

from loader import dp
import logging

from keyboards.inline.tabel_menu_tourism import kb_table_tourism_menu
from keyboards.inline.tabel_menu_sport import kb_table_sport_menu
from keyboards.inline.table_menu_culture import kb_table_culture_menu

@dp.callback_query_handler(text_contains="festival_cup")
async def show_festival_cup_result(call: types.CallbackQuery):
    """Возвращает пользователю результат кубка фестиваля
    """
    await call.answer(cache_time=360)
    callback_data = call.data
    logging.info(f"{callback_data=}")

    await call.message.answer_photo(photo=open(r"data\img\festival_cup.jpg",'rb'),caption="Кубок фестиваля")


@dp.callback_query_handler(text_contains="holding_cup")
async def show_holding_cup_result(call: types.CallbackQuery):
    """Возвращает пользователю результат кубка холдинга
    """
    await call.answer(cache_time=360)
    callback_data = call.data
    logging.info(f"{callback_data=}")

    await call.message.answer_photo(photo=open(r"data\img\holding_cup.jpg",'rb'),caption="Кубок холдинга")


@dp.callback_query_handler(text_contains="tourism_cup")
async def show_tourism_cup_result(call: types.CallbackQuery):
    """Возвращает пользователю результат кубка туризма
    """
    await call.answer(cache_time=360)
    callback_data = call.data
    logging.info(f"{callback_data=}")

    await call.message.answer_photo(photo=open(r"data\img\cup_tourism.jpg",'rb'),caption="Кубок туризма\n\nРезультаты конкурсов из категории Кубка туризма смотри ниже   👇",reply_markup=kb_table_tourism_menu)


@dp.callback_query_handler(text_contains="sports_cup")
async def show_sports_cup_result(call: types.CallbackQuery):
    """Возвращает пользователю результат кубка спорта
    """
    await call.answer(cache_time=360)
    callback_data = call.data
    logging.info(f"{callback_data=}")

    await call.message.answer_photo(photo=open(r"data\img\sports_cup.jpg",'rb'),caption="Кубок спорта\n\nРезультаты конкурсов из категории Кубка спорта смотри ниже   👇",reply_markup=kb_table_sport_menu)


@dp.callback_query_handler(text_contains="culture_cup")
async def show_culture_cup_result(call: types.CallbackQuery):
    """Возвращает пользователю результат кубка спорта
    """
    await call.answer(cache_time=360)
    callback_data = call.data
    logging.info(f"{callback_data=}")

    await call.message.answer_photo(photo=open(r"data\img\culture_cup.jpg",'rb'),caption="Кубок культуры\n\nРезультаты конкурсов из категории Кубка культуры смотри ниже   👇",reply_markup=kb_table_culture_menu)


@dp.callback_query_handler(text_contains="night_orientation")
async def show_night_orientation_result(call: types.CallbackQuery):
    """Возвращает пользователю результат ночного ориентирования
    """
    await call.answer(cache_time=360)
    callback_data = call.data
    logging.info(f"{callback_data=}")

    await call.message.answer_photo(photo=open(r"data\img\pic_night_orientation.jpg",'rb'),caption="Ночное ориентирование")


@dp.callback_query_handler(text_contains="cycling_tourism")
async def show_cycling_tourism_result(call: types.CallbackQuery):
    """Возвращает пользователю результат Велотуризм
    """
    await call.answer(cache_time=360)
    callback_data = call.data
    logging.info(f"{callback_data=}")

    await call.message.answer_photo(photo=open(r"data\img\pic_cycling_tourism.jpg",'rb'),caption="Велоориентирование")


@dp.callback_query_handler(text_contains="hiking_technique")
async def show_hiking_technique_result(call: types.CallbackQuery):
    """Возвращает пользователю результат Техники пешеходного туризма
    """
    await call.answer(cache_time=360)
    callback_data = call.data
    logging.info(f"{callback_data=}")

    await call.message.answer_photo(photo=open(r"data\img\pic_hiking_technique.jpg",'rb'),caption="Техника пешеходного туризма")


@dp.callback_query_handler(text_contains="tourist_route")
async def show_tourist_route_result(call: types.CallbackQuery):
    """Возвращает пользователю результат Туристического маршрута
    """
    await call.answer(cache_time=360)
    callback_data = call.data
    logging.info(f"{callback_data=}")

    await call.message.answer_photo(photo=open(r"data\img\pic_tourist_route.jpg",'rb'),caption="Туристический маршрут")


@dp.callback_query_handler(text_contains="sleight_of_hand")
async def show_sleight_of_hand_result(call: types.CallbackQuery):
    """Возвращает пользователю результат Ловкость рук
    """
    await call.answer(cache_time=360)
    callback_data = call.data
    logging.info(f"{callback_data=}")

    await call.message.answer_photo(photo=open(r"data\img\pic_sleight_of_hand.jpg",'rb'),caption="Ловкость рук")


@dp.callback_query_handler(text_contains="fight_for_the_man")
async def show_fight_for_the_man_result(call: types.CallbackQuery):
    """Возвращает пользователю результат Борьба за мужика
    """
    await call.answer(cache_time=360)
    callback_data = call.data
    logging.info(f"{callback_data=}")

    await call.message.answer_photo(photo=open(r"data\img\pic_fight_for_the_man.jpg",'rb'),caption="Борьба за мужика")


@dp.callback_query_handler(text_contains="thors_Hammer")
async def show_thors_Hammer_result(call: types.CallbackQuery):
    """Возвращает пользователю результат Молота Тора
    """
    await call.answer(cache_time=360)
    callback_data = call.data
    logging.info(f"{callback_data=}")

    await call.message.answer_photo(photo=open(r"data\img\pic_thors_Hammer.jpg",'rb'),caption="Молот Тора")


@dp.callback_query_handler(text_contains="volleyball")
async def show_volleyball_result(call: types.CallbackQuery):
    """Возвращает пользователю результат Волейбола
    """
    await call.answer(cache_time=360)
    callback_data = call.data
    logging.info(f"{callback_data=}")

    await call.message.answer_photo(photo=open(r"data\img\pic_volleyball.jpg",'rb'),caption="Волейбол")


@dp.callback_query_handler(text_contains="tug_of_war")
async def show_tug_of_war_result(call: types.CallbackQuery):
    """Возвращает пользователю результат Перетягивание каната
    """
    await call.answer(cache_time=360)
    callback_data = call.data
    logging.info(f"{callback_data=}")

    await call.message.answer_photo(photo=open(r"data\img\pic_tug_of_war.jpg",'rb'),caption="Перетягивание каната")


@dp.callback_query_handler(text_contains="knockers")
async def show_knockers_result(call: types.CallbackQuery):
    """Возвращает пользователю результат Выбивалы
    """
    await call.answer(cache_time=360)
    callback_data = call.data
    logging.info(f"{callback_data=}")

    await call.message.answer_photo(photo=open(r"data\img\pic_knockers.jpg",'rb'),caption="Выбивалы")


@dp.callback_query_handler(text_contains="body_art")
async def show_body_art_result(call: types.CallbackQuery):
    """Возвращает пользователю результат Боди-Арт
    """
    await call.answer(cache_time=360)
    callback_data = call.data
    logging.info(f"{callback_data=}")

    await call.message.answer_photo(photo=open(r"data\img\pic_body_art.jpg",'rb'),caption="Боди-Арт")


@dp.callback_query_handler(text_contains="bivouac")
async def show_bivouac_result(call: types.CallbackQuery):
    """Возвращает пользователю результат Бивуак
    """
    await call.answer(cache_time=360)
    callback_data = call.data
    logging.info(f"{callback_data=}")

    await call.message.answer_photo(photo=open(r"data\img\pic_bivouac.jpg",'rb'),caption="Бивуак")


@dp.callback_query_handler(text_contains="dranik-fest")
async def show_dranik_fest_result(call: types.CallbackQuery):
    """Возвращает пользователю результат Драник-fest
    """
    await call.answer(cache_time=360)
    callback_data = call.data
    logging.info(f"{callback_data=}")

    await call.message.answer_photo(photo=open(r"data\img\pic_dranik-fest.jpg",'rb'),caption="Драник-fest")


@dp.callback_query_handler(text_contains="creative_competition")
async def show_creative_competition_result(call: types.CallbackQuery):
    """Возвращает пользователю результат Творческий конкурс
    """
    await call.answer(cache_time=360)
    callback_data = call.data
    logging.info(f"{callback_data=}")

    await call.message.answer_photo(photo=open(r"data\img\pic_creative_competition.jpg",'rb'),caption="Творческий конкурс")