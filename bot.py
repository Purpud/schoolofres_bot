import telebot
import config
from telebot import types

bot = telebot.TeleBot(config.TOKEN)

# Реакция на "/start"
@bot.message_handler(commands=['start'])
def welcome(message):
	sti = open('stickers/welcome.tgs', 'rb')
	bot.send_sticker(message.chat.id, sti)

	# keyboard
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton("Організатори")
	item2 = types.KeyboardButton("Інфо про проєкт")
	item3 = types.KeyboardButton("Зареєструватися")

	markup.add(item1, item2)
	markup.add(item3)

	bot.send_message(message.chat.id, "Привіт, <b>{0.first_name}</b>!\nХочеш дізнатися більше про локальну школу успіху в Києві?\nВибирай опцію нижче 👇".format(message.from_user, bot.get_me()),
		parse_mode='html', reply_markup=markup)

# Обработка нажатий на клавиши клавматуры
@bot.message_handler(content_types=['text'])
def answer_reply(message):
	if message.chat.type == 'private':
		# if message.text == 'Інфо про проєкт':
		# 	markup = types.InlineKeyboardMarkup(row_width=1)
		# 	item1 = types.InlineKeyboardButton("Купить", callback_data='buy')
		#
		# 	markup.add(item1)
		#
		# 	bot.send_photo(message.chat.id, photo=open('stickers/AirPods.jpg', 'rb'), caption="AirPods 2", reply_markup=markup)

		if message.text == 'Організатори':
			# Julia Popadina
			bot.send_photo(message.chat.id, photo=open('assets/participants_compressed/Julia.jpg', 'rb'), caption="⭐ *Юлія Попадіна* ⭐", parse_mode='markdown')
			bot.send_message(message.chat.id, (
			"Я *Юля*, у квітні святкуватиму 17-ий день народження, люблю котів і творчість Жадана. Організаторка проєкту \"School of Resilience Kyiv\"\n"
			"Цього року стала випускницею проєкту \"School of Resilience\", що подарував 10 неймовірних днів у сонячному місті Гайдельберг.\n"
			"Нетворкінг, який ми отримали на проєкті, а також навички і знання, без яких ну просто ніяк у мінливому сучасному світі, були просто неоціненними! "), parse_mode='markdown')

			# Denis Budnychenko
			bot.send_photo(message.chat.id, photo=open('assets/participants_compressed/Den.jpg', 'rb'), caption="⭐ *Денис Будниченко* ⭐", parse_mode='markdown')
			bot.send_message(message.chat.id, ("Привіт, я *Денис*, випускник проєкту \"Shool of Resilience\" та організатор проєкту \"Shool of Resilience Kyiv\" "), parse_mode='markdown')

			# Kamila Shaga
			bot.send_photo(message.chat.id, photo=open('assets/participants_compressed/Kamila.jpg', 'rb'), caption="⭐ *Каміла Шага* ⭐", parse_mode='markdown')
			bot.send_message(message.chat.id, ("Привіт, я *Каміла*, випускниця проєкту \"Shool of Resilience\" та організаторка проєкту \"Shool of Resilience Kyiv\" "), parse_mode='markdown')

			# Margo Vovchek
			bot.send_photo(message.chat.id, photo=open('assets/participants_compressed/Margo.jpg', 'rb'), caption="⭐ *Маргарита Вовчек* ⭐", parse_mode='markdown')
			bot.send_message(message.chat.id, ("Привіт, я *Марго*, випускниця проєкту \"Shool of Resilience\" та організаторка проєкту \"Shool of Resilience Kyiv\" "), parse_mode='markdown')

			# Max Pinchuk
			bot.send_photo(message.chat.id, photo=open('assets/participants_compressed/Max.jpg', 'rb'), caption="⭐ *Максим Пінчук* ⭐", parse_mode='markdown')
			bot.send_message(message.chat.id, ("Привіт, я *Макс*, випускник проєкту \"Shool of Resilience\" та організатор проєкту \"Shool of Resilience Kyiv\" "), parse_mode='markdown')

			# Nazar Slabliuk
			bot.send_photo(message.chat.id, photo=open('assets/participants_compressed/Nazar.jpg', 'rb'), caption="⭐ *Назар Слаблюк* ⭐", parse_mode='markdown')
			bot.send_message(message.chat.id, ("Привіт, я *Назар*, випускник проєкту \"Shool of Resilience\" та організатор проєкту \"Shool of Resilience Kyiv\" "), parse_mode='markdown')

			# Sonia Kuchinska
			bot.send_photo(message.chat.id, photo=open('assets/participants_compressed/Sonia.jpg', 'rb'), caption="⭐ *Софія Кучинська* ⭐", parse_mode='markdown')
			bot.send_message(message.chat.id, ("Привіт, я *Соня*, випускниця проєкту \"Shool of Resilience\" та організаторка проєкту \"Shool of Resilience Kyiv\" "), parse_mode='markdown')

			# Eugene Kravchuk
			bot.send_photo(message.chat.id, photo=open('assets/participants_compressed/Eugene.jpg', 'rb'), caption="⭐ *Євгеній Кравчук* ⭐", parse_mode='markdown')
			bot.send_message(message.chat.id, ("Привіт, я *Женя*, випускник проєкту \"Shool of Resilience\" та організатор проєкту \"Shool of Resilience Kyiv\""), parse_mode='markdown')
		elif message.text == 'Інфо про проєкт':
			# bot.send_message(message.chat.id, ("*На проєкті ти дізнаєшся:*\n\n"
			# 								   "• Як заповнити грантову заявку і отримати фінансування на свої найнеймовірніші ідеї? 💡\n"
			# 								   "• Як захопити увагу аудиторії, побороти страх і стати майстром публічних виступів? 💬\n"
			# 								   "• Як розвинути особистий бренд щоб залишати незабутнє враження скрізь, де вас побачать? 🎯\n\n"
			# 								   "Ми впевнені, що багатьох цікавлять ці питання, і гарантуємо: школа стійкості - це місце де ви обов'язково отримаєте відповідь на кожне із них! 😃\n\n"
			# 								   "Натхненні власним досвідом, ми приступили до розробки проєкту *\"School of Resilience Kyiv\"*, стати учасником якого вже цієї весни, можеш стати саме ТИ! 🫵\n\n"
			# 								   "Будьте певні, ми з командою підготували дещо дійсно крутезне! 😎"),parse_mode='markdown')

			bot.send_message(message.chat.id, ("*На проєкті ти дізнаєшся:*\n\n"
											   "• Як заповнити грантову заявку і отримати фінансування на свої найнеймовірніші ідеї? 💡\n"
											   "• Як захопити увагу аудиторії, побороти страх і стати майстром публічних виступів? 💬\n"
											   "• Як розвинути особистий бренд щоб залишати незабутнє враження скрізь, де вас побачать? 🎯\n\n"), parse_mode='markdown')
			bot.send_message(message.chat.id, ("Ми впевнені, що багатьох цікавлять ці питання, і гарантуємо: школа стійкості - це місце де ви обов'язково отримаєте відповідь на кожне із них! 😃\n\n"), parse_mode='markdown')
			bot.send_message(message.chat.id, ("Натхненні власним досвідом, ми приступили до розробки проєкту *\"School of Resilience Kyiv\"*, стати учасником якого вже цієї весни, можеш стати саме ТИ! 🫵\n\n"), parse_mode='markdown')
			bot.send_message(message.chat.id, ("Будьте певні, ми з командою підготували дещо дійсно крутезне! 😎"), parse_mode='markdown')
			bot.send_message(message.chat.id, ("Щоб зареєструватися переходь за посиланням: <b><a href=\"https://docs.google.com/forms/d/e/1FAIpQLScTNtP9jxucN2n4RMWowc97i41DA16ibRbQp7KIGCF6uAmQVw/viewform\">реєстрація</a></b>"), parse_mode='html')
		elif message.text == 'Зареєструватися':
			bot.send_message(message.chat.id, "Щоб зареєструватися переходь за посиланням: <b><a href=\"https://docs.google.com/forms/d/e/1FAIpQLScTNtP9jxucN2n4RMWowc97i41DA16ibRbQp7KIGCF6uAmQVw/viewform\">реєстрація</a></b>", parse_mode="html")


		else:
			bot.send_message(message.chat.id, "Я не знаю, що відповісти")

# Непонятная хрень
bot.enable_save_next_step_handlers(delay=2)
bot.load_next_step_handlers()

# RUN
if __name__ == '__main__':
	bot.polling(none_stop=True)