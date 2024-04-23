import telebot
bot = telebot.TeleBot("6565221179:AAFBJrOeJBV9rjP_NGarCKNtXqR-yp0_EU4")
#bot = telebot.TeleBot("7107331036:AAF0-AgnOPA5_UTEprnfQ3YznRFau15sLdE")
from telebot import types
import textes
import time

VERSION = "0.5 Beta"


listMessages = []

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
    btn1 = types.InlineKeyboardButton("Список сил", callback_data="listOfPowers")
    btn2 = types.InlineKeyboardButton("[НОВОЕ] Поиск", callback_data="find")
    btn3 = types.InlineKeyboardButton("Калькулятор давления, плотности и силы", callback_data="calculator")
    btn4 = types.InlineKeyboardButton("О разработке бота", callback_data="development")
    btn5 = types.InlineKeyboardButton("Список определений", callback_data="listOfOprs")
    markup.row(btn1, btn5)
    markup.row(btn2)
    markup.row(btn3)
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
    lines = text.split()
    listPowers = textes.listPowers
    listOprs = textes.listOprs
    isfinded = None
    del lines[0]
    if len(lines) == 0:
        bot.send_message(message.chat.id, "⚠️ Укажите текст который пытаетесь найти /find [текст]")
    else:
        for word in lines:
            print("word in lines")
            for line in listPowers:
                print("line in textes")
                if word in line:
                    print("word in line")
                    bot.send_message(message.chat.id, line)
                    isfinded = True
                    print (isfinded)
                    break
        for word in lines:
            for line in listOprs:
                if word in line:
                    bot.send_message(message.chat.id, line)
                    break
        


@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    listOprs = textes.listOprs
    listPowers = textes.listPowers
    if callback.data == "listOfPowers":
        bot.send_message(callback.message.chat.id, "Список сил (пока не полный)👇👇👇")
        for index in listPowers:
            bot.send_message(callback.message.chat.id, index)
        bot.send_message(callback.message.chat.id, "Чтобы вернуться в меню нажмите здесь👉 /start")
    elif callback.data == "find":
        bot.send_message(callback.message.chat.id, "Новая функция: поиск! Пока может работать не очень стабильно, но в будущем все исправится! \n Для использования введите /find и текст, который пытаетесь найти.")
    elif callback.data == "calculator":
        bot.send_message(callback.message.chat.id, 'Калькулятор пока не доступен, как говорится "Coming soon..."')
    elif callback.data == "development":
        bot.send_message(callback.message.chat.id, f"Развиваю бот в одиночку, по мере сил и возможностей. Версия на данный момент: {VERSION} \n Предложить идею: @smurfobara")
        bot.send_message(callback.message.chat.id, f"Список изменений на версию {VERSION}: \n Переход в Beta \n Добавлен раздел 'определения' \n Полностью переработана и улучшена система поиска \n Доработка и оптимизация кода")
    elif callback.data == "listOfOprs":
        bot.send_message(callback.message.chat.id, "Список определений (пока не полный)👇👇👇")
        for index in listOprs:
            bot.send_message(callback.message.chat.id, index)
        bot.send_message(callback.message.chat.id, "Чтобы вернуться в меню нажмите здесь👉 /start")
        



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
