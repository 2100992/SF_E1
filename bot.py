from telegram_bot import TOKEN, User
import telebot

bot = telebot.TeleBot(TOKEN)
users = {}

@bot.message_handler(commands=['start'])
def start_message(message):
    # print(f'dir(message.chat.id) = {dir(message.chat.id)}')
    print(f'message.chat.id = {message.chat.id}')

    # users[message.chat.id] = User(message.chat.id)
    # user = users[message.chat.id]

    # print(f'username = {user.username}')
    # print(f'first_name = {user.first_name}')
    # print(f'last_name = {user.last_name}')

    # bot.send_message(message.chat.id, f'Привет {user.username}, ты написал мне /start')
    bot.send_message(message.chat.id, f'Привет {message.chat.username}, ты написал мне /start')

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'Сыграем в игру':
        bot.send_message(message.chat.id, 'Привет, мой создатель')
    elif message.text == 'Пока':
        bot.send_message(message.chat.id, 'Прощай, создатель')

bot.polling()
