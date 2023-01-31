from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

search_bank = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text="📍 Eng yaqin bankni topish", callback_data="mylocation"),
    ],
    [
        InlineKeyboardButton(text="🏛 Banklarni ko'rish", callback_data="bank"),
    ],
])

search_hos = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text="📍 Eng yaqin shifoxonani topish", callback_data="mylocationhos"),
    ],
    [
        InlineKeyboardButton(text="🏥 Shifoxonalarni ko'rish", callback_data="hospital"),
    ],
])