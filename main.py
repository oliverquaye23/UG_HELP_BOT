import telebot

from bot import API_KEY

bot = telebot.TeleBot(API_KEY, parse_mode=None)

@bot.message_handler(commands=['start','help'])
def welcome_message(message):
    bot.reply_to(message, "Hello, welcome to the student's query bot.")

bot.infinity_polling()