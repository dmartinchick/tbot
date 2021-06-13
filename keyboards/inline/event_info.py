from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.inline.callback_datas import card_info_choice

kb_event_card_info = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Правила", callback_data=card_info_choice.new(
                item_name = "event_rules"
            )),
            InlineKeyboardButton(text="Короткая справка", callback_data="card:event_info"),
        ]
    ]
)