from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton, inline_keyboard
from keyboards.inline.callback_datas import table_sport_choice


kb_table_culture_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Боди-Арт",callback_data=table_sport_choice.new(
                item_name = "body_art",
            )),
        ],
        [
            InlineKeyboardButton(text="Бивуак",callback_data="table_sport:bivouac")
        ],
        [
            InlineKeyboardButton(text="Драник-fest",callback_data="table_sport:dranik-fest")
        ],
        [
            InlineKeyboardButton(text="Творческий конкурс",callback_data="table_sport:creative_competition")
        ]
    ]
)