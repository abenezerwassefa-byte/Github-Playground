class BalanceException(Exception):
    pass


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

# Now, let's do a withdraw method. This could get a little complex.
    def viableTransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(
                f"Sorry, your account only has ${self.balance}"
            )

    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance = self.balance - amount
            print("\nWithdraw complete.")
            self.getBalance()
        except BalanceException as error:
            print(f"\nWithdraw interrupted: {error}")

    def transfer(self, amount, account):
        try:
            print('\n Beginning Transfer...')
            # see what happen if this were omitted
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)  # what is this doing?
            print('Transfer Complete!')
        except BalanceException as error:
            print(f'Transfer Interrupted. {error}')


class Interest(BankAccount):
    def deposit(self, amount):
        self.balance = self.balance + (amount * 1.05)
        print("\nDeposit Complete")
        self.getBalance()


class Savings(Interest):
    def __init__(self, initialAmount, acctName):
        super().__init__(initialAmount, acctName)
        self.fee = 5

    def withdraw(self, amount):
        try:
            self.viableTransaction(amount + self.fee)
            self.balance = self.balance - (amount + self.fee)
            print("Withdraw Complete.")
            self.getBalance()
        except BalanceException as error:
            print(f"\n Withdraw Interrupted: {error}")
# Read this documentation and understand it
