import telebot

token = "461633768:AAFg3dQCW4HhM3K76d9nM-Au0Ai0nNVfE_w"
bot = telebot.TeleBot(token=token)

def anek(message):
    if message.text.lower() == "да":
        bot.send_message(message.chat.id, "Купил мужик шляпу, а она ему как раз.")
    else:
        bot.send_message(message.chat.id, "Ну как хочешь :(")


@bot.message_handler(content_types=["text"])
def echo(message):
    if message.text.lower() == "привет":
        m = bot.send_message(message.chat.id, "Хочешь анек расскажу?")
        bot.register_next_step_handler(m, anek)

bot.polling(none_stop=True)


