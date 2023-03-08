import datetime
import random

from schemas.account import Account


class Card:
    def __init__(self, account: Account, nip: int):
        now = datetime.datetime.now()
        self.account = account #Se llama la funcion account y se agrega el valor cuenta
        self.nip = nip #Se guarda el numero del nip de la tarjeta
        self.number = random.randint(4400_000_000_000, 4500_000_000_000) #Genera un numero random para la tarjeta
        self.expiration = datetime.datetime(year=now.year + 5, month=now.month, day=1) #Se genera una fecha de hoy a 5 años con el mismo mes y mismo dia
