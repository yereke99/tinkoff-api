import types

import bot
from load import bot, dp
from aiogram import types
from text import*
from keyboard import*
from request import*
import asyncio
from forma import Pay

@dp.callback_query_handler(text=['access', 'about', 'pay', 'add'])
async def inline_handler(query: types.CallbackQuery):
    que = query.data

    if que == 'access':
        await Pay.fio.set()
        await bot.send_message(
            query.from_user.id,
            text='ФИО?',
            reply_markup=types.ReplyKeyboardMarkup(selective=True, resize_keyboard=True).add("Отмена")
            )
    elif que == 'about':
        await bot.send_message(
            query.from_user.id,
            text='Спасибо',
            reply_markup=types.ReplyKeyboardMarkup()
        )

    elif que == 'pay':
        re = Request()
        payment_url = re.post_request()
        await asyncio.sleep(0.2)
        
        await bot.send_message(
            query.from_user.id,
            text=str(payment_url['PaymentURL'])
        )

    elif que == 'add':
        pass    
          
                  
