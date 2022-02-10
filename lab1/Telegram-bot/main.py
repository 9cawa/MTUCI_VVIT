import telebot
from telebot import types
import random

token = "5045703758:AAEZIBJt3a6ide7mZ08ymHVyq7L0kBJ6CnI"
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start','назад'])
def start(message):
    keyboard = telebot.types.ReplyKeyboardMarkup()
    keyboard.row("/mtuciNews", "/help", "/fun")
    bot.send_message(message.chat.id, 'Привет! Выбери команду.', reply_markup=keyboard)
@bot.message_handler(commands=['mtuciNews'])
def start(message):
    keyboard = telebot.types.ReplyKeyboardMarkup()
    keyboard.row("хочу", "не хочу", "назад")
    bot.send_message(message.chat.id, 'Хочешь узнать свежую информацию о МТУСИ?', reply_markup=keyboard)
@bot.message_handler(commands=['fun'])
def start(message):
    keyboard = telebot.types.ReplyKeyboardMarkup()
    keyboard.row("да", "нет", "назад")
    bot.send_message(message.chat.id, 'Хочешь узнать насколько ты крут?', reply_markup=keyboard)
@bot.message_handler(commands=['help'])
def start_message(message):
    keyboard = telebot.types.ReplyKeyboardMarkup()
    keyboard.row("/mtuciNews", "/help", "/fun")
    bot.send_message(message.chat.id, 'Мои функции:\n'
                     '/mtuciNews - Информация о мтуси\n'
                     '/fun - Тут прикол\n'
                     '/help - Помощь')
@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == "хочу":
        bot.send_message(message.chat.id, 'Тогда тебе сюда – https://mtuci.ru/')
        keyboard = telebot.types.ReplyKeyboardMarkup()
        keyboard.row("/mtuciNews", "/help", "/fun")
        bot.send_message(message.chat.id, 'Выбери команду.', reply_markup=keyboard)
    if message.text.lower() == "не хочу":
        bot.send_message(message.chat.id, 'А надо! Бегом сюда - https://mtuci.ru/')
        keyboard = telebot.types.ReplyKeyboardMarkup()
        keyboard.row("/mtuciNews", "/help", "/fun")
        bot.send_message(message.chat.id, 'Выбери команду.', reply_markup=keyboard)
    if message.text.lower() == "да":
        bot.send_message(message.chat.id, 'Ты крутой на: ' + str(random.randint(0, 100)) + '%!')
        keyboard = telebot.types.ReplyKeyboardMarkup()
        keyboard.row("/mtuciNews", "/help", "/fun")
        bot.send_message(message.chat.id, 'Выбери команду.', reply_markup=keyboard)
    if message.text.lower() == "нет":
        bot.send_message(message.chat.id, 'Трус!')
        keyboard = telebot.types.ReplyKeyboardMarkup()
        keyboard.row("/mtuciNews", "/help", "/fun")
        bot.send_message(message.chat.id, 'Выбери команду.', reply_markup=keyboard)
    if message.text.lower() == "назад":
        keyboard = telebot.types.ReplyKeyboardMarkup()
        keyboard.row("/mtuciNews", "/help", "/fun")
        bot.send_message(message.chat.id, 'Выбери команду.', reply_markup=keyboard)
bot.infinity_polling()
