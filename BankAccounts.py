# imports
from flask import Flask, render_template, redirect, request
from flask_scss import Scss
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone
app = Flask(__name__)
Scss(app)

# learn what sqlalchemy is!!
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db = SQLAlchemy(app)

# Data class ~ Row of data
# One model = one row of data


class MyTask(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(100), nullable=False)
    complete = db.Column(db.Integer)
    created = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    # DateTime is an object here

    def __repr__(self):
        return f"Task{self.id}"

# Routes to Webpages


# POST MEANS SEND DATA AND GET MEANS RECIEVE DATA
@app.route("/", methods=["POST", "GET"])
def index():
    # Add tasks

    # See all added tasks

    return render_template("Bank.html")


# Runner and Debugger
if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)

# above is a flask tutorial attempt^^^^


class BalanceException(Exception):
    pass  # this subclass is creating a custom error.


class BankAccount:
    def __init__(self, initialAmount, acctName):
        self.balance = initialAmount
        self.name = acctName
        print(
            f"Account {self.name} has been created. Your balance is ${self.balance:.2f}")

    def getBalance(self):
        print(f"Account {self.name} has ${self.balance:.2f}")

    def deposit(self, amount):
        # this is not a statement; it's a reassignment
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
# Read this documentation and understand
