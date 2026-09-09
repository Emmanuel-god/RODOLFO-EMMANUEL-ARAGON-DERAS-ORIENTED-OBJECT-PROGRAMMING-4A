class window:
    def __init__(self, material,color,form):
        self.material = material
        self.color = color
        self.form = form

    def move(self):
        print("The window is moving")

    def describe(self):
        print(f"The window is made wit {self.material}")

#create multiple instances using the class "Window"
#instance 1:
window1 = window("grey", "aluminum", "square")
#instance 2:
window2 = window("black", "steel", "rectangle")

print(window1.material)
print(window2.material)
window1.describe()
window2.describe()

# LAb1. Bank Account 
class BankAccount:

    def __init__(self, holder, balance):
        self.holder = holder
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited: ${amount}")

    def withdraw(self, amount):
        self.__balance -= amount
        print(f"Withdrawn: ${amount}")

    def check_balance(self):
        print(f"Current balance: ${self.__balance}")


# create multiple instances using the class "BankAccount"

# instance 1
account1 = BankAccount("Raúl Pérez", 5000)

# instance 2
account2 = BankAccount("Joel López", 3000)

print(account1.holder)
account1.check_balance()
account1.deposit(1000)
account1.withdraw(2000)
account1.check_balance()

print()

print(account2.holder)
account2.check_balance()
account2.deposit(500)
account2.withdraw(1200)
account2.check_balance()
