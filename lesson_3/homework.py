"""
Домашнее задание: усовершенствуйте скрипт из прошлого домашнего задания. Проведите рефакторинг кода и обособьте
некоторые блоки кода в отдельные функции. Дополните функциональность вашего ежедневника.

Дополнительные опции:
- вывод на экран информации о деле по его id;
- удаление дела по его id;
- редактирование дела по его id: описание, дата, исполнитель.
"""

new_id = 0  # тут будем хранить айдишник для следующего дела
all_deals = {}  # тут будем хранить все наши дела
valid_answers = {"1", "2", "3", "4"}


def show_all_deals():
    for deal in all_deals.items():
        print(deal)


def get_deal_by_id():
    while True:
        deal_id = input("Enter deal id [required]: ")
        if not deal_id.isdigit():
            print("Sorry, deal id should be a int number!")
            continue  # уходим на следующую итерацию
        break

    deal_id = int(deal_id)
    if deal_id not in all_deals:
        print(f"The notebook has no deal with that id: {deal_id}")
    else:
        print(all_deals[deal_id])


def delete_deal_by_id():
    while True:
        deal_id = input("Enter deal id [required]: ")
        if not deal_id.isdigit():
            print("Sorry, deal id should be a int number!")
            continue  # уходим на следующую итерацию
        break

    deal_id = int(deal_id)
    if deal_id not in all_deals:
        print(f"The notebook has no deal with that id: {deal_id}")
    else:
        del all_deals[deal_id]

    show_all_deals()


def edit_deal_by_id():
    """Задача со звёздочкой"""

    edit_choice = {
        "1": "description",
        "2": "responsible",
        "3": "date"
    }

    while True:
        deal_id = input("Enter deal id [required]: ")
        if not deal_id.isdigit():
            print("Sorry, deal id should be a int number!")
            continue  # уходим на следующую итерацию
        break

    deal_id = int(deal_id)
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

            new_value = input(f"Please, enter new value for {edit_choice[modify]}: ")
            all_deals[deal_id][edit_choice[modify]] = new_value
            break
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

    all_deals[new_id] = deal_dict
    new_id += 1

    show_all_deals()


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

    if answer == "1":
        create_new_deal()
    elif answer == "2":
        get_deal_by_id()
    elif answer == "3":
        edit_deal_by_id()
    elif answer == "4":
        delete_deal_by_id()


print("End of program!")
