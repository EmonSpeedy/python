class Person:
    def __init__(self, name, age, height, weight) -> None:
        self.name = name
        self.age = age
        self. height = height
        self.weight = weight


class Player(Person):
    def __init__(self, name, age, height, weight, team) -> None:
        self.team = team
        super().__init__(name, age, height, weight)

    # operator overloading +, *, lenght
    def __add__(self, other):
        return self.age + other.age
    def __mul__(self, other):
        return self.weight * other.weight
    def __len__(self):
        return self.height
    def __gt__(self, other):
        return self.age > other.age


sakib = Player('Sakib', 42, 66, 74, 'BD')
mushi = Player('Mushfiq', 40, 65, 76, 'BD')

print(sakib + mushi)
print(sakib * mushi)
print(len(mushi))
print(sakib > mushi)
