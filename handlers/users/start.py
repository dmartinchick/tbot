from aiogram import types
#from aiogram.dispatcher.filters import Command
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default import start_menu_button

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Привет, {message.from_user.full_name}!\n"
                        "Я телеграм бот туристического фестиваля Сварог2021\n\n"
                        "Я помогу соорентироваться какие конкурсы проходят прямо сейчас, "
                        "раскажу правила и условия участия в конкурсах, а так же отвечу на вопрос кто ледирует прямо сейчас!\n\n"
                        "Если ты захочешь, то я могу напоминить тебе об интересующих тебя конкурсах или сообщить об успехах команд, за которыми ты следишь")
    await message.answer("Для перехода к меню нажмите кнопку ниже", reply_markup=start_menu_button)

# TODO: реализвать указание на кнопку меню, саму кнопку меню, а так же внести пользователя в базу