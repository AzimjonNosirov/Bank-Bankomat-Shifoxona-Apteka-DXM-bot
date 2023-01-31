from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove

from keyboards.default.location_button import keyboard
from utils.misc.get_distance import choose_shortest
from loader import dp
from aiogram.dispatcher import FSMContext
from states.locstates import locstates
from data.Bankomat import Bankomat
from data.location import Banks
from data.Dorixona import Dorixona
from data.Shifoxonalar import Shifoxona
from keyboards.default.menuKeyboard import menuStart, menuBankomat, menuApteka
from keyboards.default.shahar_bank import shaharbank
from keyboards.default.shahar_shifoxona import shaharShifo

@dp.callback_query_handler(text="mylocation", state = "*")
async def show_contact_keys(call: CallbackQuery, state:FSMContext):
     await call.message.answer(text="Joylashuvni yuboring:", reply_markup=keyboard)

@dp.callback_query_handler(text="mylocationhos", state = "*")
async def show_contact_keys(call: CallbackQuery, state:FSMContext):
     await call.message.answer(text="Joylashuvni yuboring:", reply_markup=keyboard)

@dp.callback_query_handler(text="chemist", state = "*")
async def show_contact_keys(call: CallbackQuery, state:FSMContext):
     await call.message.answer(text="Joylashuvni yuboring:", reply_markup=keyboard)

@dp.callback_query_handler(text="pha", state = "*")
async def show_contact_keys(call: CallbackQuery, state:FSMContext):
     await call.message.answer(text="Dorixonalar joylashgan hududni ko'rish:", reply_markup=menuApteka)

@dp.callback_query_handler(text="atm", state = "*")
async def show_contact_keys(call: CallbackQuery, state:FSMContext):
     await call.message.answer(text="Bankomatlar joylashgan hududni ko'rish :", reply_markup=menuBankomat)

@dp.callback_query_handler(text="bank", state = "*")
async def show_contact_keys(call: CallbackQuery, state:FSMContext):
     await call.message.answer(text="Banklarni ko'rish :", reply_markup=shaharbank)

@dp.callback_query_handler(text="hospital", state = "*")
async def show_contact_keys(call: CallbackQuery, state:FSMContext):
     await call.message.answer(text="Shifoxonalarni ko'rish :", reply_markup=shaharShifo)

@dp.message_handler(content_types='location', state = locstates.bank)
async def get_contact(message: Message, state:FSMContext):
    
    location = message.location
    latitude = location.latitude
    longitude = location.longitude
    closest_shops = choose_shortest(location, Banks)

    text = "\n\n".join([f"<a href='{url}'>{bank_name}</a>\n Masofa: {distance:.1f} km."
                        for bank_name, distance, url, bank_location in closest_shops])

    await message.answer(f"Rahmat. Siz uchun eng yaqin bank 👇👇👇👇 \n"
                         f"{text}", disable_web_page_preview=True, reply_markup=menuStart)

    for bank_name, distance, url, bank_location in closest_shops:
        await message.answer_location(latitude=bank_location["lat"],
                                      longitude=bank_location["lon"])

    await state.finish()

@dp.message_handler(content_types='location', state = locstates.bankomat)
async def get_contact(message: Message, state:FSMContext):
    
    location = message.location
    latitude = location.latitude
    longitude = location.longitude
    closest_shops = choose_shortest(location, Bankomat)

    text = "\n\n".join([f"<a href='{url}'>{bankomat_name}</a>\n Masofa: {distance:.1f} km."
                        for bankomat_name, distance, url, bankomat_location in closest_shops])

    await message.answer(f"Rahmat. Siz uchun eng yaqin bankomat 👇👇👇👇 \n"
                         f"{text}", disable_web_page_preview=True, reply_markup=menuStart)

    for bankomat_name, distance, url, bankomat_location in closest_shops:
        await message.answer_location(latitude=bankomat_location["lat"],
                                      longitude=bankomat_location["lon"])
    await state.finish()

@dp.message_handler(content_types='location', state = locstates.hospital)
async def get_contact(message: Message, state:FSMContext):
    
    location = message.location
    latitude = location.latitude
    longitude = location.longitude
    closest_shops = choose_shortest(location, Shifoxona)

    text = "\n\n".join([f"<a href='{url}'>{hospital_name}</a>\n Masofa: {distance:.1f} km."
                        for hospital_name, distance, url, hospital_location in closest_shops])

    await message.answer(f"Rahmat. Siz uchun eng yaqin shifoxona 👇👇👇👇 \n"
                         f"{text}", disable_web_page_preview=True, reply_markup=menuStart)

    for hospital_name, distance, url, hospital_location in closest_shops:
        await message.answer_location(latitude=hospital_location["lat"],
                                      longitude=hospital_location["lon"])

    await state.finish()

@dp.message_handler(content_types='location', state = locstates.chemist)
async def get_contact(message: Message, state:FSMContext):
    
    location = message.location
    latitude = location.latitude
    longitude = location.longitude
    closest_shops = choose_shortest(location, Dorixona)

    text = "\n\n".join([f"<a href='{url}'>{chemist_name}</a>\n Masofa: {distance:.1f} km."
                        for chemist_name, distance, url, chemist_location in closest_shops])

    await message.answer(f"Rahmat. Siz uchun eng yaqin dorixona 👇👇👇👇 \n"
                         f"{text}", disable_web_page_preview=True, reply_markup=menuStart)

    for chemist_name, distance, url, chemist_location in closest_shops:
        await message.answer_location(latitude=chemist_location["lat"],
                                      longitude=chemist_location["lon"])

    await state.finish()


