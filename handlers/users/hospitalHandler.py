from aiogram.dispatcher.filters import Text, Command
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, Message
from loader import dp, bot
from keyboards.default.shahar_shifoxona import shaharShifo
from keyboards.default.menuKeyboard import menuStart
from states.locstates import locstates
from aiogram.dispatcher import FSMContext

@dp.message_handler(text="NAMANGAN SHAHAR BOLALAR SHIFOXONASI", state="*")
async def send_agronam(message:Message, state=FSMContext):
    
    file_id = 'AgACAgIAAxkBAAODY7PgeEPKVG4N8qJrUvtzKeEr1IkAArHAMRsTBKFJUYd2M-OcX7UBAAMCAAN4AAMtBA'
    
    text = "<b>NAMANGAN SHAHAR BOLALAR SHIFOXONASI</b>\n"
    text += "Manzil: Go'zal dahasi 4-uy\n"
    text += "Mo'ljal: Go'zal shifoxonasi orqasida\n Tel: +998 69 237 16 48, +998 69 237 10 43\n"
    text += "Ish tartibi: 24/7"
    
    await message.answer_location(latitude="41.00796883587812", longitude=" 71.62345267916557")        
    await message.reply_photo(file_id, caption=text)
    await state.finish()
    
@dp.message_handler(text="NAMANGAN VILOYATINING YUQUMLI KASALLIKLAR SHIFOXONASI", state="*")
async def send_sanoat(message:Message, state=FSMContext):
    
    file_id = 'AgACAgIAAxkBAAICAAFjs-3qLQJdT53wFPYrdcCIfihjvQACr8AxGxMEoUmGWODg3mWa9QEAAwIAA3gAAy0E'
    
    text = "<b>NAMANGAN VILOYATINING YUQUMLI KASALLIKLAR SHIFOXONASI</b>\n"
    text += "Manzil: K.Otamirzayev ko'chasi 90-uy\n"
    text += "Mo'ljal: Doctor A xususiy klinikasi\nTel: +998 69 224 73 58, +998 69 224 69 15\n"
    text += "Ish tartibi: 24/7"
    
    await message.answer_location(latitude="40.99052274911174", longitude="71.70909736965017")        
    await message.reply_photo(file_id, caption=text)
    await state.finish() 

@dp.message_handler(text="RESPUBLIKA IXTISOSLASHTIRILGAN AKUSHERLIK VA GINEKOLOGIYA ILMIY - AMALIY TIBBIYOT MARKAZINING NAMANGAN FILIALI", state="*")
async def send_ipa(message:Message, state=FSMContext):
    
    file_id = 'AgACAgIAAxkBAAICAmOz7q-dEpQD7rziz3mm8QGvKNU1AAKuwDEbEwShSeMcnOf57i9tAQADAgADbQADLQQ'
    
    text = "<b>Respublika Ixtisoslashtirilgan Akusherlik va Ginekologiya Ilmiy-Amaliy Tibbiyot Markazi Namangan Filiali</b>\n"
    text += "Manzil: Boburshox ko'chasi 143A-uy\n"
    text += "Mo'ljal: Yuqumli kasalliklar shifoxonasi\nTel: +998 69 239 38 03\n"
    text += "Ish tartibi: Dushanbadan-Jumagacha 07:00-19:00, tushliksiz"
    
    await message.answer_location(latitude="40.99535848695003", longitude="71.64694200841065")        
    await message.reply_photo(file_id, caption=text)
    await state.finish()

@dp.message_handler(text="NAMANGAN VILOYAT KO'P TARMOQLI TIBBIYOT MARKAZI", state="*")
async def send_hamkor(message:Message, state=FSMContext):
    
    file_id = 'AgACAgIAAxkBAAIB5WOz7YyBRvHnmhfnFmWBPziix8dfAAKwwDEbEwShSZdycp0AASprrQEAAwIAA3kAAy0E'
    
    text = "<b>Namangan viloyat ko'p tarmoqli tibbiyot markazi</b>\n"
    text += "Manzil: Nomongoniy ko'chasi 9-uy\n"
    text += "Mo'ljal: Sayhun mehmonxonasi\nTel: +998 69 226 20 04, +998 69 226 36 00\n"
    text += "Ish tartibi: Dushanbadan-Shanbagacha 09:00-18:00, tushliksiz"
    
    await message.answer_location(latitude="41.00393608604384", longitude="71.66104554126807")        
    await message.reply_photo(file_id, caption=text)
    await state.finish()

@dp.message_handler(text="ANGIOMED", state="*")
async def send_asaka(message:Message, state=FSMContext):
    
    file_id = 'AgACAgIAAxkBAAN2Y7PgdVeL6gVp1LM66BEMahkbETwAAqXAMRsTBKFJAAE8C2H-sFFjAQADAgADeAADLQQ'
    
    text = "<b>ANGIOMED</b>\n"
    text += "Manzil: I.Karimov ko'chasi\nTel: +998 78 888 00 01\n"
    text += "Mo'ljal: Namangan mehmonxonasi, NBU bank oldida\n"
    text += "Ish tartibi: Dushanbadan-Shanbagacha 09:00-18:00"
    
    await message.answer_location(latitude="40.99625761004835", longitude="71.58655921917563")        
    await message.reply_photo(file_id, caption=text)
    await state.finish()

@dp.message_handler(text="Rano medical center", state="*")
async def send_infin(message:Message, state=FSMContext):
    
    file_id = 'AgACAgIAAxkBAAIByGOz7J_NiUUyyNEZGijae-brSbz1AALNwDEbEwShSZMcdoMKIv1ZAQADAgADeAADLQQ'
    
    text = "<b>Rano medical center</b>\n"
    text += "Manzil: I.Karimov ko'chasi\nTel: +998 69 232 90 09\n"
    text += "Mo'ljal: Al-mashriq oshxonasi yonida\n"
    text += "Ish tartibi: Dushanbadan-Shanbagacha 09:00-18:00"
    
    await message.answer_location(latitude="40.99639110137484", longitude="71.59026379416488")        
    await message.reply_photo(file_id, caption=text)
    await state.finish()

@dp.message_handler(text="HABIB shifoxonasi", state="*")
async def send_trast(message:Message, state=FSMContext):
     
    file_id = 'AgACAgIAAxkBAAIB42Oz7YNyr9cAAXVwRA9VTKHU55IVFQACz8AxGxMEoUlaoFyF8S2X-QEAAwIAA3gAAy0E'
    
    text = "<b>HABIB shifoxonasi</b>\n"
    text += "Manzil: Xotira ko'chasi 5-uy\nTel: +998 90 555 52 25\n"
    text += "Mo'ljal: 5-oila poliklinasi oldida\n"
    text += "Ish tartibi: Dushanbadan-Shanbagacha 09:00-17:00"
    
    await message.answer_location(latitude="41.00063794372812", longitude="71.61002748966733")        
    await message.reply_photo(file_id, caption=text)
    await state.finish()

@dp.message_handler(text="5-oila poliklinasi", state="*")
async def send_mikro(message:Message, state=FSMContext):
    
    file_id = 'AgACAgIAAxkBAAIBxmOz69xtmNWu3EjITrxw_2v5-9-GAAKtwDEbEwShSVvGznXCO8VnAQADAgADeQADLQQ'
    
    text = "<b>5-oila poliklinasi</b>\n"
    text += "Manzil: Xotira ko'chasi 71A, 5A-kichik noxiya \nTel: +998 69 232 50 71\n"
    text += "Mo'ljal: Koson petak tarafda"
    text += "Ish tartibi: Dushanbadan-Shanbagacha 08:00-20:00"
    
    await message.answer_location(latitude="41.000552061203145", longitude="71.61042198414846")        
    await message.reply_photo(file_id, caption=text)
    await state.finish()

@dp.message_handler(text="Galomed", state="*")
async def send_ipak(message:Message, state=FSMContext):
    
    file_id = 'AgACAgIAAxkBAANzY7PgdNYMb8q8Y-zz2tQDRv9AGJ4AAqTAMRsTBKFJTpIrB-oPCwQBAAMCAANtAAMtBA'
    
    text = "<b>Galomed</b>\n"
    text += "Manzil: 1-kichik noxiya, Sportchilar ko'chasi \nTel: +998 95 307 00 70\n"
    text += "Mo'ljal: 56-maktab oldida\n"
    text += "Ish tartibi: Dushanbadan-Jumagacha 08:00-20:00"
    
    await message.answer_location(latitude="41.003701653981", longitude="71.59076202766865")        
    await message.reply_photo(file_id, caption=text)
    await state.finish()

@dp.message_handler(text="\"ZZZ\" ko'z klinikasi", state="*")
async def send_nbu(message:Message, state=FSMContext):
    
    file_id = 'AgACAgIAAxkBAAMcY7PfV-iWrxClRzxhoJeO0c2UUQYAAo3AMRsTBKFJo0KrcOgQjmkBAAMCAAN5AAMtBA'
    
    text = "<b>\"ZZZ\" ko'z klinikasi</b>\n"
    text += "Manzil: 2-kichik noxiya \n"
    text += "Mo'ljal: 1-shahar roddom, \"Navbahor\" stadioni \nTel: +998 69 232 91 63"
    text += "Ish tartibi: Dushanbadan-Jumagacha 09:00-16:00, Shanba - 08:00-14:00"
    
    await message.answer_location(latitude="41.000267811219075", longitude="71.58959532489571")        
    await message.reply_photo(file_id, caption=text)
    await state.finish()

# @dp.message_handler(text="G'ishtli bolnitsa", state=locstates.hospital)
# async def send_nbu(message:Message, state=FSMContext):
    
#     file_id = ''
    
#     text = "<b>G'ishtli bolnitsa</b>\n"
#     text += "Manzil: 2-kichik noxiya\n"
#     text += "Mo'ljal: \"ZZZ\" ko'z klinikasi oldida\nTel: +998 -------"
#     text += "Ish tartibi: Dushanbadan-Shanbagacha 08:00-19:00"
    
#     await message.answer_location(latitude="41.000591816121926", longitude="71.5901996191277")        
#     await message.reply_photo(file_id, caption=text)
#     await state.finish()

@dp.message_handler(text="👈 Ortga", state="*")
async def back_hos(message:Message, state=FSMContext):
    await message.answer("Ortga", reply_markup=menuStart)
    await state.finish()

