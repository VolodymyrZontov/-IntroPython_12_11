### вызов функции внутри другой функции
def generate_alphabet():
    alpha_list = [chr(numb) for numb in range(ord("a"), ord("z") + 1)]
    alphabet = "".join(alpha_list)
    return alphabet


def transform_alphabet(symbol):
    alphabet = generate_alphabet()
    alphabet = alphabet.replace(symbol, symbol.upper())
    return alphabet


symbol = "a"
alphabet_new = transform_alphabet(symbol)
print(alphabet_new)

#############################################################
# Константы в python
import random

MIN_LEN = 15
MAX_LEN = 20


def create_str_rand_len(min_len=MIN_LEN, max_len=MAX_LEN):
    rand_str = "".join(["a" for _ in range(random.randint(min_len, max_len))])
    return rand_str


def create_list_some_len(numb_values):
    result_list = [create_str_rand_len() for _ in range(numb_values)]
    return result_list


numb = 5
my_list = create_list_some_len(numb)
print(my_list)


#########################################################################################
# Значения по умолчанию

def print_person(name="John", age=12, job="programmer"):
    print(f"My name is {name.upper()}. I am {age} and i'm {job}. ")


name = "Vladimir"
job = "president"
age = 42
print_person(name, job=job, age=age)
