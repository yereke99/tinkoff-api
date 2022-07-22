from aiogram import Bot, Dispatcher, types
import logging
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config import Token

bot = Bot(token=Token, parse_mode=types.ParseMode.HTML)
memory = MemoryStorage()
dp = Dispatcher(bot, storage=memory)

logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s', level=logging.INFO,)
