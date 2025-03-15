from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardButton, InlineKeyboardMarkup)

main_menu = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Каталог')],
                                     [KeyboardButton(text='Корзина')],
                                     [KeyboardButton(text='Контакты'),
                                      KeyboardButton(text='Помощь')]],
                           resize_keyboard=True,
                           input_field_placeholder='Выберите пункт меню...')

register_keyboard = ReplyKeyboardMarkup(keyboard=[[
    KeyboardButton(text="Зарегистрироваться", request_contact=True)
]], resize_keyboard=True, one_time_keyboard=True)

catalog = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Футболки', callback_data='t-shirts')],
    [InlineKeyboardButton(text='Кроссовки', callback_data='sneakers')],
    [InlineKeyboardButton(text='Кепки', callback_data='caps')]])
