"""
Домашнее задание: усовершенствуйте скрипт из прошлого домашнего задания. Вы уже умеете ...
теперь прикручиваем next step handler
"""

import json
import telebot

with open("notebook.json", "r") as all_deals_file:
    all_deals = json.load(all_deals_file)  # тут будем хранить все наши дела

new_id = int(max(all_deals.keys() or [0, ]))  # тут будем хранить айдишник для следующего дела
valid_answers = {"1", "2", "3", "4"}

TOKEN = "2104221180:AAGmwLGyb1m8fTnePreXS5bruo_HaW2Vj_w"

bot = telebot.TeleBot(TOKEN)

MAIN_MENU = "1. Create new deal: /create_new_deal\n" \
            "2. Get deal by id: /get_deal_by_id\n" \
            "3. Edit deal by id: /edit_deal\n" \
            "4. Delete deal by id: /delete_deal_by_id\n"


@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(message, text=MAIN_MENU)


def show_all_deals(message):
    res = ""
    with open("notebook.json", "r") as notebook_data:
        deal_dict = json.load(notebook_data)
        for deal_id in deal_dict:
            res += f"\n{deal_id}:\ndescription: {deal_dict[deal_id]['description']}\n" \
                   f"responsible: {deal_dict[deal_id]['responsible']}\n" \
                   f"date: {deal_dict[deal_id]['date']}\n"
        bot.reply_to(message, text=res)


def ask_deal_id_2(message):
    deal_id = message.text
    with open("notebook.json", "r") as notebook_data:
        deal_dict = json.load(notebook_data)
        if deal_id not in deal_dict:
            bot.reply_to(message, text=f"The notebook has no deal with that id: {deal_id}")
        else:
            bot.reply_to(message, text=f"\n{deal_id}:\ndescription: {deal_dict[deal_id]['description']}\n"
                                       f"responsible: {deal_dict[deal_id]['responsible']}\n"
                                       f"date: {deal_dict[deal_id]['date']}\n")


@bot.message_handler(commands=["get_deal_by_id"])
def get_deal_by_id(message):
    bot.reply_to(message, text="Enter deal_id:")
    bot.register_next_step_handler(message, ask_deal_id_2)


def ask_and_delete(message):
    deal_id = message.text
    with open("notebook.json", "r") as notebook_data:
        deal_dict = json.load(notebook_data)
    if deal_id not in deal_dict:
        bot.reply_to(message, text=f"The notebook has no deal with that id: {deal_id}")
    else:
        del deal_dict[deal_id]

        with open("notebook.json", "w") as all_deals_file:
            json.dump(deal_dict, all_deals_file, indent=4, ensure_ascii=False)  # тут будем хранить все наши дела

        show_all_deals(message)


@bot.message_handler(commands=["delete_deal_by_id"])
def delete_deal_by_id(message):
    bot.reply_to(message, text="Enter id:")
    bot.register_next_step_handler(message, ask_and_delete)


def ask_new_value(message, deal_id, edit_key):
    new_value = message.text

    with open("notebook.json", "r") as notebook_data:
        deal_dict = json.load(notebook_data)

    deal_dict[deal_id][edit_key] = new_value

    with open("notebook.json", "w") as all_deals_file:
        json.dump(deal_dict, all_deals_file, indent=4, ensure_ascii=False)  # тут будем хранить все наши дела

    show_all_deals(message)


def ask_edit_key(message, deal_id):
    edit_key = message.text

    params = {
        "1": "description",
        "2": "responsible",
        "3": "date"
    }

    if edit_key not in params:
        bot.reply_to(message, text=f"Wrong parameter for editing!")
    else:
        bot.reply_to(message, text=f"Please, enter new value for '{params[edit_key]}' parameter:")
        bot.register_next_step_handler(message, ask_new_value, deal_id, params[edit_key])


def ask_deal_id(message):
    deal_id = message.text
    with open("notebook.json", "r") as notebook_data:
        deal_dict = json.load(notebook_data)
    if deal_id not in deal_dict:
        bot.reply_to(message, text=f"The notebook has no deal with that id: {deal_id}")
    else:
        bot.reply_to(message, text="Choose parameter which you want to change?\n"
                                   "1. description [1]\n"
                                   "2. responsible [2]\n"
                                   "3. date [3]\n")
        bot.register_next_step_handler(message, ask_edit_key, deal_id)


@bot.message_handler(commands=["edit_deal"])
def edit_deal_by_id(message):
    bot.reply_to(message, text="Which id?")
    bot.register_next_step_handler(message, ask_deal_id)


def set_new_deal(message, description, responsible):
    global new_id
    new_id += 1

    date = message.text

    with open("notebook.json", "r") as notebook_data:
        deal_dict = json.load(notebook_data)

    deal_dict[new_id] = {
        "description": description,
        "responsible": responsible,
        "date": None if date == "no" else date
    }

    with open("notebook.json", "w") as all_deals_file:
        json.dump(deal_dict, all_deals_file, indent=4, ensure_ascii=False)  # тут будем хранить все наши дела

    show_all_deals(message)


def ask_responsible(message, description):
    bot.reply_to(message, text="Enter date or set 'no' to set None:")
    responsible = message.text
    bot.register_next_step_handler(message, set_new_deal, description, None if responsible == "no" else responsible)


def ask_description(message):
    bot.reply_to(message, text="Enter responsible person name or set 'no' to set None:")
    description = message.text
    bot.register_next_step_handler(message, ask_responsible, description)


@bot.message_handler(commands=["create_new_deal"])
def create_new_deal(message):
    bot.reply_to(message, text=f"Enter description:")
    bot.register_next_step_handler(message, ask_description)


# организуем большой бесконечный цикл для работы нашей программы
while True:
    try:
        print("Starting bot!")
        bot.polling()
    except Exception as err:
        print(err)
