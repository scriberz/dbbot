# bot.py
import telebot
from config import API_TOKEN
from handlers import start

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def handle_start(message):
    start(bot, message)

if __name__ == '__main__':
    bot.polling(non_stop=True)
