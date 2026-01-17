import time
from .interest import calculate_interest




class CryptoVault:
def __init__(self, owner: str):
self.owner = owner
self.balance = 0.0
self.last_update = time.time()


def _apply_interest(self):
interest, ts = calculate_interest(self.balance, self.last_update)
self.balance += interest
self.last_update = ts


def deposit(self, amount: float):
if amount <= 0:
raise ValueError("Invalid amount")
self._apply_interest()
self.balance += amount


def withdraw(self, amount: float):
self._apply_interest()
if amount > self.balance:
raise ValueError("Insufficient funds")
self.balance -= amount


def get_balance(self) -> float:
self._apply_interest()
return round(self.balance, 8)
