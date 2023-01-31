from aiogram.dispatcher.filters.state import StatesGroup, State


# Shaxsiy ma'lumotlarni yig'sih uchun PersonalData holatini yaratamiz
class locstates(StatesGroup):
    bank = State()
    bankomat = State()
    hospital = State()
    chemist = State()
    banks = State()
    hosts = State()