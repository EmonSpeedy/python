# access modifier :--> public, private, protected
# Encapsulation :--> Hides details
class Bank:
    def __init__(self, holder_name, init_deposit) -> None:
        self.holder_name = holder_name # public attribute
        self._branch = "Dhaka"  # protected attribute
        self.__balance = init_deposit  # private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Invalid amount , Try again!")


    def disp_blnc(self):
        return self.__balance
    

anik = Bank("Anik", 10500)
anik.deposit(1000)
anik._Bank__balance = 1 # a secret way to access private attributes

print(anik.disp_blnc())
