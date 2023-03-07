import datetime
import random

from schemas.account import Account


class Card:
    def __init__(self, account: Account, nip: int):
        now = datetime.datetime.now()
        self.account = account
        self.nip = nip
        self.number = random.randint(4400_000_000_000, 4500_000_000_000) #Genera un numero random para la tarjeta
        self.expiration = datetime.datetime(year=now.year + 5, month=now.month, day=1)
