# Все пункты сделать как отдельные функции(можно создавать дополнительные вспомагательные функции)
#
# 1. Написать функцию, которая получает в виде параметра имя файла названия интернет доменов (domains.txt)
# и возвращает их в виде списка строк (названия возвращать без точки).
#
# 2. Написать функцию, которая получает в виде параметра имя файла (names.txt)
# и возвращает список всех фамилий из него.
# Каждая строка файла содержит номер, фамилию, страну, некоторое число (таблица взята с википедии).
# Разделитель - символ табуляции "\t"
#
# 3. Написать функцию, которая получает в виде параметра имя файла (authors.txt) и возвращает список
# словарей вида {"date_original": date_original, "date_modified": date_modified}
# в которых date_original - это дата из строки (если есть),
# а date_modified - эта же дата, представленная в формате "dd/mm/yyyy" ( d -день, m- месяц, y - год)
# Например[{"date_original": "8th February 1828", "date_modified": 08 / 02 / 1828}, ...]

from config import month_dict
from utils import read_file


def get_domains(filename):
    lines = read_file(filename)
    domains = [line.replace(".", "") for line in lines]
    return domains


def get_names(filename):
    lines = read_file(filename)
    names = [line.split("\t")[1] for line in lines]
    return names


def modificate_date(date_author):
    day, month, year = date_author.split()
    day = day[:-2].zfill(2)
    month = month_dict[month]
    return f"{day}/{month}/{year}"


def get_authors(filename):
    authors = []
    lines = read_file(filename)
    for line in lines:
        if " - " in line:
            date_author = line.split(" - ")[0]
            authors.append({"date_original": date_author, "date_modified": modificate_date(date_author)})
    return authors


print(__name__)

if __name__ == "__main__":
    filename = "domains.txt"
    filename = f"Homeworks/{filename}"
    domains = get_domains(filename)

    filename = "names.txt"
    filename = f"Homeworks/{filename}"
    names = get_names(filename)
    print(names)

    filename = "authors.txt"
    filename = f"Homeworks/{filename}"
    authors = get_authors(filename)
    print(authors)
