from aiogram.types.base import T
from load import bot, dp
from aiogram import types
from keyboard import*
from text import*
import inline_handler

@dp.message_handler(commands=['admin'])
async def admin(message: types.Message):
    print(message.from_user.id)
    id_user = message.from_user.id
    if id_user == 800703982:
        await bot.send_message(
            message.from_user.id,
            text='Ваш(-а-) статус 📈Трейдер',
            reply_markup=invest_button
        )

@dp.message_handler(commands=['secret'])
async def adv(message: types.Message):
    id_user = 1576146812
    await bot.send_message(
            id_user,
            text=secret,
            reply_markup=btn_start
        )    

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    print(message.from_user.id)
    await bot.send_message(
        message.from_user.id,
        text="{name}, приветствуем вас!".format(name=message.from_user.first_name),
        reply_markup=btn_start
    )

    await bot.send_message(
        message.from_user.id,
        text=text_with_button,
        reply_markup=p_b
    )


@dp.message_handler(content_types=['text'])
async def text_handler(message: types.Message):
    msg = message.text
    
    if msg == "Моя подписка":
        await bot.send_message(
            message.from_user.id,
            text=podpiska,
            reply_markup=about_b
        )
    if msg == "💰Открыть сделку":
        await bot.send_message(
            message.from_user.id,
            text='Функцияналы',
            reply_markup=open_pay
        )    


