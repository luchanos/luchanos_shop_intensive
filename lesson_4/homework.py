"""
Домашнее задание: усовершенствуйте скрипт из прошлого домашнего задания. Разработайте систему для долговременного
хранения данных в виде файла, а также сделайте так, чтобы функциональность вашего скрипта использовала этот файл.

Подсказка: теперь при создании новой записи должна производиться соответствующая запись в файл (аналогично с другими
операциями).
"""
import json

with open("notebook.json", "r") as all_deals_file:
    all_deals = json.load(all_deals_file)  # тут будем хранить все наши дела

new_id = int(max(all_deals.keys() or [0, ]))  # тут будем хранить айдишник для следующего дела
valid_answers = {"1", "2", "3", "4"}


def show_all_deals():
    with open("notebook.json", "r") as notebook_data:
        deal_dict = json.load(notebook_data)
        for el in deal_dict.items():
            print(el[1])


def get_deal_id_from_user():
    while True:
        deal_id = input("Enter deal id [required]: ")
        if not deal_id.isdigit():
            print("Sorry, deal id should be a int number!")
            continue  # уходим на следующую итерацию
        break
    return deal_id


def get_deal_by_id():
    deal_id = get_deal_id_from_user()
    if deal_id not in all_deals:
        print(f"The notebook has no deal with that id: {deal_id}")
    else:
        print(all_deals[deal_id])


def delete_deal_by_id():
    deal_id = get_deal_id_from_user()
    if deal_id not in all_deals:
        print(f"The notebook has no deal with that id: {deal_id}")
    else:
        del all_deals[deal_id]

        with open("notebook.json", "w") as all_deals_file:
            json.dump(all_deals, all_deals_file, indent=4, ensure_ascii=False)  # тут будем хранить все наши дела

        show_all_deals()


def edit_deal_by_id():
    """Задача со звёздочкой"""

    edit_choice = {
        "1": "description",
        "2": "responsible",
        "3": "date"
    }

    deal_id = get_deal_id_from_user()
    if deal_id not in all_deals:
        print(f"The notebook has no deal with that id: {deal_id}")
    else:
        print(all_deals[deal_id])

        while True:
            modify = input("What do you want to edit?\n"
                           "1. description\n"
                           "2. responsible\n"
                           "3. date\n")

            if modify not in {"1", "2", "3"}:
                print("Sorry, I don't understand you ;(")
                continue
            break

        new_value = input(f"Please, enter new value for {edit_choice[modify]}: ")
        all_deals[deal_id][edit_choice[modify]] = new_value

        with open("notebook.json", "w") as all_deals_file:
            json.dump(all_deals, all_deals_file, indent=4, ensure_ascii=False)  # тут будем хранить все наши дела

    show_all_deals()


def create_new_deal():
    global new_id

    while True:
        description = input("Enter deal description [required]: ")
        if description == "":
            print("Sorry, deal description should not be empty!")
            continue  # уходим на следующую итерацию
        break

    responsible = input("Enter deal responsible person [or keep empty]: ")
    date = input("Enter deal date [or keep empty]: ")

    deal_dict = {
        "description": description,
        "responsible": responsible or None,
        "date": date or None
    }

    new_id += 1
    all_deals[str(new_id)] = deal_dict

    with open("notebook.json", "w") as all_deals_file:
        json.dump(all_deals, all_deals_file, indent=4, ensure_ascii=False)  # тут будем хранить все наши дела

    show_all_deals()


CHOICE_MAPPER = {
    "1": create_new_deal,
    "2": get_deal_by_id,
    "3": edit_deal_by_id,
    "4": delete_deal_by_id
}


# организуем большой бесконечный цикл для работы нашей программы
while True:
    answer = input("1. Create new deal [1]\n"
                   "2. Get deal by id [2]\n"
                   "3. Edit deal by id [3]\n"
                   "4. Delete deal by id [4]\n"
                   "5. Quit [q/Q]:\n")
    if answer.lower() == "q":
        print("Exiting program...")
        break
    elif answer not in valid_answers:
        print("Sorry, I don't understand you ;(")
        continue  # уходим на следующую итерацию

    # повышаем гибкость нашего кода
    action_for_execution = CHOICE_MAPPER.get(answer)
    if action_for_execution is not None:
        action_for_execution()


print("End of program!")
