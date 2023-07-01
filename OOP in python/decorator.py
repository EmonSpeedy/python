import math
import time
def timer(func):
    def inner(*args, **kargs):
        print('time started')
        start = time.time()
        # print(func())
        func(*args, **kargs)
        print('time ended')
        end = time.time()
        print(f'Total time taken {end - start}')

    return inner

# timer()()
@timer     # decorator
def get_factorial(n):
    print('Factorial started')
    result = math.factorial(n)
    print(f'factorial of {n} is {result}')

get_factorial(120)
# vejaille way to decorate 
# timer(get_factorial)()