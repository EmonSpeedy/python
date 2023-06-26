class Shop:
    shopname = "Jamuna"

    def __init__(self, buyer):
        self.buyer = buyer
        self.cart = [] # it is instance attribute it will store individual customer info

    def add_to_cart(self, item):
        self.cart.append(item)

cus1 = Shop("Michael")
cus1.add_to_cart("Boot")
cus1.add_to_cart("Sunglass")
print(cus1.cart)

cus2 = Shop("Juliat")
cus2.add_to_cart("High heels")
cus2.add_to_cart("Lipstick")
print(cus2.cart)
