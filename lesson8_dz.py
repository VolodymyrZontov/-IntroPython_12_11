# 1. Дано целое число (int). Определить сколько нулей в этом числе.
number = 1200300400
number = str(number)
my_symbol = "0"
result = number.count(my_symbol)
print(result)

# 2. Дано целое число (int). Определить сколько нулей в конце этого числа.
# Например для числа 1002000 - три нуля
num = 1200300400
num = str(num)
result_num = (len(num) - len(num.rstrip("0")))

# 3. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list по следующему правилу:
# Если строка стоит на нечетном месте в my_list, то ее заменить на
# перевернутую строку. "qwe" на "ewq".
# Если на четном - оставить без изменения.

my_list = ["qwe", "rty", "uio"]
my_list_new = list()
for idx in range(len(my_list)):
    new_value = my_list[idx][::-1] if idx % 2 else my_list[idx]
    my_list_new.append(my_list[idx])
print(my_list_new)

# 4. Дан список my_list. СОЗДАТЬ НОВЫЙ список new_list у которого первый элемент из my_list
# стоит на последнем месте в new_list. Если my_list [1,2,3,4], то new_list [2,3,4,1]

my_list = [1,2,3,4]
new_list = my_list[:-1] + [my_list[0]]
print(new_list)

# 5.Дан список my_list. В ЭТОМ списке первый элемент переставить на последнее место.
# [1,2,3,4] -> [2,3,4,1]. Пересоздавать список нельзя! (используйте метод pop)

my_list = ["POTATO", "TOMATO", "MEAT", "CHEESE"]
my_list.append(my_list.pop(0))
print(my_list)

# 6. Дана строка в которой есть числа (разделяются пробелами).
# Например "43 больше чем 34 но меньше чем 56". Найти сумму ВСЕХ ЧИСЕЛ (А НЕ ЦИФР) в этой строке.
# Для данного примера ответ - 133. (используйте split и проверку isdigit)
test_str = "43 больше     чем 34 но меньше чем 56"

numb_list = []
for word in test_str.split():
    if word.isdigit():
        numb_list.append(int(word))
result = sum(numb_list)

# 7. Дана строка my_str в которой символы МОГУТ повторяться и два символа l_limit, r_limit,
# которые точно находятся в этой строке. Причем l_limit левее чем r_limit.
# В переменную sub_str поместить НАИБОЛЬШУЮ часть строки между этими символами.
# my_str = "My long string", l_limit = "o", r_limit = "g" -> sub_str = "ng strin".

my_str = "My long string"
l_limit = "o"
r_limit = "g"
result = my_str[my_str.find(l_limit)+1: my_str.rfind(r_limit)]
print(f"Substring: {result}")

# 8. Дана строка my_str. Разделите эту строку на пары из двух символов и поместите эти пары в список.
# Если строка содержит нечетное количество символов, пропущенный второй символ последней пары должен
# быть заменен подчеркиванием ('_'). Примеры: 'abcd' -> ['ab', 'cd'], 'abcde' -> ['ab', 'cd', e_']
# (используйте срезы длинны 2)
my_str = "qwert"
res_list = list()

temp = my_str + '_' if len(my_str) % 2 else my_str

for idx in range(0, len(temp), 2):
    res_list.append(temp[idx:idx + 2])


# 9. Дан список чисел. Определите, сколько в этом списке элементов,
# которые больше суммы двух своих соседей (слева и справа), и НАПЕЧАТАЙТЕ КОЛИЧЕСТВО таких элементов.
# Крайние элементы списка никогда не учитываются, поскольку у них недостаточно соседей.
# Для списка [2,4,1,5,3,9,0,7] ответом будет 3 потому что 4 > 2+1, 5 > 1+3, 9>3+0.

my_list = [2,4,1,5,3,9,0,7]
result = 0

for index in range(1, len(my_list) - 1):
    if my_list[index] > my_list[index - 1] + my_list[index + 1]:
        result += 1

# 10. Дан список словарей persons в формате [{"name": "John", "age": 15}, ... ,{"name": "Jack", "age": 45}]
# а) Определить возраст самого молодого человека и поместить в новый список имена всех людей,
# чей возраст совпадает с этим минимальным возрастом.
# б) Определить самое длинное имя и поместить в новый список имена всех людей,
# чье имя по длине совпадает с этой длиной.
# в) Посчитать среднее количество лет всех людей из списка.

persons = [{"name": "John", "age": 15},
           {"name": "Anna", "age": 23},
           {"name": "Dan", "age": 5},
           {"name": "Maximusss", "age": 24},
           {"name": "Olgha", "age": 25},
           {"name": "Volodymyr", "age": 5},
           {"name": "Jack", "age": 45}]

ages = []
names_lens = []

for person_dict in persons:
    ages.append(person_dict["age"])
    names_lens.append(len(person_dict["name"]))

min_age = min(ages)
max_len_name = max(names_lens)

for person_dict in persons:
    if person_dict["age"] == min_age:
        print(person_dict["name"])

for person_dict in persons:
    if len(person_dict["name"]) == max_len_name:
        print(person_dict["name"])

mean_age = sum(ages) / len(ages)
print(mean_age)