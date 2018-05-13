class BankAccount:
    def __init__(self, owner, balance = 0.0):
        self.owner = owner
        self.balance = balance
        
    def deposit(self, num):
        self.balance += num
        return self.balance
        
    def withdraw(self, num):
        self.balance -= num
        return self.balance

acct = BankAccount("Dany")
print(acct.owner)