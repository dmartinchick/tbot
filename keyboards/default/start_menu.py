from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = KeyboardButton(text='/Меню')
start_menu_button = ReplyKeyboardMarkup(resize_keyboard=True).add(menu)