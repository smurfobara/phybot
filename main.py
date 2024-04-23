import telebot
bot = telebot.TeleBot("6565221179:AAFBJrOeJBV9rjP_NGarCKNtXqR-yp0_EU4")
#bot = telebot.TeleBot("7107331036:AAF0-AgnOPA5_UTEprnfQ3YznRFau15sLdE")
from telebot import types
import textes
import time

VERSION = "0.3 Alpha"

txt = open("users.txt")
contenttext = txt.read()
txt.close()

@bot.message_handler(commands=["start"])
def start(message):
    with open("users.txt", "a") as k:
        with open("users.txt") as s:
            contenttxt = s.read()
            finding = contenttxt.find(str(message.from_user.id))
            if int(finding) == -1:
                print(message.chat.id, file=k)
                print(f"appended!")
    s.close()
    k.close()
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("Силы с определениями и формулами", callback_data="listOfPowers")
    btn2 = types.InlineKeyboardButton("[НОВОЕ] Поиск", callback_data="find")
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


@bot.message_handler(commands=["find"])
def finding(message):
    text = str(message.text)
    text = text.lower()
    textmass = text.split()
    del textmass[0]
    if len(textmass) == 0:
        bot.send_message(message.chat.id, "⚠️ Укажите текст который пытаетесь найти /find [текст]")
    for word in textmass:
        if word in textes.power:
            bot.send_message(message.chat.id, textes.power)
        elif word in textes.powerEarth:
            bot.send_message(message.chat.id, textes.powerEarth)
        elif word in textes.powerVes:
            bot.send_message(message.chat.id, textes.powerVes)
        elif word in textes.PowerRavno:
            bot.send_message(message.chat.id, textes.PowerRavno)
        elif word in textes.powerTr:
            bot.send_message(message.chat.id, textes.powerTr)
        elif word in textes.powerUpr:
            bot.send_message(message.chat.id, textes.powerUpr)
        


@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == "listOfPowers":
        bot.send_message(callback.message.chat.id, "Список сил 👇👇👇")
        bot.send_message(callback.message.chat.id, textes.power + textes.powerTr + textes.powerEarth + textes.powerUpr + textes.powerVes + textes.PowerRavno)
    elif callback.data == "find":
        bot.send_message(callback.message.chat.id, "Новая функция: поиск! Пока может работать не очень стабильно, но в будущем все исправится! \n Для использования введите /find и текст, который пытаетесь найти.")
    elif callback.data == "calculator":
        bot.send_message(callback.message.chat.id, 'Калькулятор пока не доступен, как говорится "Coming soon..."')
    elif callback.data == "development":
        bot.send_message(callback.message.chat.id, f"Развиваю бот в одиночку, по мере сил и возможностей. Версия на данный момент: {VERSION} \n Предложить идею: @smurfobara")
        bot.send_message(callback.message.chat.id, f"Список изменений на версию {VERSION}: \n ПОИСК - первая версия поиска! \n Доработка и оптимизация кода")

@bot.message_handler(commands=["botclosing"])
def closing(message):
    global contenttext
    if message.from_user.id == 5893427261:
        with open("users.txt", "r") as l:
            contenttext = l.read()
            listoftext = contenttext.split()
        for listitem in listoftext:
            bot.send_message(listitem, "Бот будет временно недоступен по техническим причинам. Для связи: @smurfobara")
        l.close()

@bot.message_handler(commands=["botopening"])
def closing(message):
    global contenttext
    if message.from_user.id == 5893427261:
        with open("users.txt", "r") as l:
            contenttext = l.read()
            listoftext = contenttext.split()
        for listitem in listoftext:
            bot.send_message(listitem, "Бот снова работает✅")
        l.close()

@bot.message_handler(commands=["sendtxt"])
def sendtxt(message):
    if message.from_user.id == 5893427261:
        file = open("users.txt", "rb")
        bot.send_document(message.chat.id, file)
        file.close()

@bot.message_handler(commands=["sendmsgusers"])
def sendmessage(message):
    if message.from_user.id == 5893427261:
        text = message.text
        listtext = text.split()
        with open("users.txt", "r") as l:
            contenttext = l.read()
            listoftext = contenttext.split()
        del listtext[0]
        stringline = " ".join(listtext)
        for listitem in listoftext:
            print(listitem)
            print(listoftext)
            bot.send_message(listitem, stringline)
        l.close()
        bot.send_message(5893427261, "Рассылка завершена")

bot.polling(none_stop=True)
