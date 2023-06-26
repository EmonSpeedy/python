
# global variable can be accessed without using global keyword
# but to modify we must use global keyword

balance = 1000

def shopping(item, price):
    global balance
    print(f'Balance before buying {item}', balance)
    balance = balance - price
    print(f'Balance after buying {item}', balance)

shopping('sunglass', 500)
