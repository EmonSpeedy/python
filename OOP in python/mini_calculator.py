class Calculator:
    brand = "CASIO 100ms"

    def add(self, num1, num2):
        return num1 + num2
    def deduct(self, num1, num2):
        return num1 - num2
    def multi(self, num1, num2):
        return num1 * num2
    def divide(self, num1, num2):
        return num1 / num2

oper = Calculator()
n1 = int(input('Enter 1st number : '))
n2 = int(input('Enter 2nd number : '))
inp = input("Enter a method : ")
if inp == '+':
    res = oper.add(n1, n2)
elif inp == '-':
    res = oper.deduct(n1, n2)
elif inp == '*':
    res = oper.multi(n1, n2)
else:
    res = oper.divide(n1, n2)

print("Result is : ",res)
