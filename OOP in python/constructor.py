class Phone:
    manufactured = 'China'

    def __init__(self, owner, brand, price):
        self.owner = owner
        self.brand = brand
        self.price = price

    def SMS(self, sms, phn):
        self.sms = sms
        self.phn = phn
        text = f"SMS sent to 0{phn}. Text was {sms}"
        print(text)

my_phn = Phone("Emon", "Realme", 25000)
print(my_phn.owner,' ,', my_phn.brand,' ,',my_phn.price)

mom_phn = Phone("Johara", "Samsung", 12000)
print(mom_phn.owner,' ,', mom_phn.brand,' ,',mom_phn.price)

dad_phn = Phone("Mahabul", "Samsung", 30000)
print(dad_phn.owner,' ,', dad_phn.brand,' ,',dad_phn.price)

