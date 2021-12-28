################################################
# 1. Создать папку ./alphabet/ Если папка существует, то ОК.
# 2. В папке ./alphabet/ создать файлы вида a.txt, b.txt, ..., z.txt
# в которых будет записана строка алфавита, но с заменой буквы из названия файла на прописную.
# Пример: для b.txt строка будет aBcde...
# 3. Сделать щелчек Таноса - удалить случайным образом половину всех файлов в этой папке.

import os


os.makedirs("lesson10/data/alphabet", exist_ok=True)   # Лучший способ создания папки

os.remove("Homeworks/lesson8_2.txt")

# try:
#     os.mkdir("lesson10/data/alphabet")
# except FileExistsError:
#     pass