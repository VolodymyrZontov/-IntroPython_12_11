# CLI
import sys
import requests

from argparse import ArgumentParser

args = ArgumentParser()

# args.add_argument("first_arg", nargs='?', type=str, default='')
# args.add_argument("second_arg", nargs='?', type=int, default=0)
# args.add_argument("-f","--print_flag", nargs='?', type=str, default='FLAG')
# args.add_argument("-f","--flag", nargs='?', type=bool, default=True)
# print('args.parse_args() -->', args.parse_args())

args.add_argument("quote_nums", nargs='?', type=int, default=3)
args = vars(args.parse_args())
# print('args -->', args)

quote_nums = args["quote_nums"]

# args = sys.argv
# try:
#     quote_nums = int(args[1])
# except (ValueError, IndexError):
#     quote_nums = 3

url = "http://api.forismatic.com/api/1.0/"

for idx in range(quote_nums):
    params = {"method": "getQuote",
              "format": "json",
              "lang": "ru",
              "key": idx}

    response = requests.get(url, params=params)
    response = response.json()
    print(response['quoteText'], response["quoteAuthor"])

#####################################################################
import re

value = "QWE"
my_str = f"Я хочу найти {value} 123"

sub_value = "WE"
pattern = r'[A-Z]{1}' + sub_value + ' [0-9]+'
print(pattern)
res = re.findall(pattern, my_str)
print(res)

#filter

my_list = [12, 24, 5, -1, 4]

# new_list = [value for value in my_list if value > 10]


def check_func(value):
    if value >= 0:
        return value ** 0.5 >= 2
    return False

new_list = list(filter(check_func, my_list))
# new_list = list(filter(lambda x: x > 10, my_list))
print(new_list)