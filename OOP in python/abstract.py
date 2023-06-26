from abc import ABC, abstractmethod
# abc = abstract base class
class Animal(ABC):
    @abstractmethod     #enforce all derived class to have eat method
    def eat(self):
        print('Hey nana , eating banana')
    @abstractmethod
    def move(self):
        print('Jumping papa')

class Monkey(Animal):
    def __init__(self, name) -> None:
        self.category = 'Monkey'
        self.name = name
        super().__init__()

    def eat(self):
        print('Hey nana na, I am eating banana')

    def move(self):
        print('Jumping papa')

lucy = Monkey('lucy')
lucy.eat()
lucy.move()
