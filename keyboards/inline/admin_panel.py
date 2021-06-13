from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.inline.callback_datas import admin_choice

kb_admin_panel = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Добавить результаты", callback_data=admin_choice.new(
                item_name = "add_result"
            )),
        ],
        [
            InlineKeyboardButton(text="Исправить результат", callback_data="admin:update_result"),
        ],
        [
            InlineKeyboardButton(text="Сообщение всем пользователям", callback_data="admin:send_admin_message"),
        ],
    ]
)