from telegram_bot import TOKEN, User
import telebot

bot = telebot.TeleBot(TOKEN)
users = {}

@bot.message_handler(commands=['start'])
def start_message(message):
    print(f'dir(message.chat) = {dir(message.chat)}')

    users[message.chat.id] = User(message.chat.id)

    bot.send_message(message.chat.id, 'Привет, ты написал мне /start')

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'Сыграем в игру':
        bot.send_message(message.chat.id, 'Привет, мой создатель')
    elif message.text == 'Пока':
        bot.send_message(message.chat.id, 'Прощай, создатель')

bot.polling()
