from aiogram import types
from aiogram.dispatcher.filters import Command
from loader import dp

from keyboards.inline.choise_start_menu import choise_start_menu

@dp.message_handler(commands='Меню')
async def show_inline_menu(message: types.Message):
    await message.answer("О чем тебе рассказать?", reply_markup=choise_start_menu)

