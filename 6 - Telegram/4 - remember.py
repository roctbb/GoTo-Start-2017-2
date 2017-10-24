import telebot

token = "461633768:AAFg3dQCW4HhM3K76d9nM-Au0Ai0nNVfE_w"
bot = telebot.TeleBot(token=token)
phrases = {}

@bot.message_handler(commands=['remind'])
def remind(message):
    user = message.chat.id
    bot.send_message(user, phrases[user])

@bot.message_handler(content_types=['text'])
def remember(message):
    user = message.chat.id
    phrases[user] = message.text
    bot.send_message(user, "Я запомнил")

bot.polling(none_stop=True)


