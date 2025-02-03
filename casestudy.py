class Atm:
    def __init__(self):
        print("account created")
        self.balance = 0
    def deposit(self):
        amount=int(input("enter amount"))
        self.balance=self.balance +amount
        print("the deposit money is:",amount)
    def withdraw(self):
        amount = int(input("enter the eithdraw amount1000"))
        if self.balance < amount:
            print("insufficient balance")
        else:
            self.balance = self.balance-amount
            print("remaining balance is:",self.balance)
            
    def enquiry(self):
        print("available balance",self.balance)
a=Atm()
a.deposit()
a.withdraw()
a.enquiry()