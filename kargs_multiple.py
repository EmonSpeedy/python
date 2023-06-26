
def full_name(first, last):
    name = f'Name is : {first} {last}'
    return name
name = full_name(last = 'Mia', first = 'Alu')
print(name)

# **k-args --> arguments with keys

def famous_name(first, last, **addition):
    for key, value in addition.items():
        print(key, value)

name = famous_name(first = 'Mijanur', last = 'Rahman', title = 'Alem', occup = 'Hujur', last1 = 'Azhari')
print(name)

# can returns multiple answers from the same function

def a_lot(num1, num2):
    sum = num1 + num2
    sub = num1 - num2
    mul = num1 * num2
    div = num1 // num2
    return [sum, sub, mul, div]

answer = a_lot(10, 5)
print(answer)
