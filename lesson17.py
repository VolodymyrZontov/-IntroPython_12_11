# наследование
# инкапсуляция

import json
import os
from string import ascii_lowercase as alphabet
from random import shuffle


class PlayAlphabet:
    def __init__(self, dirname):
        self._dir_name = dirname
        self.__create_dir()

    def __create_dir(self):
        os.makedirs(self._dir_name, exist_ok=True)

    def _create_file(self, symbol):
        filename = f"{symbol}.txt"
        with open(os.path.join(self._dir_name, filename), "w") as txt_file:
            txt_file.write(alphabet.replace(symbol, symbol.upper()))

    def create_files(self):
        for symbol in alphabet:
            self._create_file(symbol)

    def do_tanos_click(self):
        list_dir = os.listdir(self._dir_name)
        shuffle(list_dir)
        for filename in list_dir[:len(list_dir) // 2]:
            os.remove(os.path.join(dir_name, filename))


dir_name = "alphabet"
play_test = PlayAlphabet(dir_name)
play_test.create_files()
play_test.do_tanos_click()
play_test._dir_name = "aaa"
play_test._PlayAlphabet__create_dir()



#####################################################################
#
# class Car:
#     def drive(self):
#         return "I can drive"
#
#
# class Boat:
#     def sail(self):
#         return "I can sail"
#
#     def drive(self):
#         return "I can't drive"
#
#
# class Amphibian(Car, Boat):
#     pass
#
#
# # class Amphibian:
# #     def __init__(self):
# #         car = Car()
# #         boat = Boat()
#
#
# amphibian = Amphibian()
#
# print(amphibian.sail())
# print(amphibian.drive())

#####################################################################
# class JsonReader:
#     def __init__(self, filename):
#         self.filename = filename
#         self.data = self.read_json()  # считываем сразу все в память
#         # self.data = None
#
#     def read_json(self):
#         with open(self.filename, 'r') as file:
#             # self.data = json.load(file)  # считываем при запуске метода
#             return json.load(file)
#
#     def sort(self):
#         raise NotImplementedError


# class ListJson(JsonReader):
#     def sort(self):
#         self.data.sort()
#
#
# class DictJson(JsonReader):
#     def sort(self):
#         self.data = {key: self.data[key] for key in sorted(self.data.keys())}
#
#
# json_reader = ListJson("test_list.json")
# print(json_reader.data)
# json_reader.sort()
# print(json_reader.data)
#
# json_reader = DictJson("test_dict.json")
# print(json_reader.data)
# json_reader.sort()
# print(json_reader.data)

# json_reader.read_json()
# data = json_reader.data
# print(data)

#####################################################################

# class Person:
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#
#     def __str__(self):
#         return f"My name is {self.name}. I'm {self.age}"
#
#     def increase_age(self):
#         self.age += 1
#
#
# class Employee(Person):
#     def __init__(self, name, age, sex, job):
#         super().__init__(name, age, sex)
#         self.job = job
#
#     def __repr__(self):
#         return f"I am {self.job}"
#
#     def __str__(self):
#         base_str = super().__str__()
#         return f"{base_str}. I am a {self.job}"
#
#     def send_message(self, message):
#         return f"I just have send a message: {message}"
#
#
# person_1 = Employee("John", 23, "male", "postmen")
# print(person_1)
# person_1.increase_age()
# print(person_1)
# print(person_1.send_message("Hello!"))
