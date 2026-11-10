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


class Customer:

    def __init__(self, name, customer_id):
        self.name = name
        self.customer_id = customer_id
        self._accounts = []

    def add_account(self, account):
        self._accounts.append(account)

    def remove_account(self, number):
        for idx, acc in enumerate(self._accounts):
            if acc.number == number:
                self._accounts.pop(idx)
                return
        raise KeyError("Счет с таким номером не найден у клиента")

    def accounts(self):
        return list(self._accounts)

    def total_balance(self):
        return sum(acc.balance for acc in self._accounts)


class Bank:

    def __init__(self):
        self._customers = {}
        self._all_accounts = {}

    def add_customer(self, customer):
        if customer.customer_id in self._customers:
            raise ValueError("Клиент с таким ID уже существует")
        self._customers[customer.customer_id] = customer

    def customer(self, customer_id):
        if customer_id not in self._customers:
            raise KeyError("Клиент не найден")
        return self._customers[customer_id]

    def open_account(self, customer_id, account):
        if customer_id not in self._customers:
            raise KeyError("Клиент не найден")
        if account.number in self._all_accounts:
            raise ValueError("Счет с таким номером уже существует")

        self._all_accounts[account.number] = (customer_id, account)
        self._customers[customer_id].add_account(account)

    def close_account(self, number):
        if number not in self._all_accounts:
            raise KeyError("Счет не найден")

        customer_id, account = self._all_accounts[number]
        if account.balance != 0:
            raise ValueError("Нельзя закрыть счет с ненулевым остатком")

        self._customers[customer_id].remove_account(number)
        del self._all_accounts[number]

    def transfer(self, from_number, to_number, amount):
        if from_number == to_number:
            raise ValueError("Нельзя перевести деньги на тот же самый счет")
        if from_number not in self._all_accounts or to_number not in self._all_accounts:
            raise KeyError("Один или оба счета не найдены в банке")
        if amount <= 0:
            raise ValueError("Сумма перевода должна быть положительной")

        from_account = self._all_accounts[from_number][1]
        to_account = self._all_accounts[to_number][1]
        from_account.withdraw(amount)
        to_account.deposit(amount)

    def accounts(self, customer_id, min_balance=None):
        if customer_id not in self._customers:
            raise KeyError("Клиент не найден")

        cust_accounts = self._customers[customer_id].accounts()
        if min_balance is not None:
            return [acc for acc in cust_accounts if acc.balance >= min_balance]
        return cust_accounts

    def total_deposits(self):
        return sum(account.balance for _, account in self._all_accounts.values())