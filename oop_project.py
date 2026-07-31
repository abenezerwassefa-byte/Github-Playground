from BankAccounts import *
Dave = BankAccount(1000.2312, "Dave")
Sara = BankAccount(2000, "Sara")

Jim = Interest(50000, "Jimmy")
Jim.getBalance()
Jim.deposit(100)
Jim.transfer(200, Dave)
# =============Study this!! Don't slack off!!
