# typing
# работа с файлами

import os


########################### Путь к файлу
dir = "Homeworks"
# subdir = "tmp"
filename = "lesson8.txt"
#
# # file_path = f"{dir}/{filename}"
file_path = os.path.join(dir, filename)
# print(file_path)

# содержимое папки
# dir = os.listdir("Homeworks")
# print(dir)

# dirname = 'lesson7'
# for file_obj in os.listdir(dirname):
#     file_obj_path = os.path.join(dirname, file_obj)
#     if os.path.isdir(file_obj_path):
#         print(f"This is real folder: {file_obj}")


################################ V1
with open(file_path, "r") as txt_file:
    data = txt_file.read()

data = data.split("\n")
print(data)

############################### V2

# with open(file_path, "r") as txt_file:
#     data = txt_file.readlines()
#
# print(data)

data.append("TEST")
data.append("TEST2")

################################ V1
with open(file_path, "w") as txt_file:
    txt_file.write("\n".join(data))

############################### V2
# with open(file_path, "w") as txt_file:
#     txt_file.writelines(data)






# def print_uppercase(text: str) -> None:
#     result = text.upper()
#     print(result)
#
#
# def convert_uppercase(text: str) -> str:
#     return text * 12
#
#
# def create_funny_list(my_list: list, f_str: str="John", s_str: str="Silver") -> list:
#     if len(f_str) > 0:
#         my_list.append(f_str)
#         my_list.append(s_str)
#         return my_list
#     else:
#         return []
#
#
# print_uppercase("12")
# result = convert_uppercase("12")
# print(result)
