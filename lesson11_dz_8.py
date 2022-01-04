# 1. Написать функцию которой передается один параметр - список строк my_list.
# Функция возвращает новый список в котором содержаться
# элементы из my_list у которых первый символ - буква "a".

def get_list_startswith_a(my_list):
    new_list = [word for word in my_list if word.startswith("a")]
    return new_list


my_list = ["wqe", "asd", "qaz", "az"]
res_1 = get_list_startswith_a(my_list)
print(res_1)


# 2. Написать функцию которой передается один параметр - список строк my_list.
# Функция возвращает новый список в котором содержаться
# элементы из my_list в которых есть символ - буква "a" на любом месте.

def get_list_contains_a(my_list):
    new_list = [word for word in my_list if "a" in word]
    return new_list


my_list = ["wqe", "asd", "qaz", "az"]
res_2 = get_list_contains_a(my_list)
print(res_2)


# 3. Написать функцию которой передается один параметр - список строк my_list в
# котором могут быть как строки (type str) так и целые числа (type int).
# Например [1, 2, 3, "11", "22", 33, "one"]
# Функция возвращает новый список в котором содержаться только строки из my_list.

def get_list_with_str(my_list):
    new_list = [word for word in my_list if type(word) is str]
    return new_list


my_list = ["wqe", "asd", 3, 45, "qaz", "az"]
res_3 = get_list_with_str(my_list)
print(res_3)


# 4. Написать функцию которой передается один параметр - строка my_str.
# Функция возвращает список в котором содержаться те символы из my_str,
# которые встречаются в строке только один раз.
# Т.е. для строкb "qqweeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeerrty" ответ должен быть ["w", "t", "y"]

def get_unique_one_symbols(my_str):
    new_list = [symbol for symbol in set(my_str) if my_str.count(symbol) == 1]
    return new_list


my_str = "qqweeerrty"
res_4 = get_unique_one_symbols(my_str)
print(res_4)


# 5. Написать функцию которой передается два параметра - две строки.
# Функция возвращает список в который поместить те символы,
# которые есть в обеих строках хотя бы раз.
# Т.е. для строк "qqwwerrttyy" и "qweeeeeee123" ответ должен быть ["q", "w", "e"]

def get_common_symbols(first_str, second_str):
    return list(set(first_str).intersection(set(second_str)))


first_str = "qqwwerrttyy"
second_str = "qweeeeeee123"
res_5 = get_common_symbols(first_str, second_str)
print(res_5)


# 6. Написать функцию которой передается два параметра - две строки.
# Функция возвращает список в который поместить те символы, которые есть в обеих строках,
# но в каждой только по одному разу.
# Т.е. для строк "qwwwwerrrrtyyyy" и "qweeeeeeerty123" ответ должен быть ["q", "t"]

def get_common_unique_symbols(first_str, second_str):
    new_list = []
    for symbol in get_common_symbols(first_str, second_str):
        if first_str.count(symbol) == second_str.count(symbol) == 1:
            new_list.append(symbol)
    return new_list


first_str = "qwwwwerrrrtyyyy"
second_str = "qweeeeeeerty123"
res_6 = get_common_unique_symbols(first_str, second_str)
print(res_6)

# 7*. Даны списки names и domains (создать самостоятельно).
# Написать функцию create_email для генерирования e-mail в формате:
# фамилия.число_от_100_до_999@строка_букв_длинной_от_5_до_7_символов.домен
# фамилию и домен брать случайным образом из заданных списков переданных в функцию в виде параметров.
# Строку и число генерировать случайным образом.
#
# Пример использования функции:
import random
from string import ascii_lowercase as alphabet


def create_email(domains, names):
    name = random.choice(names)
    domain = random.choice(domains)
    len_str = random.randint(5, 7)
    rand_int = random.randint(100, 999)
    rand_str = "".join([random.choice(alphabet) for _ in range(len_str)])
    e_mail = f"{name}.{rand_int}@{rand_str}.{domain}"
    return e_mail


names = ["king", "miller", "kean"]
domains = ["net", "com", "ua"]
e_mail = create_email(domains, names)
print(e_mail)
# >>>miller.249@sgdyyur.com
