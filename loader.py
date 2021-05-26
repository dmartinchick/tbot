import asyncio
import aiomysql

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from mysql.connector.errors import Error

from data import config

# Загрузка подключения к Боту
bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# Загрузка подключения к базе данных
loop = asyncio.get_event_loop()
@asyncio.coroutine
async def get_event_name():
    conn = await aiomysql.connect(
        host=config.HOST,
        port=config.PORT,
        user=config.USER,
        password=config.PASSWORD,
        db='svarog2021',
        loop=loop)
    cur = await conn.cursor()
    async with conn.cursor() as cur:
        await cur.execute('SELECT name FROM event WHERE id=%s', 1)
        print(cur.fetchall())

loop.run_until_complete(get_event_name())

