import json

my_dict = {
    "first_key": 1,
    "second_key": 2,
    "third_key": {
        "inner_key_one": 11,
        "inner_key_two": 22
    }
}

with open("my_data.json", "w") as json_file:
    json.dump(my_dict, json_file, indent=4, ensure_ascii=False)

with open("my_data_2.json", "r") as json_file:
    my_data_from_json = json.load(json_file)

print(my_data_from_json)

# в json ключ может быть только строкой
# рассказать про всякие функции min, max
