"""
1) У вас есть переменная my_str, тип - str. И переменная my_symbol, тип - str.
Напечатать ЧИСЛО сколько раз my_symbol встречается в my_str.
Пример:  my_str="blablacar", my_symbol="bla".
Вывод на экран:
2
"""
my_str="blablacarbla"
my_symbol="bla"
result = my_str.count(my_symbol)
print(result)

"""
2) У вас есть переменная my_str, тип - str. И переменная my_symbol, тип - str. 
Напечатать столько раз my_symbol, сколько он встречается в my_str. 
Пример:  my_str="blablacar", my_symbol="bla". 
Вывод на экран:
bla
bla
"""
my_str = "blablacarbla"
my_symbol = "bla"
for i in range(my_str.count(my_symbol)):
    print(my_symbol)

print("----------------------")

result = my_str.count(my_symbol)
res = [my_symbol] * result
print(res, *res, sep="\n")
# print((f"{my_symbol}\n"*result).strip(), end="")  # сложный способ

print("----------------------")

first, second, *_ = (100, 20, 30, 40)
print(first, second, _ )

my_list = [1, 2, 3, 4]
print(*my_list, sep="\n")

"""
3) У вас есть переменная my_str, тип - str. 
Большая и маленькая буква считается как один символ.
Напечатать ЧИСЛО сколько РАЗНЫХ символов встречается в my_str.  
Пробелы, запятые и т.д. считаем тоже как символы.
Пример:  my_str="bla BLA car". 
Вывод на экран:
6
"""
my_str = "bla BLA car"
# my_str = my_str.lower()  # переменную my_str можно переписать, если она не нужна
my_set = set(my_str.lower())
result = len(my_set)
print(result)


my_str = "bla BLA car"
bean = []
for symbol in my_str.lower():
    if symbol not in bean:
        bean.append(symbol)
result = len(bean)
print(result)




"""
4)
Дана строка my_str и пустой список my_list.
Заполнить my_list символами из my_str, 
которые стоят на четных местах в строке (считаем с 0)
"""
my_str = "qwertyASDFGH"
my_list = []
print(id(my_list))
# my_list += list(my_str[::2])  # добавляет список к существующему списку
my_list.extend(list(my_str[::2]))
print(id(my_list), my_list)

value = 2
value += 1

"""
5)
Дана строка my_str, список str_index целых чисел в диапазоне от 
0 до длинны строки минус 1, пустой список my_list.
Заполнить my_list символами из my_str, которые стоят на местах с 
индексами из str_index
"""
my_str = "qwerty123456"
str_index = [1, 3, 11, 0, 5, 5, 3, 2]
my_list = []

for index in str_index:
    my_list.append(my_str[index])
print(my_list)



"""
6)
Дано целое число (тип int). Определить сколько цифр в этом числе.
"""
number = 128973816581735168456287359129834092876582634

result = len(str(number))
print(result)

"""
7)
Дано целое число (тип int). Определить наибольшую цифру в этом числе.
"""
number = 2873816581735168456287351283402876582634

result = max(str(number))
print(result)

my_str = "123asd{"
print(max(my_str), ord("1"), chr(123))

"""
8)
Дано целое число (тип int). Составить число (int) с цифрами в обратном порядке.
"""
number = 2873816581735168456287351283402876582634

result = int(str(number)[::-1])
print(result, type(result))
"""
9)
Дано целое число (тип int). Составить число с цифрами в порядке возрастания(убывания).
"""

number = 2873816581735168456287351283402876582634

result = sorted(str(number), reverse=True)
res_int = int("".join(result))
print(res_int)


# генератор списков


res_list = []
for number in range(1, 11):
    # numb_sq = number ** 2
    # res_list.append(numb_sq)
    res_list.append(number ** 2)  # можно писать вложенные конструкции, главное знать меру ))
print(res_list)

res_list = [number ** 2 for number in range(1, 11)]
print(res_list)

my_str = "bla BLA car"
result = [symbol for symbol in my_str if symbol.isupper()]
print(result)

my_list = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
res = []
for my_tuple in my_list:
    this_tuple = (my_tuple[0], my_tuple[1], 100)
    # this_tuple = (*my_tuple[:-1], 100)  # можно воспользоваться распаковкой объекта
    res.append(this_tuple)
# res = [my_tuple[:-1] + (100,) for my_tuple in my_list]
print(res)

# тернарный оператор
from random import randint

value = randint(1, 6)

if value == 6:
    prize = 1000
else:
    prize = 0

prize = 1000 if value == 6 else 0
print(prize)
