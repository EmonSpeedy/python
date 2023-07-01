class Shopping:
    cart = [] # class attribute or static attribute
    origin = 'China'

    def __init__(self, name, location) -> None:
        self.name = name        # instance attribute
        self.location = location

    def purchase(self, item, price, amount):
        remaining = amount - price
        print(f'Item = {item}, Price = {price}, Remaining = {remaining}')

    @classmethod
    def kinbo(self, item):
        # print(self.name)
        print(f'Ami {item} kinbo')

    @staticmethod
    def multiply( a, b):
        return a*b


s1 = Shopping('Hala store', "bostir para")
# s1.purchase('Chiruni', 100, 200)
# s1.kinbo('T-shirt')
Shopping.kinbo('Pant')

print(s1.multiply(3, 6))
print(Shopping.multiply(12, 2)) # static method
