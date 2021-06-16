from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton, inline_keyboard
from keyboards.inline.callback_datas import table_sport_choice

kb_table_sport_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Ловкость рук",callback_data=table_sport_choice.new(
                item_name = "sleight_of_hand",
            )),
        ],
        [
            InlineKeyboardButton(text="Борьба за мужика",callback_data="table_sport:fight_for_the_man")
        ],
        [
            InlineKeyboardButton(text="Молот Тора",callback_data="table_sport:thors_Hammer")
        ],
        [
            InlineKeyboardButton(text="Волейбол",callback_data="table_sport:volleyball")
        ],
        [
            InlineKeyboardButton(text="Перетягивание каната",callback_data="table_sport:tug_of_war")
        ],
        [
            InlineKeyboardButton(text="Выбивалы",callback_data="table_sport:knockers")
        ]
    ]
)