class Person:
    def __init__(self, name, age, height, weight) -> None:
        self.name = name
        self.age = age
        self. height = height
        self.weight = weight

    def eat(self):
        print("Eating fat food")

    def exercise(self):
        raise NotImplementedError # raised error means must have to implement to sub class

class Player(Person):
    def __init__(self, name, age, height, weight, team) -> None:
        self.team = team
        super().__init__(name, age, height, weight)

    def eat(self):  #This method is overriding the eat method from super class
        print('Eating healthy food')

    def exercise(self):
        print('Doing exercise')


p = Player("Rahim", 35, 178, 76, "BD")
p.eat()
p.exercise()
