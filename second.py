import telebot
bot = telebot.TeleBot("6565221179:AAFBJrOeJBV9rjP_NGarCKNtXqR-yp0_EU4")
#bot = telebot.TeleBot("7107331036:AAF0-AgnOPA5_UTEprnfQ3YznRFau15sLdE")


@bot.message_handler()
def messagesend(message):
    bot.send_message(message.chat.id, "⛔️Бот на технических работах⛔️")


bot.polling(none_stop=True)