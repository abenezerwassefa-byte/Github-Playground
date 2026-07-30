class BankAccount:
    def __init__(self, initialAmount, acctName):
        self.balance = initialAmount
        self.name = acctName
        return f"Account {self.name} has been created. Your balance is ${self.balance:.2f}"
