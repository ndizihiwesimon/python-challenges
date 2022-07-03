# *Problem 19*. Implement an ATM, which keeps track of the total amount of money it has. The user should be able to interact with the ATM, and it provide options until they would like to exit. Implement some method, Interact, which allows the user to interact with the ATM.
# It should have some methods that the user can select via this interface, which you can implement as you think makes most sense:
# 1. Withdraw
# 2. Deposit
# 3. Current balance
# 4. Exit
 
class ATM:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def withdraw(self, amount):
        if self.amount >= amount:
            self.amount -= amount
        else:
            print("Insufficient funds to withdraw: %s available: %s" % (amount, self.amount))
    
    def deposit(self, amount):
        self.amount += amount
        print("Deposit done successfully, deposited amount: %s New balance: %s" % (amount, self.amount))

    def balance(self, amount):
        print("You have %s on your account!" % self.amount)

    def stop(self):
        return print("%s, Thank you for using ATM services" % self.name)
            
if __name__ == '__main__':
    name = input('Enter your Name: ')
    amount = input('Please enter starting amount: ')
    service = ATM(name, amount)
    
    on = True
    while on:
        print("ATM")
        
