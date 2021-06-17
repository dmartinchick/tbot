# - *- coding: utf- 8 - *-

from environs import Env

# Теперь используем вместо библиотеки python-dotenv библиотеку environs
env = Env()
env.read_env()

# Данные для подключения к Телеграммботу
BOT_TOKEN = env.str("BOT_TOKEN")  # Забираем значение типа str
ADMINS = env.list("ADMINS")  # Тут у нас будет список из админов
IP = env.str("ip")  # Тоже str, но для айпи адреса хоста

# Данные для подключения к базе данных
HOST = env.str("HOST")
PORT = env.int("PORT")
USER = env.str("USER")
PASSWORD = env.str("PASSWORD")
DB = env.str("DB")

