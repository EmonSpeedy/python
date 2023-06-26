class Shop:
    def __init__(self, name):
        self.name = name
        self.cart = []

    def add_to_cart(self, item, price, quant):
        product = {'item': item, 'price': price, 'quantity': quant}
        self.cart.append(product)

    def remove_cart(self, Item):
        for items in self.cart:
            if items['item'] == Item:
                self.cart.remove(items)
                break
                  

    def check_out(self, amount):
        total_amount = 0
        for items in self.cart:
            total_amount += (items['price'] * items['quantity'])
        print(f'You have to pay {total_amount} BDT.')
        if amount < total_amount:
            print(f'Sorry! you have to pay more {total_amount-amount} BDT.')
        elif amount > total_amount:
            print(f'You will take more {amount-total_amount} BDT.')
        else:
            print("Congratulations!!!")
            print(f'Here is your checkout card. You can take your items.')

    

cus1 = Shop("Selim")
cus1.add_to_cart("Perfume", 150, 2)
cus1.add_to_cart("Potato", 70, 4)
print(cus1.cart)
cus1.remove_cart('Perfume')
print(cus1.cart)
cus1.check_out(400)
