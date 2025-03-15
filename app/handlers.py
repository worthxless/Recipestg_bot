from aiogram import F, Router, types
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from aiogram.filters import CommandStart, Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import  FSMContext
from sqlalchemy.util import await_only

import app.keyboard as kb
from app.database.requests.user import create_new_user, get_user

router = Router()


# class Register(StatesGroup):
#     name = State()
#     age = State()
#     course = State()


@router.message(CommandStart())
async def cmd_start(message: Message):
    user = message.from_user
    if get_user(user.id) is None:
        await message.answer(f"Привет, {user.username}!!! Сначала зарегистрируйся", reply_markup=kb.register_keyboard)
    else:
        await message.answer(f"C возвращением, {user.username}.", reply_markup=kb.main_menu)


@router.message(F.contact)
async def cmd_start(message: Message):
    user = message.from_user
    if get_user(user.id) is not None:
        create_new_user(
            user.id,
            user.first_name,
            user.last_name,
            user.username,
            message.contact.phone_number
        )
        return await message.answer("Успешно получено \nГлавное Меню",reply_markup=kb.main_menu)
    return await message.answer("Вы уже зарегистрированы", reply_markup=kb.main_menu)

@router.message(F.text=="Помощь")
async def cmd_start(message: Message):
    await message.answer("Выбирай что нужно", reply_markup=kb.main_menu)

@router.message(F.text=="Каталог")
async def catalog(message: Message):
    await message.answer('Выберите категорию товара', reply_markup=kb.catalog)

@router.callback_query(F.data == "t-shirts")
async def tshirt(callback: CallbackQuery):
    await callback.message.answer('Вы выбрали категорию футболок')
    await callback.answer()


# @router.message(Command('register'))
# async def register(message: Message, state: FSMContext):
#     await state.set_state(Register.name)
#     await message.answer('Введите ваше имя')
#
# @router.message(Register.name)
# async def register_name(message: Message, state: FSMContext):
#     await state.update_data(name=message.text)
#     await state.set_state(Register.age)
#     await message.answer('Введите свой возраст')
#
# @router.message(Register.age)
# async def register_age(message: Message, state: FSMContext):
#     await state.update_data(age=message.text)
#     await state.set_state(Register.course)
#     await message.answer('Введите свой курс')
#
# @router.message(Register.course)
# async def register_course(message: Message, state: FSMContext):
#     await state.update_data(course=message.text)
#     data = await state.get_data()
#     await message.answer(f'Ваше имя: {data["name"]}\nВаш возраст: {data["age"]}\nВаш курс: {data["course"]} ')
#     await state.clear()





















