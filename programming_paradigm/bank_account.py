class BankAccount:
    def __init__(self, account_balance, initial_balance=0):
        self.account_balance = account_balance
        self.initial_balance = initial_balance

    # Function for deposit
    def deposit(self, amount):
            self.account_balance += amount
    # Function for withdraw
    def withdraw(self, amount):
            if self.account_balance > amount:
                self.account_balance -= amount
                return True
            else:
                return False
    # Function to display account balance
    def display_balance(self):
            print(f"Current Balance: ${self.account_balance}.00")
