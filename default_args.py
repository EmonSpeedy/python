# default arguments system

def sum_it(num1, num2, num3 = 0):
    total = num1 + num2 + num3
    return total

ans = sum_it(10, 20)
print(ans)

# Args

def summation(num1, num2, *numbers):
    print(numbers)
    sum = 0
    for nums in numbers:
        sum += nums
    return sum

ans1 = summation(20, 40, 30, 55)
print(ans1)
