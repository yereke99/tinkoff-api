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
from database import*


class Pay(StatesGroup):
    fio = State()
    email = State()
    tele_number = State()
    

@dp.message_handler(state='*', commands='Отмена')
@dp.message_handler(Text(equals='Отмена', ignore_case=True), state='*')
async def cancell_handler(message: types.Message, state: FSMContext):
    """
        :param message: Бастартылды
        :param state: Тоқтату
        :return: finish
    """

    current_state = await state.get_state()
    if current_state is None:
        return

    logging.info('Отмена')
    await state.finish()
    await bot.send_message(
        message.from_user.id,
        text='Отменим',
        reply_markup=btn_start
    ) 

@dp.message_handler(state=Pay.fio)
async def fio_handle(message: types.Message, state: FSMContext):
    await Pay.next()
    global fio_
    
    async with state.proxy() as data:
        data['fio'] = message.text
        fio_ = data['fio']
    await bot.send_message(
        message.from_user.id,
        text='Электронная почта',
        reply_markup=types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    )    


@dp.message_handler(state=Pay.email)
async def fio_handle(message: types.Message, state: FSMContext):
    await Pay.next()
    global email_
    
    async with state.proxy() as data:
        data['email'] = message.text
        email_ = data['email']
    await bot.send_message(
        message.from_user.id,
        text='Телефон номер',
        reply_markup=types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    )    

@dp.message_handler(lambda message: not message.text.isdigit(), state=Pay.tele_number)
async def invalidContact(message: types.Message):
    return await message.reply("Только с цифрами")


@dp.message_handler(lambda message: message.text.isdigit(), state=Pay.tele_number)
async def fio_handle(message: types.Message, state: FSMContext):
    global tele_number_
    
    id = message.from_user.id
    async with state.proxy() as data:
        data['tele_number'] = message.text
        tele_number_ = data['tele_number']
   
    re = Request()
    re.AddCustomer(url="https://rest-api-test.tinkoff.ru/v2/AddCustomer", nick=str(id))
    
        
    
    await asyncio.sleep(0.5)
    init_payment = re.Init(url="https://rest-api-test.tinkoff.ru/v2/Init/", customerKey=str(id), recurrent=True)
    init = types.InlineKeyboardButton('Подвердит оплату', url=init_payment['PaymentURL'])
    
    init_payment_button = types.InlineKeyboardMarkup(row_width=1).insert(init)
    
    database = Database()
    
    
    database.insert_client(
            id, 
            fio_, 
            email_, 
            tele_number_, 
            init_payment['OrderId'], 
            init_payment['PaymentId'],
            0,
            0, 
            "",
            "",
            "false"
    )
    
    print(id)
    print(fio_)
    print(email_)
    print(tele_number_)
    print(init_payment['OrderId'])
    print(init_payment['PaymentId'])
    
    
    await bot.send_message(
        message.from_user.id,
        text=about_podpiska,
        reply_markup=init_payment_button
    )

    
    await state.finish()
