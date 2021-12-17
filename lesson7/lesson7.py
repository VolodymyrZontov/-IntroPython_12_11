# импорт

# создание строки алфавита
alpha_list = [chr(numb) for numb in range(ord("a"), ord("z") + 1)]
alphabet = "".join(alpha_list)
print(alphabet)

# импортирование модуля string для получения строки алфавита
import string
alphabet = string.ascii_lowercase
print(alphabet)

# импортирование строки алфавита из модуля string
from string import ascii_lowercase
alphabet = ascii_lowercase
print(alphabet)

# импортирование строки алфавита из модуля string с именованием
from string import ascii_lowercase as alphabet
print(alphabet)

# сокращения в нейминге при импорте
import random as rnd
value = rnd.randint(1, 6)

# импорт из файла
from utils import alphabet
print(alphabet)

# импорт из файла в папке
from data.project_const import DEBUG_MODE
# from data.project_const import *   # желательно не использовать

month_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

if DEBUG_MODE:
    print("Hello!", month_list)
