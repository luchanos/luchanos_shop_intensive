# pip - менеджер пакетов
# requirements.txt - файл для сборки зависимостей

import telebot

TOKEN = "2104221180:AAGmwLGyb1m8fTnePreXS5bruo_HaW2Vj_w"

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["main"])
def main(message):
    bot.reply_to(message, text="Какой-то текст")


@bot.message_handler(commands=["splitter"])
def main_2(message):
    splitted_text = message.text.split()
    answer = "*".join(splitted_text)
    bot.reply_to(message, text=answer)


# основная задача - правильно обрабатывать входящую строчку
@bot.message_handler(commands=["main_3"])
def main_3(message):
    splitted_text = message.text.split()[1].split("|")
    answer = "*".join(splitted_text)
    bot.reply_to(message, text=answer)


while True:
    try:
        print("Starting bot!")
        bot.polling()
    except Exception as err:
        print(err)
