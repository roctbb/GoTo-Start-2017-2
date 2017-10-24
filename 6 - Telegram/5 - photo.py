import uuid
import telebot
from PIL import Image

token = "461633768:AAFg3dQCW4HhM3K76d9nM-Au0Ai0nNVfE_w"
bot = telebot.TeleBot(token=token)

def process(filename):
    img = Image.open(filename)
    box = (0, 0, img.width // 2, img.height)
    left = img.crop(box)
    left = left.transpose(Image.FLIP_LEFT_RIGHT)
    img.paste(left, (img.width // 2, 0))
    img.save(filename)

@bot.message_handler(content_types=['photo'])
def photo(message):
    # скачивание файла
    file_id = message.photo[-1].file_id
    path = bot.get_file(file_id)
    downloaded_file = bot.download_file(path.file_path)

    # узнаешь расширение и придумываем имя
    extn = '.' + str(path.file_path).split('.')[-1]
    name = 'images/' + str(uuid.uuid4()) + extn

    # создаем файл и записываем туда данные
    with open(name, 'wb') as new_file:
        new_file.write(downloaded_file)

    process(name)

    # открываем файл и отправляем его пользователю
    with open(name, 'rb') as new_file:
        bot.send_photo(message.chat.id, new_file.read())

bot.polling(none_stop=True)


