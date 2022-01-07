"""
Домашнее задание: на основе прошлого домашнего задания доработать скрипт таким образом,
чтобы запрашивать у пользователя информацию о новом деле. Пример:

Enter deal description: make something valuable
Enter deal date (optional): 01-01-2023
Enter deal responsible person: Nikolai

После добавления каждого нового дела на экран нужно вывести полный список всех дел ежедневника.
"""

new_id = 0  # тут будем хранить айдишник для следующего дела
all_deals = {}  # тут будем хранить все наши дела

# организуем большой бесконечный цикл для работы нашей программы
while True:
    answer = input("Would you like to enter new deal to system? [yes/no]: ")
    if answer.lower() == "no":
        break
    elif answer.lower() != "yes":
        print("Sorry, I don't understand you ;(")
        continue  # уходим на следующую итерацию

    description = input("Enter deal description [required]: ")
    if description == "":
        print("Sorry, deal description should not be empty!")
        continue  # уходим на следующую итерацию

    responsible = input("Enter deal responsible person [or keep empty]: ")
    date = input("Enter deal date [or keep empty]: ")

    deal_dict = {
            "description": description,
            "responsible": responsible or None,
            "date": date or None
        }

    all_deals[new_id] = deal_dict
    new_id += 1

    # вывод всех дел на экран
    for deal in all_deals.items():
        print(deal)
