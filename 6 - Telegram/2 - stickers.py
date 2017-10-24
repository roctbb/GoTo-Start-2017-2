import telebot
import random

token = "461633768:AAFg3dQCW4HhM3K76d9nM-Au0Ai0nNVfE_w"
bot = telebot.TeleBot(token=token)
stickers = []

@bot.message_handler(content_types=['text'])
def calc(message):
    user = message.chat.id
    text = message.text
    try:
        result = eval(text)
        bot.send_message(user, result)
    except:
        bot.send_message(user, "Ну это перебор!")

@bot.message_handler(content_types=['sticker'])
def echo(message):
    user = message.chat.id
    sticker = message.sticker.file_id

    stickers.append(sticker)

    bot.send_sticker(user,random.choice(stickers))


bot.polling(none_stop=True)


