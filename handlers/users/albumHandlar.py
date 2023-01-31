from loader import dp, bot
from aiogram.types import InputFile, Message, MediaGroup
from aiogram.dispatcher.filters import Command
from keyboards.inline.search_bank import search_bank, search_hos
from keyboards.inline.search_bankomat import search_bankomat, search_chemist
from loader import dp, bot
from states.locstates import locstates

@dp.message_handler(text="Banklar")
async def send_bank(message: Message):

	file_id = 'AgACAgIAAxkBAAOxY7PoOtCDMsIrB-6VpeQQ6QfEECIAAsHAMRsTBKFJ1YI7Dd-MYMYBAAMCAAN5AAMtBA'
	
	text = "<b>Banklar bo'limini tanladingiz</b> \n"
	text += "Bu bo'lim orqali o'zingizga uchun eng yaqin bo'lgan bankni topishingiz mumkin\n"
	text += "Siz quyidagi banklarni ko'rishingiz mumkin:\n"
	text += "👉 NBU bank\n👉 Agrobank\n👉 Bank Ipak Yo'li\n👉 Mikrokreditbank\n👉 Trastbank mini banki\n👉 Agrobank Namangan filiali\n👉 O'zsanoatqurilish bank\n👉 Ipak yo'li banki Namangan filiali"
	
	await message.reply_photo(file_id, caption=text, reply_markup=search_bank)
	await locstates.bank.set()
	
@dp.message_handler(text="Bankomatlar")
async def send_bankomat(message: Message):
	file_id = 'AgACAgIAAxkBAAOUY7PmbvHa5ozSDFKxMznkmVs5x_sAAuTFMRtjjaBJZlS-tfIwSdQBAAMCAAN5AAMtBA'

	text = "<b>Bankomatlar bo'limini tanladingiz</b> \n"
	text += "Bu bo'lim orqali o'zingizga eng yaqin bankomatni topishingiz mumkin"
	await message.reply_photo(file_id, caption=text, reply_markup=search_bankomat)
	await locstates.bankomat.set()

@dp.message_handler(text="Shifoxonalar")
async def send_hospital(message: Message):

	file_id = 'AgACAgIAAxkBAANDY7PgaYCoyzzQY2tL_8yp1xTcaWsAApLAMRsTBKFJOauBk5y9WsMBAAMCAAN5AAMtBA'
	
	text = "<b>Shifoxonalar bo'limini tanladingiz</b> \n"
	text += "Bu bo'lim orqali o'zingiz uchun eng yaqin bo'lgan shifoxonani topishingiz mumkin\n"
	
	await message.reply_photo(file_id, caption=text, reply_markup=search_hos)
	await locstates.hospital.set()

@dp.message_handler(text="Dorixonalar")
async def send_chemist(message: Message):

	file_id = 'AgACAgIAAxkBAAOZY7Pmx7wPPt59_J12zgTHlrBI26MAAuLFMRtjjaBJpQVT4poZKCwBAAMCAAN4AAMtBA'
	
	text = "<b>Dorixonalar bo'limini tanladingiz</b> \n"
	text += "Bu bo'lim orqali o'zingiz uchun eng yaqin bo'lgan dorixonani topishingiz mumkin\n"
	text += "Siz Namangan hududidagi dorixonalarni ko'rishingiz mumkin:\n"
	
	await message.reply_photo(file_id, caption=text, reply_markup=search_chemist)
	await locstates.chemist.set()

@dp.message_handler(text="Qo'llanma")
async def send_qollanma(message: Message):

	text = "<b>Banklar va bankomatlar, Shifoxonalar va dorixonalar</b>\n\n"
	text += "Bu bot orqali o'zingizga eng yaqin bo'lgan bank va bankomatlar, Shifoxona va dorixonalar ro'yxati, Davlat xizmatlari markazini topishingiz mumkin\n"
	text += "Botdan foydalanish uchun o'zingizga kerakli bo'limni tanlab o'zingiz turgan joyingizni yuboring va bot orqali o'zingizga eng yaqin bo'lgan bank va shifoxonani topa olasiz "
	text += "Bu bot @Mr_Azimboy tomonidan yasalgan"
	
	await message.answer(text)

# @dp.message_handler(text='📍Joylashuv')
# async def get_contact(message: types.Message):
#        await message.answer_location(latitude="40.994657983152365",
#                                       longitude=" 71.6048352815629")
#        await message.answer("Bizning lokatsiyamiz")

@dp.message_handler(text="Davlat xizmatlari markazi \n(Namangan shahar)")
async def send_sanoat(message:Message):
    
	file_id = 'AgACAgIAAxkBAANwY7PgcxwNlYaa4v_ya-ZQxr1CPjwAAqrAMRsTBKFJ6z3JRmPscvIBAAMCAAN5AAMtBA'
	
	text = "<b>Davlat xizmatlari markazi (Namangan shahar)</b>\n"
	text += "Manzil: A.Xo'jayev ko'chasi 38-uy\nTel: +998 69 227 00 32\n"
	text += "Mo'ljal: NamDU binosi oldida,31-maktab ro'parasida\n"
	text += "Ish tartibi: Dushanbadan-Jumagacha 09:00-18:00, Dam olish kuni: Shanba-Yakshanba"
	
	await message.answer_location(latitude="41.00424411552747", longitude="71.67479438383347")        
	await message.reply_photo(file_id, caption=text)

@dp.message_handler(text="Davlat xizmatlari markazi \n(Davlatobod tuman)")
async def send_sanoat(message:Message):
    
	file_id = 'AgACAgIAAxkBAAOIY7Pg7W9EdOWMMUHaxLh8iiglmL4AAqPAMRsTBKFJIYWyUrF4Km4BAAMCAAN5AAMtBA'
	
	text = "<b>Davlat xizmatlari markazi (Davlatobod tuman)</b>\n"
	text += "Manzil: I.Karimov ko'chasi\n"
	text += "Mo'ljal: 3-kichik tuman, Tennis kort ro'parasida\n"
	text += "Ish tartibi: Dushanbadan-Jumagacha 09:00-18:00, Dam olish kuni: Shanba-Yakshanba"
	
	await message.answer_location(latitude="41.00265687037824", longitude="71.60933900611056")        
	await message.reply_photo(file_id, caption=text)
