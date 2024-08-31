import telebot

from pdfminer.high_level import extract_pages, extract_text

from bot import API_KEY

text = extract_text("ug_rules.pdf")
print(text)

bot = telebot.TeleBot(API_KEY, parse_mode=None)

@bot.message_handler(commands=['start','help'])
def welcome_message(message):
    bot.reply_to(message, "Hello, welcome to the student's query bot.")

bot.infinity_polling()