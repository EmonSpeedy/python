class Family:
    def __init__(self, address) -> None:
        self.address = address

class School:
    def __init__(self, id, level):
        self.id = id
        self.level = level

class Sport:
    def __init__(self, game):
        self.game = game


class Student(Family, School, Sport):
    def __init__(self, address, id, level, game) -> None:
        Family.__init__(self, address)
        School.__init__(self, id, level)
        Sport.__init__(self, game)
        
    def display_info(self) -> str:
        print("Students family location : ", self.address)
        print("Students ID : ", self.id)
        print("Students class : ", self.level)
        print("Student activity : ", self.game)


stu1 = Student("2-no: Gate, Chittagong", 1500020, "7th", "Cricket")
stu1.display_info()

stu2 = Student("Bahaddarhat, Chittagong", 1500050, "7th", "Badminton")
stu2.display_info()

