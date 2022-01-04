################################################
# 1. Создать папку ./alphabet/ Если папка существует, то ОК.
# 2. В папке ./alphabet/ создать файлы вида a.txt, b.txt, ..., z.txt
# в которых будет записана строка алфавита, но с заменой буквы из названия файла на прописную.
# Пример: для b.txt строка будет aBcde...
# 3. Сделать щелчек Таноса - удалить случайным образом половину всех файлов в этой папке.

import os
from string import ascii_lowercase as alphabet
from random import shuffle


def create_dir(dir_name):
    os.makedirs(dir_name, exist_ok=True)


def create_file(dir_name, symbol):
    filename = f"{symbol}.txt"
    with open(os.path.join(dir_name, filename), "w") as txt_file:
        txt_file.write(alphabet.replace(symbol, symbol.upper()))


def create_files(dir_name):
    for symbol in alphabet:
        create_file(dir_name, symbol)


def do_tanos_click(dir_name):
    list_dir = os.listdir(dir_name)
    shuffle(list_dir)  # list_dir = list(set(list_dir)) - "одноразовое" решение
    for filename in list_dir[:len(list_dir) // 2]:
        os.remove(os.path.join(dir_name, filename))


dir_name = "alphabet"
create_dir(dir_name)
create_files(dir_name)
do_tanos_click(dir_name)

#
# os.makedirs("lesson10/data/alphabet", exist_ok=True)   # Лучший способ создания папки
#
# os.remove("Homeworks/lesson8_2.txt")

# try:
#     os.mkdir("lesson10/data/alphabet")
# except FileExistsError:
#     pass
