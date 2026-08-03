from dataclasses import dataclass
from typing import List

@dataclass
class BankAccount:
    name: str
    id: int
    balance: float


class Bank:
    def __init__(self, bank_accounts: List[BankAccount]):
        self.bank_accounts = {}
        for acc in bank_accounts:
            self.bank_accounts[acc.id] = acc

    def get_balance(self, account_id: int) -> float:
        return self.bank_accounts.get(account_id).balance

    def deposit(self, account_id: int, amount: float) -> bool:
        self.bank_accounts[account_id].balance += amount
        return True

    def withdraw(self, account_id: int, amount: float) -> bool:
        current_balance = self.bank_accounts[account_id].balance
        if current_balance - amount >= 0:
            self.bank_accounts[account_id].balance -= amount
            return True
        return False

    def transfer(self, from_account_id: int, to_account_id: int, amount: float) -> bool:
        withdraw_result = self.withdraw(from_account_id, amount)
        if not withdraw_result:
            return False

        deposit_result = self.deposit(to_account_id, amount)
        if not deposit_result:
            return False

        return True

### pytest for about class


def test_get_balance():
    accounts = [
        BankAccount(id=1, name="John Doe", balance=1000.0),
        BankAccount(id=2, name="Mohsin", balance=2000.0),
        BankAccount(id=3, name="Kiran", balance=3000.0)
    ]

    bank = Bank(accounts)

    assert bank.get_balance(1) == 1000.0
    assert bank.get_balance(2) == 2000.0
    assert bank.get_balance(3) == 3000.0

    # pyrefly: ignore [comparison-in-tests]
    assert bank.get_balance(4) == None

def test_deposit():
    accounts = [
        BankAccount(id=1, name="John Doe", balance=1000.0),
        BankAccount(id=2, name="Mohsin", balance=2000.0),
        BankAccount(id=3, name="Kiran", balance=3000.0)
    ]

    bank = Bank(accounts)

    assert bank.deposit(1, 100.0) == True
    assert bank.get_balance(1) == 1100.0

    assert bank.deposit(2, 200.0) == True
    assert bank.get_balance(2) == 2200.0

    assert bank.deposit(3, 300.0) == True
    assert bank.get_balance(3) == 3300.0

def test_withdraw():
    accounts = [
        BankAccount(id=1, name="John Doe", balance=1000.0),
        BankAccount(id=2, name="Mohsin", balance=2000.0),
        BankAccount(id=3, name="Kiran", balance=3000.0)
    ]

    bank = Bank(accounts)

    assert bank.withdraw(1, 100.0) == True
    assert bank.get_balance(1) == 900.0

    assert bank.withdraw(2, 200.0) == True
    assert bank.get_balance(2) == 1800.0

    assert bank.withdraw(3, 300.0) == True
    assert bank.get_balance(3) == 2700.0


test_get_balance()