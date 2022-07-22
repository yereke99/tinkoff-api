import logging, text

from aiogram.dispatcher.filters import state
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from load import bot, dp
from aiogram.dispatcher.filters import Text
from aiogram import types
from keyboard import*
from text import*
import inline_handler
import asyncio
import requests


class Send(StatesGroup):
    push = State()

@dp.message_handler(state='*', commands='??????')
@dp.message_handler(Text(equals='??????', ignore_case=True), state='*')
async def cancell_handler(message: types.Message, state: FSMContext):
    """
        :param message: ???????????
        :param state: ???????
        :return: finish
    """

    current_state = await state.get_state()
    if current_state is None:
        return

    logging.info('??????')
    await state.finish()
    await bot.send_message(
        message.from_user.id,
        text='???????',
        reply_markup=btn_start
    ) 

@dp.message_handler(state=Send.push)
async def push_handler(message: types.Message, state: FSMContext):
    global text_
    async with state.proxy() as data:
        data['fio'] = message.text
        text_ = data['fio']
    await bot.send_message(
        message.from_user.id,
        text=secret,
        reply_markup=btn_start
    )  

    await state.finish()