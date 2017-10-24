import telebot
import time
from threading import Thread

token = "461633768:AAFg3dQCW4HhM3K76d9nM-Au0Ai0nNVfE_w"
bot = telebot.TeleBot(token=token)

users = []

@bot.message_handler(commands=['start', 'help'])
def start(message):
    user = message.chat.id
    bot.send_message(user, "https://www.youtube.com/watch?v=rdg4lkgsQ04")

@bot.message_handler(commands=['spam'])
def add_user(message):
    user = message.chat.id
    if user not in users:
        users.append(user)
    bot.send_message(user, "Берем сироп вишневый!")

@bot.message_handler(commands=['stop'])
def remove_user(message):
    user = message.chat.id
    users.remove(user)
    bot.send_message(user, "Все, все.")

def spam():
    while True:
        for user in users:
            bot.send_message(user, "Затем сироп вишневый!")
        time.sleep(2)

def polling():
    bot.polling(none_stop=True)

polling_thread = Thread(target=polling)
spam_thread = Thread(target=spam)

polling_thread.start()
spam_thread.start()


