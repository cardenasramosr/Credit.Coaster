from schemas.user import User


class Account:
    def __init__(self, user: User, balance: float):
        self.user = user #Se llama la funcion user y se guarda
        self.balance = balance #Se guarda el balance de la cuenta 
