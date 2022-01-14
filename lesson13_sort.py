my_list = [3, 6, 2, 15, -4, 134]

my_list.sort(key=str)
print(my_list)

sort_list = sorted(my_list, key=str)
print(sort_list)


def sort_by_name(item):
    name = item["name"]
    return name


def sort_by_age(item):
    return item["age"]


persons = [{"age": 32, "name": "John"},
           {"name": "Jack", "age": 12},
           {"name": "Jacob", "age": 65}, ]

sort_list = sorted(persons, key=sort_by_age)
print(sort_list)
