from aiogram import types
from aiogram.types.inline_keyboard import InlineKeyboardMarkup
from request import*

btn_start = types.ReplyKeyboardMarkup(selective=True, resize_keyboard=True)
btn_start.add("Моя подписка")

p = types.InlineKeyboardButton('Получить доступ', callback_data='access')

p_b = types.InlineKeyboardMarkup(row_width=1).insert(p)

about = types.InlineKeyboardButton('Узнать подробности', callback_data='about')

about_b = InlineKeyboardMarkup(row_width=1).insert(about)
 

invest_button = types.ReplyKeyboardMarkup(selective=True, resize_keyboard=True)
invest_button.add("💰Открыть сделку")

open_pay = types.ReplyKeyboardMarkup(selective=True, resize_keyboard=True)
open_pay.add("📲Публиковать сигналы") 
open_pay.add("❌Закрыть сделку")