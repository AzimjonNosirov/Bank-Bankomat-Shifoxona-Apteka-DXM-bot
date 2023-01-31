from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

search_bankomat = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="📍 Eng yaqin bankomatni topish", callback_data="mylocation"),
        ],
        [
            InlineKeyboardButton(text="🏛 Bankomatlarni ko'rish", callback_data="atm"),
        ],
    ],
)

search_chemist = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="📍 Eng yaqin dorixonani topish", callback_data="chemist"),
        ],
        [
            InlineKeyboardButton(text="🏥 Dorixonalarnini ko'rish", callback_data="pha"),
        ],
    ],
)