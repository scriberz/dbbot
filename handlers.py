# handlers.py
from database import get_user, create_user
import telebot

def start(bot: telebot.TeleBot, message: telebot.types.Message):
    user_id = message.from_user.id
    username = message.from_user.username or 'Unknown'
    
    user = get_user(user_id)
    if user:
        response = f"Welcome back, {username}!"
    else:
        create_user(user_id, username)
        response = f"Welcome, {username}! You have been added to the database."
    
    bot.send_message(message.chat.id, response)


def compute(update: Update, context: CallbackContext):
    # Логика для вычисления протеинов
    pass

def build(update: Update, context: CallbackContext):
    # Логика для строительства капсулы
    pass

def transfer(update: Update, context: CallbackContext):
    # Логика для передачи ресурсов
    pass

def status(update: Update, context: CallbackContext):
    # Логика для отображения статуса игрока
    pass

