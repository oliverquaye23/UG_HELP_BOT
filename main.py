import telebot

from pdfminer.high_level import extract_pages, extract_text

from transformers import pipeline

from bot import API_KEY

text = extract_text("ug_rules.pdf")
print(text)

QA_pipepline = pipeline("question-amswering")

bot = telebot.TeleBot(API_KEY, parse_mode=None)

@bot.message_handler(commands=['start','help'])
def welcome_message(message):
    bot.reply_to(message, "Hello, welcome to the student's query bot.")

@bot.message_handler(func=lambda message: True)
def query_response(message):
  query = message.text

  result = QA_pipepline(question=query, context=text)

  response = result['answser']
  certainty = result['score']

  if certainty > 0.3:
     answer = f"Answer: {response} \n Certainty:{round(certainty,2)} "

  else:
     answer = "Sorry! I could'nt find a relevant answer in the document "

  bot.reply_to(message, answer)
  
bot.infinity_polling()