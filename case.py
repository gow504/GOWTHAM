class Atm:
    def __init__(self):
        print("account created :")
        self.balance=0
    def deposit(self):
        amount=int(input("enter deposit money:"))
        self.balance=self.balance+amount
    def withdraw(self):
        amount=int(input("enter withdraw money:"))
        if self.balance<amount:
            print("insufficent balance")
        else:
            self.balance=self.balance-amount
            print(self.balance)
    def enquiry(self):
        print("remaining balance",self.balance)
        
        
        
a=Atm()
a.deposit()    
a.withdraw()    
a.enquiry