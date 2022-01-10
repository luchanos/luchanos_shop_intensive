"""
Домашнее задание: усовершенствуйте скрипт из прошлого домашнего задания. Вы уже умеете обрабатывать информацию
из консоли и записывать данные в файл. Теперь ваша задача на базе библиотеки PytelegramBotApi написать скрипт, который
мог бы принимать информацию из Телеграм-бота с сохранением всей функциональности консольного скрипта.

Подсказка: теперь учтите, что функции, которые вы использовали раньше для вывода информации в консоль должны
эту информацию отдавать в бота. Вспомните про ключевое слово return!
"""

import json
import telebot

with open("notebook.json", "r") as all_deals_file:
    all_deals = json.load(all_deals_file)  # тут будем хранить все наши дела

new_id = int(max(all_deals.keys() or [0, ]))  # тут будем хранить айдишник для следующего дела
valid_answers = {"1", "2", "3", "4"}

TOKEN = "2104221180:AAGmwLGyb1m8fTnePreXS5bruo_HaW2Vj_w"

bot = telebot.TeleBot(TOKEN)

MAIN_MENU = "1. Create new deal: /create_new_deal <description>|<responsible>|<date>\n" \
            "2. Get deal by id: /get_deal_by_id <id>\n" \
            "3. Edit deal by id: /edit_deal <id>|<parameter>|<new_value>\n" \
            "4. Delete deal by id: /delete_deal_by_id <id>\n"


@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(message, text=MAIN_MENU)


def show_all_deals(message):
    with open("notebook.json", "r") as notebook_data:
        deal_dict = json.load(notebook_data)
        bot.reply_to(message, text=str(deal_dict))


@bot.message_handler(commands=["get_deal_by_id"])
def get_deal_by_id(message):
    deal_id = message.text.split()[1]
    if deal_id not in all_deals:
        print(f"The notebook has no deal with that id: {deal_id}")
    else:
        bot.reply_to(message, text=str(all_deals[deal_id]))


@bot.message_handler(commands=["delete_deal_by_id"])
def delete_deal_by_id(message):
    deal_id = message.text.split()[1]
    if deal_id not in all_deals:
        print(f"The notebook has no deal with that id: {deal_id}")
    else:
        del all_deals[deal_id]

        with open("notebook.json", "w") as all_deals_file:
            json.dump(all_deals, all_deals_file, indent=4, ensure_ascii=False)  # тут будем хранить все наши дела

        show_all_deals(message)


@bot.message_handler(commands=["edit_deal"])
def edit_deal_by_id(message):

    raw_data = message.text.split()[1:][0]
    deal_id, parameter, new_value = raw_data.split("|")

    all_deals[deal_id][parameter] = new_value

    with open("notebook.json", "w") as all_deals_file:
        json.dump(all_deals, all_deals_file, indent=4, ensure_ascii=False)  # тут будем хранить все наши дела

    show_all_deals(message)


@bot.message_handler(commands=["create_new_deal"])
def create_new_deal(message):
    global new_id

    raw_data = message.text.split()[1:][0]
    description, responsible, date = raw_data.split("|")

    deal_dict = {
        "description": description,
        "responsible": responsible or None,
        "date": date or None
    }

    new_id += 1
    all_deals[str(new_id)] = deal_dict

    with open("notebook.json", "w") as all_deals_file:
        json.dump(all_deals, all_deals_file, indent=4, ensure_ascii=False)  # тут будем хранить все наши дела

    show_all_deals(message)


CHOICE_MAPPER = {
    "1": create_new_deal,
    "2": get_deal_by_id,
    "3": edit_deal_by_id,
    "4": delete_deal_by_id
}


# организуем большой бесконечный цикл для работы нашей программы
while True:
    try:
        print("Starting bot!")
        bot.polling()
    except Exception as err:
        print(err)
