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
            InlineKeyboardButton(text="Ближайшие меропрития", callback_data="start:what_next"),
        ],
        [
            InlineKeyboardButton(text="Полное расписание", callback_data="start:full_schedule"),
        ],
        [
            InlineKeyboardButton(text="Таблицы результатов", callback_data="start:tables")
        ],
        [
            InlineKeyboardButton(text="Карта фестиваля", callback_data="start:festival_map"),
        ],
        [
            InlineKeyboardButton(text="Поделиться ссылкой", callback_data="start:share"),
        ],
        [
            InlineKeyboardButton(text='О фестивале', callback_data='start:about'),
        ],        
    ]
)