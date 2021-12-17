# функции

# my_str = "asdfhkashjdfkash"
# my_str_len = len(my_str)  # возвращает значение
# value = print(my_str_len)  # не возвращает значение
# print(value)

from random import randint


def generate_list_rand_int():
    result = [randint(1, 10) for _ in range(20)]
    return result


def print_str(some_string):
    print(some_string)


def print_reverse_str(some_string):
    print(some_string[::-1])


def get_reverse_str(some_string):
    return some_string[::-1]


def change_list_last_value(my_list, last_value):
    # if not my_list:
    #     return my_list
    my_list.pop()
    my_list.append(last_value)
    return my_list


##################################
value = generate_list_rand_int()
print(value)

str_1 = "qwerty"
test_str = "TEST"
some_string = "some_string"

print_reverse_str(str_1)
print_reverse_str(test_str)
print_reverse_str(some_string)

value = get_reverse_str(test_str)
print(value)

my_list = [1, 2, 3]
last_value = 100
new_list = change_list_last_value([12, 23, 34], 123)
print(new_list)
########################## task #1
change_list_last_value([12, 23, 34], 123)
########################## task #2
generate_list_rand_int()

