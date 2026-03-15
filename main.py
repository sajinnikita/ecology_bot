import os

from config import TOKEN
import telebot
from random import choice
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id,"""Введи команду /image и получи мем про экологию
Введи команду /user и получи картинку от пользователей
Или отправь свою картинку """)
@bot.message_handler(commands=['image'])
def send_image(message):
    images = os.listdir('images')
    if images:
        image = choice(images)
        bot.send_photo(message.chat.id, open(os.path.join('images', image), 'rb'))
    else:
        bot.send_message(message.chat.id,"Автор не скачал картинки")
@bot.message_handler(commands=['user'])
def send_user(message):
    users = os.listdir('users_images')
    if users:
        user = choice(users_images)
        bot.send_photo(message.chat.id, open(os.path.join('users_images', user), 'rb'))
    else:
        bot.send_message(message.chat.id,"Пользователи не отправили картинки")
@bot.message_handler(content_types=['photo'])
def get_photo(message):
    photo = message.photo[-1]
    file_info = bot.get_file(photo.file_id)
    download_file = bot.download_file(file_info.file_path)
    with open(f'users_images/{file_info.file_id}.jpg', 'wb') as f:
        f.write(download_file)
    bot.reply_to(message, "фото сохранено")

bot.polling(none_stop=True)