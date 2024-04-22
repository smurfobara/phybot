import telebot
bot = telebot.TeleBot("6565221179:AAFBJrOeJBV9rjP_NGarCKNtXqR-yp0_EU4")
from telebot import types
import textes
import time

VERSION = "0.1 Alpha"

@bot.message_handler(commands=["start"])
def start(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("Силы с определениями", callback_data="listOfPowers")
    btn2 = types.InlineKeyboardButton("Формулы сил", callback_data="listOfFormuls")
    markup.row(btn1, btn2)
    btn3 = types.InlineKeyboardButton("Калькулятор давления, плотности и силы", callback_data="calculator")
    markup.row(btn3)
    btn4 = types.InlineKeyboardButton("О разработке бота", callback_data="development")
    markup.row(btn4)
    bot.send_message(message.chat.id, "Привет!🙌\n Этот бот поможет тебе с физикой! Выбери что тебе нужно 👇👇", reply_markup=markup)
    
""" @bot.message_handler(commands=["calculatedensity"])
def massa(message):
    bot.send_message(message.chat.id, "Введите плотность в кг на м³")
    time.sleep(10)
    bot.message_handler()
    density = int(message.text)
    bot.send_message(message.chat.id, "Теперь объем в м³") 
    V = int(message.text)
    answer = density * V
    bot.send_message(message.chat.id, f"Масса равна {answer} кг.") """



@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == "listOfPowers":
        bot.send_message(callback.message.chat.id, "Список сил 👇👇👇")
        bot.send_message(callback.message.chat.id, textes.powers)
    elif callback.data == "listOfFormuls":
        bot.send_message(callback.message.chat.id, "Список формул к силам 👇👇")
        bot.send_message(callback.message.chat.id, textes.formuls)
    elif callback.data == "calculator":
        bot.send_message(callback.message.chat.id, 'Калькулятор пока не доступен, как говорится "Coming soon..."')
    elif callback.data == "development":
        bot.send_message(callback.message.chat.id, f"Развиваю бот в одиночку, по мере сил и возможностей. Версия на данный момент: {VERSION} \n Предложить идею: @smurfobara")
        bot.send_message(callback.message.chat.id, f"Список изменений на версию {VERSION}: \n Создание, проектирование и воссоздание начальных функций бота")





bot.polling(none_stop=True)
