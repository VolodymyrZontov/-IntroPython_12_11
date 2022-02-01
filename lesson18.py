# полиморфизм, магические методы
# декораторы
# property
# staticmethod
# практическая работа


##############################################################
class Utils:
    @staticmethod
    def distance(point_1, point_2):
        return ((point_1[0] - point_2[0]) ** 2 + (point_1[1] - point_2[1]) ** 2) ** 0.5


utils = Utils()
result = utils.distance((0, 0), (3, 4))

print(result)
##############################################################
import time


def time_decorator(some_func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = some_func(*args, **kwargs)
        print(time.time() - start_time)
        return result

    return wrapper


@time_decorator
def factorial(numb):
    res = 1
    for i in range(1, numb + 1):
        res *= i
    return res


# start_time = time.time()
# result = factorial(200000)
# print(time.time() - start_time)


result = factorial(20000)

#######################################################################
my_list_1 = list('qwerty')
my_list_2 = list('asd')

result = my_list_1 + my_list_2

print(result)

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"({self.x}, {self.y})"

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

vec_1 = Vector(1, 3)
vec_2 = Vector(2, 2)

res = vec_1 > vec_2

print(res)
