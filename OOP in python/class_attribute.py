class Shop:
    Shopping_mall = "Jamuna"
    cart = [] # this array is declared as class attribute it will store everyones info

    def __init__(self, name):
        self.name = name

    def add_to_cart(self, item):
        self.cart.append(item)

customer1 = Shop("Michael")
customer1.add_to_cart("Boot")
customer1.add_to_cart("Sunglass")
print(customer1.cart)

customer2 = Shop("Julian")
customer2.add_to_cart("High heels")
customer2.add_to_cart("Lipstick")
print(customer2.cart)
