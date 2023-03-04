# Kata used: https://kata-log.rocks/banking-kata
from typing import Optional


class BankAccount:
    # Green
    # ammount = 0

    # Refactor
    def __init__(self, ammount: Optional[int] = 0):
        self.ammount = ammount

    def deposit(self, amm):
        self.ammount += amm
