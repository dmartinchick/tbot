from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton, inline_keyboard
from keyboards.inline.callback_datas import table_tourism_choice


kb_table_tourism_menu = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(text="Hочное ориентирование", callback_data=table_tourism_choice.new(
            item_name = "night_orientation"
            )),
        ],
        [
            InlineKeyboardButton(text="Велотуризм",callback_data="table_tourism:cycling_tourism"),
        ],
        [
            InlineKeyboardButton(text="Техника пешеходного  туризма",callback_data="table_tourism:hiking_technique"),
        ],
        [
            InlineKeyboardButton(text="Туристический маршрут",callback_data="table_tourism:tourist_route")
        ]
    ]
)