# ООП
# класс
# экземпляр класса
# атрибут класса
# атрибут экземпляра класса
# метод экземпляра класса

class Point:
    def __init__(self, x=0, y=0, z=0):
        self.x = x  # атрибут экземпляра класса
        self.y = y
        self.z = z
        self.my_list = [x, y, z]

    def distance(self):  # метод экземпляра класса
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5

    def __str__(self):
        return f"x = {self.x}, y = {self.y}, z = {self.z}, my_list = {self.my_list}"

    def __repr__(self):
        return f"({self.x}, {self.y}, {self.z})"

####################################################################################3

point_a = Point(1, 2, 3)
point_b = Point(10, 20, 30)
point_c = Point(11, 21, 31)
point_d = Point()
point_d.x = 1000
dist_a = point_a.distance()
print(point_a)
print(point_d)
value = str(point_b)
print(value)
points = [point_a, point_b, point_c]
print(points)

###################################################################

class Person:
    name = "John"  # атрибут класса - переменная внутри класса
    age = 12


person = Person()  # экземпляр класса - объект данного класса
person_2 = Person()
person_2.name = "Jack"  # атрибут экземпляра класса
person_2.age = 34  # атрибут экземпляра класса
person_2.education = "Math"  # атрибут экземпляра класса

Person.name = "Ann"

print(person.name, person.age)
print(person_2.name, person_2.age, person_2.education)
