class Gadget:
    def __init__(self, brand, price, color, processor, origin):
        self.brand = brand
        self.price = price
        self.color = color
        self.processor = processor
        self.origin = origin

    def run(self):
        return f"Running :: {self.brand}" 

class Laptop:
    def __init__(self, ssd):
        self.ssd = ssd

    def coding(self):
        return f"In processment of coding"
    
class Phone(Gadget):
    name = 'Phone'
    def __init__(self, brand, price, color, processor, origin, dual_sim, number):
        self.number = number
        self.dual_sim = dual_sim
        super().__init__(brand, price, color, processor, origin)

    def call(self):
        return f"Call sent to {self.number}"
    
    def display(self):
        print(f"Device : {self.name}")
        print(f"Brand : {self.brand}")
        print(f"Price : {self.price}")
        print(f"Colour : {self.color}")
        print(f"Processor : {self.processor}")
        print(f"DUAL-SIM : {self.dual_sim}")
    
class Camera:
    def __init__(self, pixel):
        self.pixel = pixel

    def shoot(self):
        return f"Shooted by Camera"


my_phn = Phone("Iphone", 120000, "Red", "A-series Bionic chip", "China", "YES", 2211988)
my_phn.display()
print(my_phn.call())
    