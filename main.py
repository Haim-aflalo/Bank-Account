from bankaccount import BankAccount

if __name__ ==  "__main__":

    account_1 = BankAccount("DAN",1000)
    print(account_1.__str__())
    account_2 = BankAccount("gad",2000)
    print(account_2.__str__())
    account_1.transfer_funds(account_2,200)
    print(account_1.__str__())
    print(account_2.__str__())
    account_2.transfer_funds(account_1,600)
    print(account_2.__str__())
    print(account_1.__str__())
