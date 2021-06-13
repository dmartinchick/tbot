from aiogram import types
#from aiogram.dispatcher.filters import Command
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default import start_menu_button

from utils.db_api.sqlighter import SQL
from aiogram.types.user import User

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):

    message_user = User.get_current()['id']
    rq = SQL.get_users()
    li_users = []
    for i in rq:
        li_users.append(i[0])
    if message_user in li_users:
        pass
    else:
        SQL.set_users(message_user)

    await message.answer(f"Привет ✋, {message.from_user.full_name}!\n"
                        "Я телеграм бот туристического фестиваля Сварог2021\n\n"
                        "❗ Я помогу соорентироваться какие конкурсы проходят прямо сейчас; \n"
                        "❗ Покажу расписание всего фестиваля;\n"
                        "❗ Раскажу правила и условия участия в конкурсах, а так же отвечу на вопрос кто ледирует прямо сейчас!\n\n"
                        "❗ Если ты захочешь, то я могу напоминить тебе об интересующих тебя конкурсах или сообщить об успехах команд, за которыми ты следишь")
    await message.answer("Для перехода к меню нажмите кнопку ниже 👇 или введите \"Меню\"", reply_markup=start_menu_button)
