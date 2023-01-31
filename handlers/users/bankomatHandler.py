from aiogram.dispatcher.filters import Text, Command
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, Message
from loader import dp, bot
from keyboards.default.menuKeyboard import menuBankomat, menuStart 
from keyboards.default.namangan_shahar import nshahar, davlatobod
from states.locstates import locstates
from aiogram.dispatcher import FSMContext

@dp.message_handler(text="Namangan sh - 102 ta", state=locstates.bankomat)
async def send_nam(message:Message, state=FSMContext):
    await message.answer("Namangan shahar tanlandi", reply_markup=nshahar)
    await state.finish()

@dp.message_handler(text="Davlatobod t - 41 ta", state=locstates.bankomat)
async def send_o(message:Message, state=FSMContext):
    await message.answer("Davlatobod tumani tanlandi", reply_markup=davlatobod)
    await state.finish()


# @dp.message_handler(text="Yangi Namangan t - 18 ta")
# async def send_n(message:Message):
#     await message.answer("Yangi Namangan tumani tanlandi", reply_markup=nshahar)

# @dp.message_handler(text="Namangan t - 19 ta")
# async def send_m(message:Message):
#     await message.answer("Namangan tumani tanlandi", reply_markup=nshahar)

# @dp.message_handler(text="To'raqo'rg'on t - 34 ta")
# async def send_l(message:Message):
#     await message.answer("To'raqo'rg'on tumani tanlandi", reply_markup=nshahar)

# @dp.message_handler(text="Mingbuloq t - 18 ta")
# async def send_k(message:Message):
#     await message.answer("Mingbuloq tumani tanlandi", reply_markup=nshahar)

# @dp.message_handler(text="Kosonsoy t - 21 ta")
# async def send_j(message:Message):
#     await message.answer("Kosonsoy tumani tanlandi", reply_markup=nshahar)

# @dp.message_handler(text="Pop t - 30 ta")
# async def send_h(message:Message):
#     await message.answer("Pop tumani tanlandi", reply_markup=nshahar)

# @dp.message_handler(text="Norin t - 17 ta")
# async def send_g(message:Message):
#     await message.answer("Norin tumani tanlandi", reply_markup=nshahar)

# @dp.message_handler(text="Uychi t - 31 ta")
# async def send_f(message:Message):
#     await message.answer("Uychi tumani tanlandi", reply_markup=nshahar)

# @dp.message_handler(text="Chortoq t - 20 ta")
# async def send_e(message:Message):
#     await message.answer("Chortoq tumani tanlandi", reply_markup=nshahar)

# @dp.message_handler(text="Chust t - 27 ta")
# async def send_d(message:Message):
#     await message.answer("Chust tumani tanlandi", reply_markup=nshahar)

# @dp.message_handler(text="Uchqo'rg'on t - 30 ta")
# async def send_c(message:Message):
#     await message.answer("Uchqo'rg'on tumani tanlandi", reply_markup=nshahar)

# @dp.message_handler(text="Yangiqo'rg'on t - 17 ta")
# async def send_a(message:Message):
#     await message.answer("Yangiqo'rg'on tumani tanlandi", reply_markup=nshahar)

@dp.message_handler(text="🔙 Ortga.")
async def send_b(message:Message):
    await message.answer("Ortga", reply_markup=menuBankomat)
    await locstates.bankomat.set()

@dp.message_handler(text="🔙 Ortga", state="*")
async def send_100(message:Message, state=FSMContext):
    await message.answer("Ortga", reply_markup=menuStart)
    await state.finish()

@dp.message_handler(text="Boburshox ko'chasi/HUMO")
async def send_1(message:Message):
    await message.answer("Manzil: Boburshox ko'chasi, Roddom ichida\n Agrobank\n tel:+998 88 231 20 02\n       +998 94 504 57 77")

@dp.message_handler(text="A.Navoiy ko'chasi 32-uy/HUMO")
async def send_2(message:Message):
    await message.answer("Manzil: A.Navoiy ko'chasi, DSI binosi ichida\n Agrobank\n tel:+998 88 231 20 02\n       +998 94 504 57 77")

@dp.message_handler(text="Boburshox ko'chasi, 1-uy/HUMO va Uzcard")
async def send_3(message:Message):
    await message.answer("Manzil: Lola BXM, Doktor A shifoxonasi yonida\n Agrobank\n tel:+998 88 231 20 02\n       +998 94 504 57 77")

@dp.message_handler(text="Zirabuloq ko'chasi, 12-uy/HUMO va Uzcard")
async def send_4(message:Message):
    await message.answer("Manzil: Chorsu BXM\n Agrobank\n tel:+998 88 231 20 02\n       +998 94 504 57 77")

@dp.message_handler(text="Uychi ko'chasi, Chorsu bank xizmatlari markazi/HUMO")
async def send_5(message:Message):
    await message.answer("Manzil: Chorsu mehmonxonasi ro'parasida\n Aloqa bank\n tel:+998 97 212 55 40")

@dp.message_handler(text="To'raqo'rg'on ko'chasi 75-uy/HUMO va Uzcard")
async def send_6(message:Message):
    await message.answer("Manzil: Aloqa bank binosida\n Aloqa bank\n tel:+998 97 212 55 40")

@dp.message_handler(text="A.Navoiy ko'chasi, 27-uy/HUMO va Uzcard")
async def send_7(message:Message):
    await message.answer("Manzil: Asaka bank binosida\n Asaka bank\n tel:+998 90 214 77 84")

@dp.message_handler(text="Chorsu dehqon bozori/HUMO va Uzcard")
async def send_8(message:Message):
    await message.answer("Manzil: Chorsu bozori oldidagi avtoturargoh\n Asaka bank\n tel:+998 90 214 77 84")

@dp.message_handler(text="A.Navoiy ko'chasi/HUMO va Uzcard")
async def send_9(message:Message):
    await message.answer("Manzil: Chorsu bozori yonida\n Turon bank\n tel:+998 94 271 55 77")

@dp.message_handler(text="Nodira ko'chasi/Uzcard")
async def send_10(message:Message):
    await message.answer("Manzil: Megapolis supermarketi\n Infin bank\n tel:+998 91 368 22 00")

@dp.message_handler(text="Nodira ko'chasi 4-uy/HUMO va Uzcard")
async def send_11(message:Message):
    await message.answer("Manzil: Infin bank binosida\n Infin bank\n tel:+998 91 368 22 00")

@dp.message_handler(text="Lola massivi/HUMO")
async def send_12(message:Message):
    await message.answer("Manzil: Best market ro'parasida\n Xalq bank\n tel:+998 99 302 11 77")

@dp.message_handler(text="Navoiy ko'chasi, Sardoba bozori/HUMO va Uzcard")
async def send_13(message:Message):
    await message.answer("Manzil: Megapolis supermarketi\n Ipak yo'li bank\n tel:+998 97 250 14 51")

@dp.message_handler(text="A.Navoiy ko'chasi 63-uy/HUMO va Uzcard")
async def send_14(message:Message):
    await message.answer("Manzil: Ipoteka banki binosi oldida\n Ipoteka bank\n tel:+998 91 360 35 55")

@dp.message_handler(text="A.Temur ko'chasi, 5-uy/HUMO")
async def send_15(message:Message):
    await message.answer("Manzil: Grand Sherdor mehmonxonasi\n Ipoteka bank\n tel:+998 91 360 35 55")

@dp.message_handler(text="N.Nomongoniy ko'chasi/Humo va Uzcard")
async def send_16(message:Message):
    await message.answer("Manzil: Nomongoniy ko'chasi 27-uy\n Kapitalbank\n tel:+998 93 916 19 94")

@dp.message_handler(text="Uychi ko'chasi, Gisht koprik/Uzcard")
async def send_17(message:Message):
    await message.answer("Manzil: G'isht koprik Dorixona binosi oldida\n Kapitalbank\n tel:+998 93 916 19 94")

@dp.message_handler(text="Jahon bozori hududida/UzCard")
async def send_18(message:Message):
    await message.answer("Manzil: Jahon bozori ma'muriyat binosi oldida\n Kapitalbank\n tel:+998 93 916 19 94")

@dp.message_handler(text="Xamza aylanma yo'li/UzCard")
async def send_18(message:Message):
    await message.answer("Manzil: Shanxai bio med dorixonasi oldida\n Kapitalbank\n tel:+998 93 916 19 94")

@dp.message_handler(text="Uychi ko'chasi, 137-uy/UzCard")
async def send_18(message:Message):
    await message.answer("Manzil: Chorsu, G'uncha petak, 202-dorixona binosi oldida\n Kapitalbank\n tel:+998 93 916 19 94")

@dp.message_handler(text="A.Temur ko'chasi, 5-uy/UzCard")
async def send_18(message:Message):
    await message.answer("Manzil: Texnopark yonida apteka binosida\n Kapitalbank\n tel:+998 93 916 19 94")

@dp.message_handler(text="A.Navoiy ko'chasi, 31-uy/UzCard")
async def send_18(message:Message):
    await message.answer("Manzil: Isfarxon supermarketi ichida\n Kapitalbank\n tel:+998 93 916 19 94")

@dp.message_handler(text="Boburshox ko'chasi, 178-uy/UzCard")
async def send_18(message:Message):
    await message.answer("Manzil: Lola, Milliy savdo markazi oldida\n Kapitalbank\n tel:+998 93 916 19 94")

@dp.message_handler(text="Navoiy ko'chasi, 70a-uy/Humo va Uzcard")
async def send_18(message:Message):
    await message.answer("Manzil: Qishloq qurilish bank ofisi\n Qishloq qurilish bank\n tel:+998 91 354 48 88")

@dp.message_handler(text="Uychi ko'chasi, Globus2 dorixona oldida/UzCard")
async def send_18(message:Message):
    await message.answer("Manzil: Globus dorixonasi oldida\n Kapitalbank\n tel:+998 93 916 19 94")

@dp.message_handler(text="Ibrat ko'chasi/HUMO")
async def send_18(message:Message):
    await message.answer("Manzil: Bilayn bosh ofisi oldida\n Markaziy bank\n tel:+998 69 227 05 12")

@dp.message_handler(text="Samarqand ko'chasi/HUMO")
async def send_19(message:Message):
    await message.answer("Manzil: Chorsu dehqon bozori hududida\n Markaziy bank\n tel:+998 69 227 05 12")

@dp.message_handler(text="A.Xo'jayev ko'chasi, Namangan DXM/HUMO")
async def send_20(message:Message):
    await message.answer("Manzil: 31-maktab ro'parasida\n Markaziy bank\n tel:+998 69 227 05 12")

@dp.message_handler(text="B.Mashrab ko'chasi,12-uy/HUMO")
async def send_21(message:Message):
    await message.answer("Manzil: Xalq ta'limi shahar bo'limi\n Markaziy bank\n tel:+998 69 227 05 12")

@dp.message_handler(text="Namagan viloyat hokimligi binosida/HUMO")
async def send_22(message:Message):
    await message.answer("Manzil: NamDU orqasida\n Markaziy bank\n tel:+998 69 227 05 12")

@dp.message_handler(text="Navoiy ko'chasi, 1-oila poliklinikasi oldida/UzCard va HUMO")
async def send_23(message:Message):
    await message.answer("Manzil: Namangan viloyat gaz ta'minoti oldida\n Savdogarbank\n tel:+998 93 407 20 55")

@dp.message_handler(text="Zirabuloq ko'chasi,Chorsu hududi/UzCard va HUMO")
async def send_24(message:Message):
    await message.answer("Manzil: Chorsu 7 etajli uy oldida\n Savdogarbank\n tel:+998 93 407 20 55")

@dp.message_handler(text="Nodira ko'chasi/HUMO va Uzcard")
async def send_25(message:Message):
    await message.answer("Manzil: Trastbank yangi binosi oldida\n Trastbank\n tel:+998 93 943 66 36")

@dp.message_handler(text="Marg'ilon ko'chasi,92-uy/ HUMO")
async def send_26(message:Message):
    await message.answer("Manzil: Viloyat hududiy elektr tarmoqlari binosida, Bobur bog'i ro'parasida\n Sanoat qurilish bank\n tel:+998 94 711 16 68")

@dp.message_handler(text="Qo'qon ko'chasi,5-uy/ HUMO va UzCard")
async def send_27(message:Message):
    await message.answer("Manzil: Sardoba bozori ro'parasida\n Trastbank\n tel:+998 93 943 66 36")

@dp.message_handler(text="B.Mashrab, 62-uy/UzCard")
async def send_28(message:Message):
    await message.answer("Manzil: Bilayn ofisi oldida\n Trastbank\n tel:+998 93 943 66 36")

@dp.message_handler(text="Xamroh(Oxunboboyev) ko'chasi,68-uy/ HUMO va UzCard")
async def send_29(message:Message):
    await message.answer("Manzil: Turon bank binosida\n Turon bank\n tel:+998 94 271 55 77")

@dp.message_handler(text="Uychi ko'chasi/HUMO va UzCard")
async def send_30(message:Message):
    await message.answer("Manzil: Chorsu mehmonxonasi ro'parasida\n Turon bank\n tel:+998 94 271 55 77")

@dp.message_handler(text="Boburshox ko'chasi,13-uy/HUMO va UzCard")
async def send_31(message:Message):
    await message.answer("Manzil: Odil Fayz klinikasi yonida \n Turon bank\n tel:+998 94 271 55 77")

@dp.message_handler(text="A.Temur ko'chasi, 97-uy/HUMO va UzCard")
async def send_32(message:Message):
    await message.answer("Manzil: Temir yo'l vokzali ro'parasida, Oydin plaza mehmonxonasi\n tel:+998 99 302 11 77")

@dp.message_handler(text="Lutfiy ko'chasi,5-uy/HUMO va UzCard")
async def send_33(message:Message):
    await message.answer("Manzil: Xalq banki binosi oldida\n Xalq bank\n tel:+998 99 302 11 77")

@dp.message_handler(text="Uychi ko'chasi, G'ishtkoprik bekati/HUMO")
async def send_34(message:Message):
    await message.answer("Manzil: G'isht koprik bekatida\n Xalq bank\n tel:+998 99 302 11 77")

@dp.message_handler(text="A.Temur ko'chasi,110-uy/HUMO va Uzcard")
async def send_35(message:Message):
    await message.answer("Manzil: Hamkorbank bank ofisi 24/7\n Hamkorbank\n tel:+998 93 264 90 09")

@dp.message_handler(text="Istiqlol ko'chasi/HUMO va UzCard")
async def send_36(message:Message):
    await message.answer("Manzil: NamDU kirish qismida\n Hamkorbank\n tel:+998 93 264 90 09")

@dp.message_handler(text="A.Navoiy ko'chasi,31-uy/HUMO va UzCard")
async def send_37(message:Message):
    await message.answer("Manzil: Xamkorbank Yuksalish ofisi oldida\n Xamkorbank\n tel:+998 91 347 10 07")

@dp.message_handler(text="Uychi ko'chasi,3-uy/ HUMO va UzCard")
async def send_38(message:Message):
    await message.answer("Manzil: Chorsu Hamkorbank BXM\n Hamkorbank\n tel:+998 91 347 10 07")

@dp.message_handler(text="Boburshox ko'chasi,11-uy/ HUMO va UzCard")
async def send_39(message:Message):
    await message.answer("Manzil: Hamkorbank lola minibank\n Hamkorbank\n tel:+998 91 347 10 07")

@dp.message_handler(text="G'alabaning 50 yilligi ko'chasi, 19-uy/ HUMO va UzCard")
async def send_40(message:Message):
    await message.answer("Manzil: Agrobank Davlatobod filiali\n Agrobank\n tel:+998 88 231 20 02\n       +998 94 504 57 77")

@dp.message_handler(text="Yuksalish dahasi/ HUMO va UzCard")
async def send_41(message:Message):
    await message.answer("Manzil: Yuksalish dahasi 24/7\n Agrobank\n tel:+998 88 231 20 02\n       +998 94 504 57 77")

@dp.message_handler(text="Sportchilar ko'chasi/ UzCard")
async def send_42(message:Message):
    await message.answer("Manzil: Sanam chevarxonasi oldida\n Agrobank\n tel:+998 88 231 20 02\n       +998 94 504 57 77")

@dp.message_handler(text="I.Karimov ko'chasi/UzCard")
async def send_43(message:Message):
    await message.answer("Manzil: Yashil bozor darvozasi oldida\n Aloqabank\n tel:+998 97 212 55 40")

@dp.message_handler(text="Sportchilar ko'chasi 53-uy/UzCard")
async def send_44(message:Message):
    await message.answer("Manzil: Milliy gvardiya binosi ichida (Otchopar)\n Ipoteka bank\n tel:+998 91 360 35 55")

@dp.message_handler(text="G'alaba ko'chasi, 2-uy/ HUMO va UzCard")
async def send_45(message:Message):
    await message.answer("Manzil: Ipak yo'li banki binosi\n Ipak yo'li bank\n tel:+998 97 250 14 51")

@dp.message_handler(text="5-kichik tuman/ HUMO va UzCard")
async def send_46(message:Message):
    await message.answer("Manzil: Ishonch do'koni pastrog'ida\n Ipoteka bank BXM\n tel:+998 91 360 35 55")

@dp.message_handler(text="5A-kichik tuman/ UzCard")
async def send_47(message:Message):
    await message.answer("Manzil: Tegen savdo markazi ro'parasida, Karamel savdo do'koni\n Kapital bank\n tel:+998 93 916 19 94")

@dp.message_handler(text="I.Karimov ko'chasi 11-uy/UzCard")
async def send_48(message:Message):
    await message.answer("Manzil: Istiqlol mehmonxonasi\n Kapital bank\n tel:+998 93 916 19 94")

@dp.message_handler(text="I.Karimov ko'chasi/UzCard")
async def send_49(message:Message):
    await message.answer("Manzil: Tennis kort ro'parasida\n Kapitalbank\n tel:+998 93 916 19 94")

@dp.message_handler(text="6-kichik tuman/ UzCard")
async def send_50(message:Message):
    await message.answer("Manzil: Makro supermarketi binosida\n Kapitalbank\n tel:+998 93 916 19 94")

@dp.message_handler(text="6-kichik tuman/ HUMO")
async def send_51(message:Message):
    await message.answer("Manzil: Makro supermarketi binosida\n Qishloq qurilish bank\n tel:+998 91 354 48 88")

@dp.message_handler(text="Shishaki MFY/ UzCard")
async def send_52(message:Message):
    await message.answer("Manzil: Irvadon supermarketi\n Kapitalbank\n tel:+998 93 916 19 94")

@dp.message_handler(text="Nurobod MFY/ UzCard")
async def send_53(message:Message):
    await message.answer("Manzil: Tvix savdo do'koni\n Kapitalbank\n tel:+998 93 916 19 94")

@dp.message_handler(text="To'raqo'rg'on ko'chasi/ HUMO va UzCard")
async def send_54(message:Message):
    await message.answer("Manzil: G'irvon bozori hududida\n Qishloq qurilish bank\n tel:+998 91 354 48 88")

@dp.message_handler(text="Viloyat ko'p tarmoqli bolalar tibbiyot markazi/ HUMO")
async def send_55(message:Message):
    await message.answer("Manzil: Irvadon shifoxonasi\n Markaziy bank\n tel:+998 *******")

@dp.message_handler(text="Namangan muhandislik-texnologiya instituti/ HUMO")
async def send_56(message:Message):
    await message.answer("Manzil: NamMTI binosida\n Markaziy bank\n tel:+998 *********")

@dp.message_handler(text="Ququmboy shox ko'chasi 7a-uy/ HUMO va UzCard")
async def send_57(message:Message):
    await message.answer("Manzil: 17-avtobaza yonida\n Mikrokreditbank\n tel:+998 91 367 36 36")

@dp.message_handler(text="I.Karimov ko'chasi 2-uy/ HUMO va UzCard")
async def send_58(message:Message):
    await message.answer("Manzil: Milliy bank ofisi\n Milliy bank\n tel:+998 99 535 33 73\n       +998 93 925 57 77")

@dp.message_handler(text="To'qimachilar ko'chasi/ HUMO")
async def send_59(message:Message):
    await message.answer("Manzil: Namangan to'qimachi MCHJ binosida\n Milliy bank\n tel:+998 99 535 33 73\n       +998 93 925 57 77")

@dp.message_handler(text="I.Karimov ko'chasi (Aeroport)/ HUMO va UzCard")
async def send_60(message:Message):
    await message.answer("Manzil: Namangan Aeroporti binosida\n Milliy bank\n tel:+998 99 535 33 73\n       +998 93 925 57 77")

@dp.message_handler(text="Navoiy ko'chasi, Megapolis savdo markazi/HUMO")
async def send_60(message:Message):
    await message.answer("Manzil: Megapolis savdo markazi binosida\nMarkaziy bank\ntel:+998 69 227 05 12")

@dp.message_handler(text="I.Karimov ko'chasi (Afsonalar bog'i)/ HUMO va UzCard")
async def send_61(message:Message):
    await message.answer("Manzil: Afsonalar bog'i\n Milliy bank\n tel:+998 99 535 33 73\n       +998 93 925 57 77")

@dp.message_handler(text="Xotira ko'chasi, 1-uy/ HUMO va UzCard")
async def send_62(message:Message):
    await message.answer("Manzil: Qal'a bekati atrofida\n Trastbank\n tel:+998 93 943 66 36")

@dp.message_handler(text="Namagan Aeroport/ HUMO")
async def send_63(message:Message):
    await message.answer("Manzil: Namangan Aeroporti binosi ichida\n Trast bank\n tel:+998 93 943 66 36")

@dp.message_handler(text="Ququmboy shox ko'chasi 40a-uy/ HUMO va UzCard")
async def send_64(message:Message):
    await message.answer("Manzil: Turon bank mini ofisi (Koson petak)\n Turon bank")

@dp.message_handler(text="I.Karimov ko'chasi 2-kichik tuman/ HUMO")
async def send_64(message:Message):
    await message.answer("Manzil: Istiqlol mehmonxonasi\n Xalq bank\n tel:+998 99 302 11 77")

@dp.message_handler(text="⬅ Ortga")
async def send_64(message:Message):
    await message.answer("Ortga", reply_markup=menuBankomat)
    await locstates.bankomat.set()
    



