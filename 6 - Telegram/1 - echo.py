import telebot

token = "461633768:AAFg3dQCW4HhM3K76d9nM-Au0Ai0nNVfE_w"
bot = telebot.TeleBot(token=token)

@bot.message_handler(content_types=['text'])
def echo(message):
    text = message.text
    user = message.chat.id

    bot.send_message(user, "Сам ты "+text+"!")





bot.polling(none_stop=True)


