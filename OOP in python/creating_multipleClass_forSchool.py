class Student:
    def __init__(self, Stu_name, Stu_class, Stu_id):
        self.Stu_name = Stu_name
        self.Stu_class = Stu_class
        self.Stu_id = Stu_id

    def __repr__(self) -> str:
        return f'Studen name :-> {self.Stu_name} | Student class :-> {self.Stu_class} | Student ID :-> {self.Stu_id}'
    
class Teacher:
    def __init__(self, te_name, te_sub, te_id):
        self.te_name = te_name
        self.te_sub = te_sub
        self.te_id = te_id

    def __repr__(self) -> str:
        return f'Teacher name :-> {self.te_name} | Teacher subject :-> {self.te_sub} | Teacher ID :-> {self.te_id}'
    
class School:
    def __init__(self, name):
        self.name = name
        self.teachers = []
        self.students = []

    def add_Teacher(self, name, subject):
        id = len(self.teachers) + 1
        teacher = Teacher(name, subject, id)
        self.teachers.append(teacher)

    def chc_fee(self, amount):
        if amount < 10500:
            return False
        elif amount > 10500:
            return False
        else:
            return True
    
    def enroll(self, name, amount):
        verdict = self.chc_fee(amount)
        if verdict:
            id = len(self.students) + 1
            student = Student(name, 1, id)
            self.students.append(student)
        else:
            if amount > 10500:
                print("Over Fee...")
            else:
                print("Insufficiant fee")

    def __repr__(self):
        print(f"Welcome to the hell land of {self.name}")
        print("------------>> OUR TEACHERS <<------------")
        for teach in self.teachers:
            print(teach)
        print("------------>> OUR STUDENTS <<------------")
        for stu in self.students:
            print(stu)
        return f'Here are all info about {self.name}'


bgc = School("BGCTUB")
bgc.add_Teacher('Subashis Ghosh', 'Java')
bgc.add_Teacher('Monjur Alam', 'Ki porai nijei jane nah')
bgc.enroll('Abdul Momin', 10500)
bgc.enroll('Raihan Talukder', 10500)

print(bgc)

         