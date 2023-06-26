class Bank:
    def __init__(self):
        self.balance = 0
        self.min_Withdraw = 1000
        self.max_Withdraw = 10000

    def get_Balance(self):
        return self.balance

    def Deposit(self, amount):
        if amount > 0:
            self.balance = self.balance + amount
        else:
            print("There is no balance added")

    def Withdraw(self, amount):
        if amount > 0 and self.balance > 0:
            if amount < self.min_Withdraw:
                print(f'Sorry! You can not withdraw less than {self.min_Withdraw} BDT.')
            elif amount > self.max_Withdraw:
                print(f'Sorry! You can not withdraw more than {self.max_Withdraw} BDT.')
            else:
                print(f'Here is your {amount} BDT.')
                self.balance -= amount
                print(f'Your new balance is {self.balance} BDT.')

        else:
            print(f'Please try again, you may have insufficiant balane or amount. THANK YOU...')


bdBank = Bank()
bdBank.Deposit(40000)
print(bdBank.get_Balance())
bdBank.Withdraw(5000)

standardchatbank = Bank()
standardchatbank.Deposit(30000)
print(standardchatbank.get_Balance())
standardchatbank.Withdraw(6000)
