
class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            return f"${amount} deposited. New balance: ${self.__account_balance}"
        else:
            return "Invalid deposit amount. Amount must be greater than 0."

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__account_balance:
            self.__account_balance -= amount
            return f"${amount} withdrawn. New balance: ${self.__account_balance}"
        else:
            return "Invalid withdrawal amount or insufficient balance."

    def display_balance(self):
        return f"Account Balance for {self.__account_holder_name}: ${self.__account_balance}"

# Creating an instance of the BankAccount class
account1 = BankAccount("12345", "John Doe", 1000)

# Testing deposit and withdrawal
print(account1.display_balance())
print(account1.deposit(500))
print(account1.withdraw(200))
