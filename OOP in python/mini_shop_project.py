class Product:
    def __init__(self, name, price, quantity) -> None:
        self.product_name = name
        self.product_price = price
        self.product_quantity = quantity

class Store:
    def __init__(self):
        self.__product_price = {}
        self.__product_quantity = {}
        self.__profit = 0

    def add_product(self, name, price, quantity):
        product = Product(name, price, quantity)
        self.__product_price[product.product_name] = product.product_price
        self.__product_quantity[product.product_name] = product.product_quantity

    def buy_product(self, name, quantity):
        if name in self.__product_quantity:
            if self.__product_quantity[name] >= quantity:
                self.__profit = self.__profit + (((5 * self.__product_price[name])/100)*quantity)
                self.__product_quantity[name] -=  quantity
                print('Congratulations! For purchasing...')
        else:
            print("Not found")

    def show_products_details(self):
        print("Prices :-> ", self.__product_price)
        print("Quantity :-> ", self.__product_quantity)

    def show_profit(self):
        print(self.__profit)
    
class Shop(Store):
    def __init__(self, name) -> None:
        self.name = name
        super().__init__()


shop1 = Shop("My Gadget")
shop1.add_product("Iphone", 120000, 8)
shop1.add_product("SamsungS10", 110000, 12)

# print(shop1.product_price['Iphone'])
shop1.show_products_details()
shop1.buy_product('SamsungS10', 4)
shop1.show_products_details()
shop1.show_profit()

