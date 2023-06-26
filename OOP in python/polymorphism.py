# poly = many
# morph = shape or method
from math import pi
class Animal:
    def __init__(self, name) -> None:
        self.name = name
    def make_sound(self):
        print("Making sound")

class Cat(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)
    def make_sound(self):
        print('meow meow')

class Dog(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)
    def make_sound(self):
        print('gheo gheo')

class Shape:
    def __init__(self, name) -> None:
        self.name = name
    def area(self):
        print('No area found')

class Rectangular(Shape):
    def __init__(self, name, length, width) -> None:
        self.length = length
        self.width = width
        super().__init__(name)
    def area(self):
        return self.length*self.width
    
class Circle(Shape):
    def __init__(self, name, radius) -> None:
        super().__init__(name)
        self.radius = radius
    def area(self):
        return pi*(self.radius)

rec1 = Rectangular('rectangular1', 50, 40)
print(rec1.area())
cir1 = Circle('circle1', 5)
print(cir1.area())
