class BankAccount:
    def __init__(self, initialAmount, acctName):
        self.balance = initialAmount
        self.name = acctName
        print(
            f"Account {self.name} has been created. Your balance is ${self.balance:.2f}")

    def getBalance(self):
        print(f"Account {self.name} has ${self.balance:.2f}")

    def deposit(self, amount):
        self.balance = self.balance + amount
        self.amount = amount
        print(f"Deposit complete. ${self.amount} deposited.")
        self.getBalance()
