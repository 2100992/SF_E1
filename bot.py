from gallows import Round
from h import WORDS_SET
from telegram_bot import TOKEN, User
import telebot

bot = telebot.TeleBot(TOKEN)
users = {}


def get_user(message):
    if not users.get(message.chat.id):
        users[message.chat.id] = User(message.chat)
    return users[message.chat.id]


@bot.message_handler(commands=['start'])
def start_message(message):

    user = get_user(message)

    bot.send_message(
        user.id, f'Привет, {user.username}! Хочешь сыграем в игру /gallows ?')


@bot.message_handler(commands=['gallows'])
def gallows_game_message(message):
    user = get_user(message)

    user_round = user.user_round = Round(WORDS_SET)

    bot.send_message(
        user.id, f'Отлично! Я загадал слово {user_round.hint} . \n Назови свою букву!')


@bot.message_handler(content_types=['text'])
def send_text(message):
    user = get_user(message)

    if message.text and user.user_round:
        user.user_round.set_letter(message.text)
        message = str(user.user_round)
    
    if user.user_round.win or user.user_round.game_over:
        user.user_round = None

    bot.send_message(user.id, message)



bot.polling()
