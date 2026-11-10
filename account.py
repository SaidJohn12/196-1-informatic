class Account:
    def __init__(self, number, owner, balance=0):
        if balance<0:
            raise ValueError("Баланс отрицательный")
        self.number=str(number)
        self.owner=str(owner)
        self.balance=balance

    def deposit(self,amount):
        if amount<=0:
            raise ValueError("С числами меньше 0 не работаю!")
        self.balance+=amount
    def withdraw(self,amount):
        if amount<=0:
            raise ValueError("С числами меньше 0 не работаю!")
        if amount>self.balance:
            raise ValueError("Денюжек не хватает")
        self.balance-=amount
    def __repr__(self):
        return f"Account('{self.number}', '{self.owner}', {self.balance})"

if __name__=="__main__":
    acc = Account("40817", "Иван", 1000)
    acc.deposit(500)
    acc.withdraw(200)
    print(acc)
    #pytest tests/test_04_classes.py -v