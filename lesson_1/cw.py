# int, float
a = 1  # так происходит присваивание значения в переменную
b = 1.0

# print - функция, позволяющая выводить информацию в консоль
print(a)
print(b)

# bool
c = True  # истина
d = False  # ложь
print(c)
print(d)

# str - строка
e = "Sample text"
e_1 = 'Sample text'
e_2 = 'a' # это тоже строка! в Python нет отдельного типа для единичного символа!

# Коллекции:
# list tuple set dict (список, кортеж, множество, словарь)
l = [1, 2, 3, 4]
t = (1, 2, 3, 4)
s = {1, 2, 3, 4}
d = {1: "orange",
     2: "apple",
     3: "pineapple"}

# списки, кортежи и строки поддерживают сложение внутри собственных типов:
print([1, 2, 3, 4] + [5, 6, 7, 8])
print((1, 2, 3, 4) + (5, 6, 7, 8))
print("abc" + "def")


print(s[2])  # выдаст ошибку
print(d[1], d[2], d[3])

# добавление элемента в конец списка
l.append(123123)

# добавление элемента в множество
s.add(1123123123)
print(s)

d[1] = l
print(d)

d_1 = {
    1: {
        "name": "orange",
        "manufacturer": "Romashka"
    },
    2: {
        "name": "orange",
        "manufacturer": "Solnyshko"
    },
    3: {
        "name": "pineapple",
        "manufacturer": "Zvezda"
    }
}

# if - условный оператор (если ..., то ..., иначе ...)
if a > 1:
    print("a is greater than 1")
else:  # опциональная часть - её может и не быть
    print("a is not greater than 1")

# с помощью if можно организовывать вложенные (каскадные) структуры:
if a > 1:
    print("a is greater than 1")
    if a > 3:
        print("a is greater than 3")
else:
    print("a is not greater than 1")

# while - цикл, выполняющийся до тех пор, пока условие истинно
cnt = 0

while cnt < 10:
    print("cnt is:", cnt)
    cnt = cnt + 1

# бесконечный цикл
while True:
    print("Это бесконечный цикл")

# цикл для обхода коллекций
for el in l:
    print("Мы достали из l очередной элемент", el, "и можем делать с ним что захотим")
    print("Например складывать его с единицей и получать в результате: ", el + 1)

# для словарей итерация происходит по ключам
for el in d:
    print(el)
