class BankAccount:
    """
    BankAccount
    """

    def __init__(self,account_holder,initial_balance):
        self.holder = account_holder
        self.balance = initial_balance

    def transfer_funds(self,other_account,amount):
        if  self.balance >= amount:
            self.balance -= amount
            other_account.balance += amount
            print("Transfer Completed")
        else:
            print("Not enough money in your bank account ")

    def __str__(self):
        return f"hello {self.holder},you have {self.balance} in your account"





