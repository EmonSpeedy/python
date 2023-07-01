# getter means read only that means you cannot change the value 
# setter means you can set or modify the vlaue through the method

class User:
    def __init__(self, name, age, money) -> None:
        self._name = name
        self._age = age
        self.__money = money

    @property   #getter
    def age(self):
        return self._age
    
    @property   #getter
    def salary(self):
        return self.__money
    
    @salary.setter  #setter
    def salary(self, value):
        if value < 1:
            print('Salary can not be negative')
        else:
            self.__money += value

shamsu = User('Kapil', 24, 11000)
# print(shamsu.__money)
print(shamsu.age)
print(shamsu.salary)
shamsu.salary = 3500
print(shamsu.salary)