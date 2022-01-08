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

    create_new_deal()
    show_all_deals()

print("End of program!")
