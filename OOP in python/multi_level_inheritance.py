class Vehicle:
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price
    
    def __repr__(self) -> str:
        return f'Bus name : {self.name}.. Price : {self.price}'
        
    def move(self):
        pass

class Bus(Vehicle):
    def __init__(self, name, price, seat) -> None:
        self.seat = seat
        super().__init__(name, price)

    def __repr__(self) -> str:
        return super().__repr__()


class Truck(Vehicle):
    def __init__(self, name, price, weight) -> None:
        self.weight = weight
        super().__init__(name, price)

class pickUp(Truck):
    def __init__(self, name, price, weight) -> None:
        super().__init__(name, price, weight)

class ACBus(Bus):
    def __init__(self, name, price, seat, temp) -> None:
        self.temp =temp
        super().__init__(name, price, seat)

    def __repr__(self) -> str:
        print(f'Seat : {self.seat}.. Temperature : {self.temp}')
        return super().__repr__()

b1 = ACBus('Green Line', 5000000, 35, 16)
print(b1)
