from aiogram.dispatcher.filters import Text, Command
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, Message
from loader import dp, bot
from keyboards.default.menuKeyboard import menuApteka, menuStart
from keyboards.default.shahar_apteka import shaharApteka, davlapteka
from states.locstates import locstates
from aiogram.dispatcher import FSMContext

@dp.message_handler(text="Namangan shahar", state=locstates.chemist)
async def send_chemist1(message:Message, state=FSMContext):
    await message.answer("Namangan shahar tanlandi", reply_markup=shaharApteka)
    await state.finish()

@dp.message_handler(text="Davlatobod tuman", state=locstates.chemist)
async def send_chemist2(message:Message, state=FSMContext):
    await message.answer("Davlatobod tumani tanlandi", reply_markup=davlapteka)
    await state.finish()

# @dp.message_handler(text="Yangi Namangan tuman")
# async def send_chemist3(message:Message):
#     await message.answer("Yangi Namangan tumani tanlandi", reply_markup=shaharApteka)

# @dp.message_handler(text="Namangan tuman")
# async def send_chemist4(message:Message):
#     await message.answer("Namangan tumani tanlandi", reply_markup=shaharApteka)

# @dp.message_handler(text="To'raqo'rg'on tuman")
# async def send_chemist5(message:Message):
#     await message.answer("To'raqo'rg'on tumani tanlandi", reply_markup=shaharApteka)

# @dp.message_handler(text="Mingbuloq tuman")
# async def send_chemist6(message:Message):
#     await message.answer("Mingbuloq tumani tanlandi", reply_markup=shaharApteka)

# @dp.message_handler(text="Kosonsoy tuman")
# async def send_chemist7(message:Message):
#     await message.answer("Kosonsoy tumani tanlandi", reply_markup=shaharApteka)

# @dp.message_handler(text="Pop tuman")
# async def send_chemist8(message:Message):
#     await message.answer("Pop tumani tanlandi", reply_markup=shaharApteka)

# @dp.message_handler(text="Norin tuman")
# async def send_chemist9(message:Message):
#     await message.answer("Norin tumani tanlandi", reply_markup=shaharApteka)

# @dp.message_handler(text="Uychi tuman")
# async def send_chemist10(message:Message):
#     await message.answer("Uychi tumani tanlandi", reply_markup=shaharApteka)

# @dp.message_handler(text="Chortoq tuman")
# async def send_chemist11(message:Message):
#     await message.answer("Chortoq tumani tanlandi", reply_markup=shaharApteka)

# @dp.message_handler(text="Chust tuman")
# async def send_chemist12(message:Message):
#     await message.answer("Chust tumani tanlandi", reply_markup=shaharApteka)

# @dp.message_handler(text="Uchqo'rg'on tuman")
# async def send_chemist13(message:Message):
#     await message.answer("Uchqo'rg'on tumani tanlandi", reply_markup=shaharApteka)

# @dp.message_handler(text="Yangiqo'rg'on tuman")
# async def send_chemist14(message:Message):
#     await message.answer("Yangiqo'rg'on tumani tanlandi", reply_markup=shaharApteka)

@dp.message_handler(text="🔙 Ortga")
async def send_bac(message:Message):
    await message.answer("Ortga", reply_markup=menuApteka)
    await locstates.chemist.set()

@dp.message_handler(text="\"LIFEUZ 24\" dorixonasi")
async def send_chemist15(message:Message):
    await message.answer("Manzil: G'irvonsoy ko'chasi\n Mo'ljal: Namangan tibbiy diagnostika markazi, \"Sayhun\" mehmonxonasi\n Tel:+998 99 696 00 06\n Ish vaqti: 24/7")
    
@dp.message_handler(text="\"111\" dorixonasi")
async def send_chemist16(message:Message):
    await message.answer("Manzil: Nomongoniy ko'chasi\n Mo'ljal: \"Sayhun\" mehmonxonasi\n Tel:+998 90 278 15 20\n Ish vaqti: 24/7 ")

@dp.message_handler(text="\"555\" dorixonasi")
async def send_chemist17(message:Message):
    await message.answer("Manzil: Namangan shahar, Hamroh ko'chasi\n Tel:+998 69 227 10 90\n Ish vaqti: 24/7")

@dp.message_handler(text="\"Arxi Med Farm Shifo\" dorixonasi")
async def send_chemist18(message:Message):
    await message.answer("Manzil: Ququmboy shasse, 5-kichik nohiya 38/16\n Tel:+998 91 360 52 33\n        +998 91 292 42 12\n Ish vaqti: 24/7")

@dp.message_handler(text="\"Best Pharm\" dorixonasi")
async def send_chemist19(message:Message):
    await message.answer("Manzil: Go'zal ko'chasi\n Mo'ljal: 7-oilaviy poliklinikasi, 35-maktab atrofida\n Tel:+998 94 278 04 40\n Ish vaqti: 24/7")

@dp.message_handler(text="\"Betterton\" dorixonasi")
async def send_chemist20(message:Message):
    await message.answer("Manzil: G'alaba ko'chasi, 6-kichik nohiya 1A-uy\n Tel:+998 -------\n Ish vaqti: 24/7")

@dp.message_handler(text="\"Do'stlik Farm\" dorixonasi")
async def send_chemist21(message:Message):
    await message.answer("Manzil: Islom Karimov ko'chasi, 11-uy\n Mo'ljal: \"Sanoat qurilish bank\" filiali oldida\n Tel:+998 69 234 30 77\n Ish vaqti: 24/7")

@dp.message_handler(text="\"Doctor\" dorixonasi")
async def send_chemist22(message:Message):
    await message.answer("Manzil: To'raqo'rg'on ko'chasi, 157-uy\n Mo'ljal: 3-oilaviy poliklinikasi\n Tel:+998 69 233 50 90\n Ish vaqti: 24/7 ")

@dp.message_handler(text="\"Eventus\" dorixonasi")
async def send_chemist23(message:Message):
    await message.answer("Manzil: Qo'qon ko'chasi, 1-uy\n Mo'ljal: \"Oqtepa lavash\", Soliq inspeksiyasi\n Tel:+998 94 301 01 90          +998 90 222 37 35 \n Ish vaqti: 24/7")

@dp.message_handler(text="\"Farm-Scales\" dorixonasi")
async def send_chemist24(message:Message):
    await message.answer("Manzil: G'alaba ko'chasi, 4-kichik nohiya\n Tel:+998 69 227 18 13\n Ish vaqti: 24/7")

@dp.message_handler(text="\"Firdavsbek farm savdo servis\" dorixonasi")
async def send_chemist25(message:Message):
    await message.answer("Manzil: Istiqlol ko'chasi, 6-uy")

@dp.message_handler(text="\"Gigant Farm Servis\" dorixonasi")
async def send_chemist26(message:Message):
    await message.answer("Manzil: Navoiy ko'chasi, 6-uy")

@dp.message_handler(text="\"Globus Farm\" dorixonasi")
async def send_chemist27(message:Message):
    await message.answer("Manzil: Islom Karimov ko'chasi, 11-uy\n Tel:+998 69 234 30 72\n Ish vaqti: 24/7")

@dp.message_handler(text="\"Hojiakbar Sifat Savdo\" dorixonasi")
async def send_chemist28(message:Message):
    await message.answer("Manzil: Nodira ko'chasi, 6-uy\n Tel:+998 69 227 78 79\n Ish vaqti: 24/7")

@dp.message_handler(text="\"Ixlos Shifo Farm \" dorixonasi")
async def send_chemist29(message:Message):
    await message.answer("Manzil: Navoiy ko'chasi\n Mo'ljal: Sardoba hududida\n Tel:+998 --------\n Ish vaqti: 24/7 ")

@dp.message_handler(text="\"Jo'rabek Aziz Shifo\" dorixonasi")
async def send_chemist30(message:Message):
    await message.answer("Manzil: G'irvonsoy ko'chasi, 14-uy\n Hamkorbank yonida\n Tel:+998 69 228 71 23\n Ish vaqti: 24/7")

@dp.message_handler(text="\"Inter Farm Servis\" dorixonasi")
async def send_chemist31(message:Message):
    await message.answer("Manzil: Boburshox ko'chasi\n Tel:+998 97 480 30 95\n Ish vaqti: 24/7")

@dp.message_handler(text="\"Kelajak Fayz Med Farm\" dorixonasi")
async def send_chemist31(message:Message):
    await message.answer("Manzil: Qo'qon ko'chasi\n Mo'ljal: Isfarxon hududida\n Tel:+998 94 275 77 75\n Ish vaqti: 24/7")

@dp.message_handler(text="\"Malinka\" dorixonasi")
async def send_chemist32(message:Message):
    await message.answer("Manzil: Go'zal ko'chasi, 55-uy\n Ish vaqti: 24/7")

@dp.message_handler(text="◀ Ortga", state="*")
async def send_back(message:Message, state=FSMContext):
    await message.answer("Ortga", reply_markup=menuStart)
    await state.finish()

@dp.message_handler(text="Apteka Yupiter")
async def send_chemist32(message:Message):
    await message.answer("Manzil: Ququmboy ko'chasi, \"Abbos\" supermarketi oldida\n Ish vaqti: 24/7")

@dp.message_handler(text="MuhammadFarmServis")
async def send_chemist32(message:Message):
    await message.answer("Manzil: Ququmboy ko'chasi, Torro Grill yonida\n Ish vaqti: 24/7")

@dp.message_handler(text="Sado Farm")
async def send_chemist32(message:Message):
    await message.answer("Manzil: 5-oila poliklinasi oldida\n Ish vaqti: 24/7")

@dp.message_handler(text="Piramida dorixonasi")
async def send_chemist32(message:Message):
    await message.answer("Manzil: G'alaba ko'chasi, Makro supermarketi oldida\n Ish vaqti: 24/7")

@dp.message_handler(text="Muovazin dorixonasi")
async def send_chemist32(message:Message):
    await message.answer("Manzil: G'alaba ko'chasi, \"Bonanza\" mini marketi yonida\n Ish vaqti: ---")

@dp.message_handler(text="Apteka 24/7")
async def send_chemist32(message:Message):
    await message.answer("Manzil: G'alaba ko'chasi, AvtoGold avtomaktab yonida\n Ish vaqti: 24/7")









