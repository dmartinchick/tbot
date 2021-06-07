from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.inline.callback_datas import start_choice

kb_start_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Что сейчас происходит", callback_data=start_choice.new(
                item_name="what_now"
            )),
        ],
        [
            InlineKeyboardButton(text="Полное расписание", callback_data="start:full_schedule"),
        ],
        [
            InlineKeyboardButton(text="Посмотреть таблицы", callback_data="start:table")
        ],
        [
            InlineKeyboardButton(text="Управление подписками", callback_data="start:subscriptions"),
        ],
        [
            InlineKeyboardButton(text="Отмена", callback_data='cancell'),
        ]
        
    ]
)