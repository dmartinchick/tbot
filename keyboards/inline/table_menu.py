from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.inline.callback_datas import table_choice


kb_table_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Кубок фестиваля", callback_data=table_choice.new(
                item_name="festival_cup"
                )),
        ],
        [
            InlineKeyboardButton(text="Кубок холдинга", callback_data = "table_result:holding_cup")
        ],
        [
            InlineKeyboardButton(text="Кубок туризма", callback_data = "table_result:tourism_cup")
        ],
        [
            InlineKeyboardButton(text="Кубок спорта", callback_data = "table_result:sports_cup")
        ],
        [
            InlineKeyboardButton(text="Кубок культуры", callback_data='table_result:culture_cup')
        ]
    ],
)