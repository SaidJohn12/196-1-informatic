class Account:
    def __init__(self, number, owner, balance=0):
        if balance < 0:
            raise ValueError("остаток не может быть отрицательным")
        self.number = number
        self.owner = owner
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("сумма должна быть положительной")
        self._balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("сумма должна быть положительной")
        if amount > self._balance:
            raise ValueError("недостаточно средств")
        self._balance -= amount

    def __repr__(self):
        return f"Account({self.number!r}, {self.owner!r}, {self._balance!r})"


class SavingsAccount(Account):
    def __init__(self, number, owner, balance=0, rate=0.05):
        super().__init__(number, owner, balance)
        self.rate = rate

    def add_interest(self):
        self._balance += self._balance * self.rate

    def __repr__(self):
        return f"SavingsAccount({self.number!r}, {self.owner!r}, {self._balance!r}, {self.rate!r})"


class CheckingAccount(Account):
    def __init__(self, number, owner, balance=0, overdraft=0):
        super().__init__(number, owner, balance)
        self.overdraft = overdraft

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("сумма должна быть положительной")
        if self._balance - amount < -self.overdraft:
            raise ValueError("превышен лимит овердрафта")
        self._balance -= amount

    def __repr__(self):
        return f"CheckingAccount({self.number!r}, {self.owner!r}, {self._balance!r}, {self.overdraft!r})"