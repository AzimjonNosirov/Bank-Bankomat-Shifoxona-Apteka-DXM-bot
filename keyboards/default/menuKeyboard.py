from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menuStart = ReplyKeyboardMarkup(
	keyboard = [
		[
			KeyboardButton(text="Banklar"),
			KeyboardButton(text="Bankomatlar"),
		],
		[
			KeyboardButton(text="Shifoxonalar"),
			KeyboardButton(text="Dorixonalar"),
		],
		[
			KeyboardButton(text="Davlat xizmatlari markazi \n(Namangan shahar)"),
		],
		[
			KeyboardButton(text="Davlat xizmatlari markazi \n(Davlatobod tuman)"),
		],
		[
			KeyboardButton(text="Qo'llanma"),
		],
	
	],
	resize_keyboard=True

)

menuBankomat = ReplyKeyboardMarkup(
	keyboard = [
		[
			KeyboardButton(text="Namangan sh - 102 ta"),
			KeyboardButton(text="Davlatobod t - 41 ta"),
		],
		# [
		# 	KeyboardButton(text="Yangi Namangan t - 18 ta"),
		# 	KeyboardButton(text="Namangan t - 19 ta"),
		# ],
		# [
		# 	KeyboardButton(text="To'raqo'rg'on t - 34 ta"),
		# 	KeyboardButton(text="Mingbuloq t - 18 ta"),
		# ],
		# [
		# 	KeyboardButton(text="Kosonsoy t - 21 ta"),
		# 	KeyboardButton(text="Pop t - 30 ta"),
		# ],
		# [
		# 	KeyboardButton(text="Norin t - 17 ta"),
		# 	KeyboardButton(text="Uychi t - 31 ta"),
		# ],
		# [
		# 	KeyboardButton(text="Chortoq t - 20 ta"),
		# 	KeyboardButton(text="Chust t - 27 ta"),
		# ],
		# [
		# 	KeyboardButton(text="Uchqo'rg'on t - 30 ta"),
		# 	KeyboardButton(text="Yangiqo'rg'on t - 17 ta"),
		# ],
		[
			KeyboardButton(text="🔙 Ortga"),
		],
	],
	resize_keyboard=True
)
menuApteka = ReplyKeyboardMarkup(
	keyboard = [
		[
			KeyboardButton(text="Namangan shahar"),
			KeyboardButton(text="Davlatobod tuman"),
		],
		# [
		# 	KeyboardButton(text="Yangi Namangan tuman"),
		# 	KeyboardButton(text="Namangan tuman"),
		# ],
		# [
		# 	KeyboardButton(text="To'raqo'rg'on tuman"),
		# 	KeyboardButton(text="Mingbuloq tuman"),
		# ],
		# [
		# 	KeyboardButton(text="Kosonsoy tuman"),
		# 	KeyboardButton(text="Pop tuman"),
		# ],
		# [
		# 	KeyboardButton(text="Norin tuman"),
		# 	KeyboardButton(text="Uychi tuman"),
		# ],
		# [
		# 	KeyboardButton(text="Chortoq tuman"),
		# 	KeyboardButton(text="Chust tuman"),
		# ],
		# [
		# 	KeyboardButton(text="Uchqo'rg'on tuman"),
		# 	KeyboardButton(text="Yangiqo'rg'on tuman"),
		# ],
		[
			KeyboardButton(text="◀ Ortga"),
		],
	],
	resize_keyboard=True
)
menuShifo = ReplyKeyboardMarkup(
	keyboard = [
		[
			KeyboardButton(text="Namangan shahar"),
			KeyboardButton(text="Davlatobod tuman"),
		],
		[
			KeyboardButton(text="👈 Ortga"),
		],
	],
	resize_keyboard=True
)







