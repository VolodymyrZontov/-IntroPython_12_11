# сортировка по нескольким полям
# lambda, map, zip, filter
# regexp

from string import ascii_uppercase as alphabet


def create_points_dict(points):
    new_points = []
    letters = alphabet[:len(points)]
    for idx, point in enumerate(points):
        new_points.append({letters[idx]: point})
    return new_points


def sort_by_point(point):
    values = list(point.values())
    return values[0]


point_a = (2, 4, -6)
point_b = (1, -4, 3)
point_c = (2, 2, 1)
point_d = (1, -4, -3)

points = [point_a, point_b, point_c, point_d]

new_points = sorted(points)
print(new_points)

points_dict = create_points_dict(points)
print(points_dict)
new_points_dict = sorted(points_dict, key=sort_by_point)
print(new_points_dict)

#####################################################


def sort_by_name_and_age(item):
    name = item["name"]
    age = item["age"]
    return name, age


persons = [{"age": 32, "name": "John"},
           {"age": 32, "name": "Anna"},
           {"name": "Jack", "age": 42},
           {"name": "Jack", "age": 12},
           {"name": "Jacob", "age": 65}, ]

sort_list = sorted(persons, key=sort_by_name_and_age)
print(sort_list)


# regexp
import re
# pattern = r"[A-Z]{1}[a-z]+"  # Выбор имени
pattern = r'[0-9]+'  # Выбор года
my_str = "Jack Jacob 1234 Anna 1945 - 1998 John ??? QWERTY asdfgh"
result = re.findall(pattern, my_str)
print(result)

# lambda, map, zip, filter


def sort_by_age(item):
    return item["age"]


persons = [{"age": 32, "name": "John"},
           {"name": "Jack", "age": 12},
           {"name": "Jacob", "age": 65}, ]

sort_list = sorted(persons, key=lambda item: item["age"])
print(sort_list)

sort_list = sorted(persons, key=lambda x: (len(x["name"]), x["age"]))
print(sort_list)

###########################

def sort_by_name_and_age(item):
    name = item["name"]
    age = item["age"]
    return name, age


persons = [{"age": 32, "name": "John"},
           {"age": 32, "name": "Anna"},
           {"name": "Jack", "age": 42},
           {"name": "Jack", "age": 12},
           {"name": "Jacob", "age": 65}, ]

sort_list = sorted(persons, key=lambda x: (x["age"], x["name"]))
print(sort_list)

# MAP
# Задача 1
def square(value):
    return value ** 2

def add(v1, v2):
    return v1 + v2

my_list = [2, 4, 6, 1, 5]
my_list_2 = [2, 4, 6, 1]
# new_list = [value ** 2 for value in my_list]
new_list = list(map(add, my_list, my_list_2))
print(new_list)

new_list = [value ** 2 for value in my_list]  # генератор списков
new_list = list(map(lambda x: x ** 2, my_list))  # lambda
new_list = list(map(square, my_list))  # функция с именем

# Задача 2
my_list = ["2", 4, "6", "1", 5]
# my_list = [str(val) for val in my_list]
my_list = list(map(str, my_list))
my_str = "".join(my_list)
print(my_str)

# zip
list_1 = [1, 2, 3]
list_2 = ['q', 'w', 'e', 'r', 't', 'y']
list_3 = {.1, .2, .3, .4}

result_dict = dict(zip(list_1, list_2))
print(result_dict)
result_list = dict(zip(list_2, tuple(zip(list_1, list_3))))
print(result_list)

