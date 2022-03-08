import telebot
from telebot import types
token = "5212720849:AAGaPCNsgaJ9INmljYQRIcCNLdjxHDHpEVc"
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])

def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("/help", "/end", "1", "2", "3")
    bot.send_message(message.chat.id, 'Привет! Хотите узнать свежую информацию о МТУСИ, расписание МТУСИ или информацию о системе дистанционного обучения МТУСИ? 1, 2 или 3')

@bot.message_handler(commands=['help'])

def start_message(message):
    bot.send_message(message.chat.id, 'Я умею при помощи команд 1, 2 или 3 присылать информацию МТУСИ, расписание МТУСИ или информацию о системе дистанционного обучения МТУСИ. Введите 1, чтобы узнать информацию о МТУСИ, введите 2,'
                                      ' чтобы узнать расписание МТУСИ или введите 3, чтобы перейти на сайт <система дистанционного обучения МТУСИ>.')

@bot.message_handler(commands=['end'])

def start_message(message):
    bot.send_message(message.chat.id, 'Спасибо за использование бота. До связи!')

@bot.message_handler(content_types=['text'])

def answer(message):
    if message.text.lower() == "1":
        bot.send_message(message.chat.id, 'Тогда вам сюда – https://mtuci.ru/')
    if message.text.lower() == "2":
        bot.send_message(message.chat.id, 'Тогда вам сюда – https://mtuci.ru/time-table/')
    if message.text.lower() == "3":
        bot.send_message(message.chat.id, 'Тогда вам сюда – https://mtuci.ru/education/eios/')
bot.infinity_polling()
