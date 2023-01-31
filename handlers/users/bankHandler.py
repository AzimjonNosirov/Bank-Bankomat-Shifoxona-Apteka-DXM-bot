from aiogram.dispatcher.filters import Text, Command
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, Message
from loader import dp, bot
from keyboards.default.shahar_bank import shaharbank
from keyboards.default.menuKeyboard import menuStart 
from states.locstates import locstates
from aiogram.dispatcher import FSMContext

@dp.message_handler(text="Agrobank Namangan filiali", state=locstates.bank)
async def send_agronam(message:Message, state=FSMContext):
    
	file_id = 'AgACAgIAAxkBAAIBPmOz6gWvf8cMaZXQbxFf8y2i98KNAAKTwDEbEwShSZOig-3GzgVUAQADAgADeAADLQQ'
	
	text = "<b>Agrobank Namangan filiali</b>\n"
	text += "Manzil: Islom Karimov ko'chasi 23-uy\n Tel: +998 69 228 72 05\n"
	text += "Mo'ljal: Pahlavon sport majmuasi\n"
	text += "Ish tartibi: Dushanbadan-Jumagacha 09:00-17:00, tushlik: 13:00-14:00"
	
	await message.answer_location(latitude="41.00796883587812", longitude=" 71.62345267916557")        
	await message.reply_photo(file_id, caption=text)
	
@dp.message_handler(text="O'zsanoatqurilish bank", state=locstates.bank)
async def send_sanoat(message:Message, state=FSMContext):
    
	file_id = 'AgACAgIAAxkBAANVY7PgbPNdwSfoMg4lkUeDpYOcjE8AApvAMRsTBKFJZ8oDu2WmPBABAAMCAAN4AAMtBA'
	
	text = "<b>O'zsanoatqurilish bank</b>\n"
	text += "Manzil: Islom Karimov ko'chasi 19-uy\n Tel: +998 69 234 32 90\n"
	text += "Mo'ljal: Do'stlik bozori\n"
	text += "Ish tartibi: Dushanbadan-Jumagacha 09:00-17:00, tushlik: 13:00-14:00"
	
	await message.answer_location(latitude="41.00628757055634", longitude=" 71.63589974858189")        
	await message.reply_photo(file_id, caption=text)

@dp.message_handler(text="Ipak yo'li banki Namangan filiali", state=locstates.bank)
async def send_ipa(message:Message, state=FSMContext):
    
	file_id = 'AgACAgIAAxkBAANaY7PgbXjnUr2KF09AgJe-vXWcivMAAp3AMRsTBKFJOLG7_uO8s0YBAAMCAAN4AAMtBA'
	
	text = "<b>Ipak yo'li banki Namangan filiali</b>\n"
	text += "Manzil: Navoiy ko'chasi\n Tel: +998 69 232 54 35\n"
	text += "Mo'ljal: Ipoteka banki yonida\n"
	text += "Ish tartibi: Dushanbadan-Jumagacha 09:00-17:00, tushlik: 13:00-14:00"
	
	await message.answer_location(latitude="40.995108141421035", longitude="71.64697572616248")        
	await message.reply_photo(file_id, caption=text)

@dp.message_handler(text="Hamkorbank Namangan filiali", state=locstates.bank)
async def send_hamkor(message:Message, state=FSMContext):
    
	file_id = 'AgACAgIAAxkBAANKY7PgagShwm3TAAEDKVeJKvO8qqaMAAKVwDEbEwShSeMQOkTy9MHIAQADAgADbQADLQQ'
	
	text = "<b>Hamkorbank Namangan filiali</b>\n"
	text += "Manzil: Navoiy ko'chasi 31-uy\n Tel: +998 69 228 80 97\n"
	text += "Mo'ljal: Namangan viloyat suv ta'minoti oldida\n"
	text += "Ish tartibi: Dushanbadan-Jumagacha 09:00-17:00, tushlik: 13:00-14:00"
	
	await message.answer_location(latitude="40.99218850100652", longitude="71.65578333442755")        
	await message.reply_photo(file_id, caption=text)
	
@dp.message_handler(text="Asaka bank Namangan filiali", state=locstates.bank)
async def send_asaka(message:Message, state=FSMContext):
    
	file_id = 'AgACAgIAAxkBAANIY7PgafldBpfEzeYT2THhnIzhi6gAApTAMRsTBKFJAAGmOYBOVvWPAQADAgADbQADLQQ'
	
	text = "<b>Asaka bank</b>\n"
	text += "Manzil: Navoiy ko'chasi 27-uy\n Tel: +998 69 227 21 45\n"
	text += "Mo'ljal: Zahiriddin Muhammad Bobur nomli istirohat bog'i oldida\n"
	text += "Ish tartibi: Dushanbadan-Jumagacha 09:00-17:00, tushlik: 13:00-14:00"
	
	await message.answer_location(latitude="40.99423599482231", longitude=" 71.67261335891952")        
	await message.reply_photo(file_id, caption=text)

@dp.message_handler(text="Infin bank Namangan filiali", state=locstates.bank)
async def send_infin(message:Message, state=FSMContext):
    
	file_id = 'AgACAgIAAxkBAAIBQWOz6q4SInXD6gb_3B32x7PaZyI2AALGwDEbEwShSX1K6eIlf3pRAQADAgADeQADLQQ'
	
	text = "<b>Infin bank Namangan filiali</b>\n"
	text += "Manzil: Nodira ko'chasi 4-uy\n Tel: +998 69 227 80 32\n"
	text += "Mo'ljal: Mobiuz ofisi yonida\n"
	text += "Ish tartibi: Dushanbadan-Jumagacha 09:00-17:00, tushlik: 13:00-14:00"
	
	await message.answer_location(latitude="40.996110584230856", longitude=" 71.66686759949698")        
	await message.reply_photo(file_id, caption=text)

@dp.message_handler(text="Trastbank Namangan filiali", state=locstates.bank)
async def send_trast(message:Message, state=FSMContext):
    
	file_id = 'AgACAgIAAxkBAANUY7PgbEj7fBYTEQh-B7pFLwWPu8kAAprAMRsTBKFJHrvDJzbyBrQBAAMCAAN4AAMtBA'
	
	text = "<b>Trastbank Namangan filiali</b>\n"
	text += "Manzil: Xotira ko'chasi 1-uy\n Tel: +998 69 232 07 33\n"
	text += "Mo'ljal: Infin bank ro'parasida\n"
	text += "Ish tartibi: Dushanbadan-Jumagacha 09:00-17:00, tushlik: 13:00-14:00"
	
	await message.answer_location(latitude="40.99637349583459", longitude=" 71.66763459698893")        
	await message.reply_photo(file_id, caption=text)

@dp.message_handler(text="Mikrokreditbank", state=locstates.bank)
async def send_mikro(message:Message, state=FSMContext):
    
	file_id = 'AgACAgIAAxkBAANSY7PgbK6Mhp8qFpUVzUvSs0st0fsAApjAMRsTBKFJ1czpevS9OZABAAMCAAN5AAMtBA'
	
	text = "<b>Mikrokreditbank</b>\n"
	text += "Manzil: 6-kichik noxiya \n Tel: +998 78 223 06 22\n"
	text += "Mo'ljal: 17-avtobaza pastida"
	text += "Ish tartibi: Dushanbadan-Jumagacha 09:00-17:00, tushlik: 13:00-14:00"
	
	await message.answer_location(latitude="41.03592991003399", longitude="71.6193266870069")        
	await message.reply_photo(file_id, caption=text)

@dp.message_handler(text="Ipak yo'li banki Davlatobod filiali", state=locstates.bank)
async def send_ipak(message:Message, state=FSMContext):
    
	file_id = 'AgACAgIAAxkBAANMY7PgahWdR2BMYh37ez1ZuCfo_VoAApfAMRsTBKFJ8ZZ7hMp7fVUBAAMCAANtAAMtBA'
	
	text = "<b>Ipak yo'li banki Davlatobod filiali</b>\n"
	text += "Manzil: 6-kichik noxiya, G'alaba ko'chasi \n Tel: +998 69 232 48 81\n"
	text += "Mo'ljal: Makro supermarketi atrofida\n"
	text += "Ish tartibi: Dushanbadan-Jumagacha 09:00-17:00, tushlik: 13:00-14:00"
	
	await message.answer_location(latitude="40.99410887880642", longitude="71.61621666372012")        
	await message.reply_photo(file_id, caption=text)

@dp.message_handler(text="NBU bank", state=locstates.bank)
async def send_nbu(message:Message, state=FSMContext):
    
	file_id = 'AgACAgIAAxkBAANBY7PgaLVH49sRqvI3hNq2T0Le2HcAApnAMRsTBKFJ1zQ_kpJ6US4BAAMCAANtAAMtBA'
	
	text = "<b>NBU bank</b>\n"
	text += "Manzil: 2-kichik noxiya, Islom Karimov ko'chasi\n"
	text += "Mo'ljal:   Namangan mehmonxonasi yonida\n"
	text += "Ish tartibi:   Dushanbadan-Jumagacha 09:00-17:00,   tushlik: 13:00-14:00"
	
	await message.answer_location(latitude="40.996726439773894", longitude=" 71.58541207857355")        
	await message.reply_photo(file_id, caption=text)

@dp.message_handler(text="Agrobank Davlatobod filiali", state=locstates.bank)
async def send_agro(message:Message, state=FSMContext):
    
	file_id = 'AgACAgIAAxkBAANYY7Pgbad7vbPMAd69R5VAl4qgjSQAApzAMRsTBKFJ2YBnzEnsUHEBAAMCAAN4AAMtBA'
	
	text = "<b>Agrobank Davlatobod filiali</b>\n"
	text += "Manzil: G'alaba ko'chasi 19A-uy\n"
	text += "Mo'ljal: Yong'in xavfsizlik boshqarmasi oldida \n"
	text += "Ish tartibi: Dushanbadan-Jumagacha 09:00-17:00, tushlik: 13:00-14:00"
	
	await message.answer_location(latitude="40.99434008191502", longitude="71.60645236060468")        
	await message.reply_photo(file_id, caption=text)

@dp.message_handler(text="Ipoteka bank", state=locstates.bank)
async def send_agro(message:Message, state=FSMContext):
    
	file_id = 'AgACAgIAAxkBAAPhY7Po38toWnVd-DdQK-V9F4HTiYQAAp7AMRsTBKFJD2a75sLc7wQBAAMCAAN4AAMtBA'
	
	text = "<b>Ipoteka bank</b>\n"
	text += "Manzil: Navoiy ko'chasi 63-uy\n"
	text += "Mo'ljal: Ipak yo'li banki oldida \n"
	text += "Ish tartibi: Dushanbadan-Jumagacha 09:00-17:00, tushlik: 13:00-14:00"
	
	await message.answer_location(latitude="40.99619082950562", longitude=" 71.64643006783949")        
	await message.reply_photo(file_id, caption=text)

@dp.message_handler(text="Tenge bank", state=locstates.bank)
async def send_agro(message:Message, state=FSMContext):
    
	file_id = 'AgACAgIAAxkBAANlY7PgcBkKSnklu1Vn4t3RZaOL0C8AAqbAMRsTBKFJJTroaJt-cOYBAAMCAAN4AAMtBA'
	
	text = "<b>Tenge bank</b>\n"
	text += "Manzil: G'alaba ko'chasi 28A-uy\n"
	text += "Mo'ljal: 4-kichik nohiya \"Baba Food\" steak house oldida\n"
	text += "Ish tartibi: Dushanbadan-Jumagacha 09:00-18:00, tushlik: 13:00-14:00"
	
	await message.answer_location(latitude="40.99470457355377", longitude="71.59992983390872")        
	await message.reply_photo(file_id, caption=text)

@dp.message_handler(text="Anorbank", state=locstates.bank)
async def send_agro(message:Message, state=FSMContext):
    
	file_id = 'AgACAgIAAxkBAANnY7PgcYJtmURlHX-ZeAAB20zLQwAB9gACp8AxGxMEoUkUHNWsR0UYvgEAAwIAA3gAAy0E'
	
	text = "<b>Anorbank</b>\n"
	text += "Manzil: G'irvonsoy ko'chasi\n"
	text += "Mo'ljal: \"Sag\" gilam do'koni yonida\n"
	text += "Ish tartibi: Dushanbadan-Shanbagacha 09:00-18:00, tushlik: 13:00-14:00"
	
	await message.answer_location(latitude="40.99243033602569", longitude="71.63483711163127")        
	await message.reply_photo(file_id, caption=text)

@dp.message_handler(text="Kapitalbank", state=locstates.bank)
async def send_agro(message:Message, state=FSMContext):
    
	file_id = 'AgACAgIAAxkBAANfY7Pgbsc88CHhjl--IcZR614ogLkAAp_AMRsTBKFJQZvMct-vqywBAAMCAAN5AAMtBA'
	
	text = "<b>Kapitalbank</b>\n"
	text += "Manzil: Nomongoniy ko'chasi 27-uy\n"
	text += "Mo'ljal: Nodira kutubxonasi oldida \n"
	text += "Ish tartibi: Dushanbadan-Jumagacha 09:00-17:00, tushlik: 13:00-14:00"
	
	await message.answer_location(latitude="40.99993711421048", longitude="71.66597492565987")        
	await message.reply_photo(file_id, caption=text)

@dp.message_handler(text="Xalq bank", state=locstates.bank)
async def send_agro(message:Message, state=FSMContext):
    
	file_id = 'AgACAgIAAxkBAANkY7PgcINhh1QX2cJXVLeC4xCFTsUAAqLAMRsTBKFJu9rM22McpncBAAMCAAN4AAMtBA'
	
	text = "<b>Xalq bank</b>\n"
	text += "Manzil: Lutfiy ko'chasi 63-uy\n"
	text += "Mo'ljal: Jinoyat ishlari bo'yicha Namangan shahar sudi binosi oldida, 'Beeline' ofisi orqasida \n"
	text += "Ish tartibi: Dushanbadan-Jumagacha 09:00-18:00, tushlik: 13:00-14:00"
	
	await message.answer_location(latitude="41.00158233601409", longitude="71.66894279005386")        
	await message.reply_photo(file_id, caption=text)

@dp.message_handler(text="Qishloq qurilish bank", state=locstates.bank)
async def send_agro(message:Message, state=FSMContext):
    
	file_id = 'AgACAgIAAxkBAANyY7PgdAycraI4ipca-UQhwbuYkFsAAqvAMRsTBKFJmQ9UXEyFwNcBAAMCAAN4AAMtBA'
	
	text = "<b>Qishloq qurilish bank</b>\n"
	text += "Manzil: Navoiy ko'chasi 70A-uy\n"
	text += "Mo'ljal: \"Ucell\"ofisi ro'parasida \n"
	text += "Ish tartibi: Dushanbadan-Jumagacha 09:00-17:00, tushlik: 13:00-14:00"
	
	await message.answer_location(latitude="40.99736902316477", longitude="71.64683239934688")        
	await message.reply_photo(file_id, caption=text)

@dp.message_handler(text="Turon bank", state=locstates.bank)
async def send_agro(message:Message, state=FSMContext):
    
	file_id = 'AgACAgIAAxkBAANjY7PgcHCF0XRP28svcrHtnM0ykK8AAqHAMRsTBKFJJIIlMnUd9KoBAAMCAAN5AAMtBA'
	
	text = "<b>Turon bank</b>\n"
	text += "Manzil: Xamroh ko'chasi 68A-uy\n"
	text += "Mo'ljal: 1-sonli FHDYO bo'limi\n"
	text += "Ish tartibi: Dushanbadan-Jumagacha 09:00-18:00, tushlik: 13:00-14:00"
	
	await message.answer_location(latitude="41.00791387649788", longitude="71.66360359686864")        
	await message.reply_photo(file_id, caption=text)

@dp.message_handler(text="Savdogirbank", state=locstates.bank)
async def send_agro(message:Message, state=FSMContext):
    
	file_id = 'AgACAgIAAxkBAANrY7PgceRW9lfhVhy4qHUmhrEcSlAAAqnAMRsTBKFJvDHFP2CwfMYBAAMCAAN4AAMtBA'
	
	text = "<b>Savdogirbank</b>\n"
	text += "Manzil: Ibrat ko'chasi 26-uy\n"
	text += "Mo'ljal: 'Hamal Computer Service' oldida \n"
	text += "Ish tartibi: Dushanbadan-Jumagacha 09:00-18:00, tushlik: 13:00-14:00"
	
	await message.answer_location(latitude="41.0058376470568", longitude="71.66922594525283")        
	await message.reply_photo(file_id, caption=text)

@dp.message_handler(text="Davr bank", state=locstates.bank)
async def send_agro(message:Message, state=FSMContext):
    
	file_id = 'AgACAgIAAxkBAANpY7PgcRL6iyzbgt0xJ5vmoTR7bH0AAqjAMRsTBKFJCEeV_urc3uYBAAMCAAN4AAMtBA'
	
	text = "<b>Davr bank</b>\n"
	text += "Manzil: Navoiy ko'chasi 1-uy\n"
	text += "Mo'ljal: \"Shodlik\" supermarketi oldida \n"
	text += "Ish tartibi: Dushanbadan-Jumagacha 08:30-17:30, tushlik: 13:00-14:00"
	
	await message.answer_location(latitude="40.99290143153587", longitude="71.64914013701926")        
	await message.reply_photo(file_id, caption=text)

@dp.message_handler(text="Markaziy bank", state=locstates.bank)
async def send_agro(message:Message, state=FSMContext):
    
	file_id = 'AgACAgIAAxkBAANiY7Pgb8U-qI9pV4wH4x8WwuDyu6AAAqDAMRsTBKFJ3NVuuRyZFqMBAAMCAAN5AAMtBA'
	
	text = "<b>Markaziy bank</b>\n"
	text += "Manzil: B.Mashrab ko'chasi 2-uy\n"
	text += "Mo'ljal: 'Beeline' ofisi oldida \n"
	text += "Ish tartibi: Dushanbadan-Jumagacha 09:00-17:00, tushlik: 13:00-14:00"
	
	await message.answer_location(latitude="41.00208232146027", longitude="71.67028389455535")        
	await message.reply_photo(file_id, caption=text)

@dp.message_handler(text="Ortga", state="*")
async def send_back(message:Message, state=FSMContext):
    await message.answer("Ortga", reply_markup=menuStart)
    await state.finish()