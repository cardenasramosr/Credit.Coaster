from schemas.account import Account
from schemas.user import User


class AccountController:

    @staticmethod
    def create_account(user: User, balance: float) -> Account: #Para crear account se requiere de un valor tipo User y un balance tipo float
        acc = Account(user, balance) ##Crea acc llamando los valores que le mandamos, user y balance
        return acc ##Regresa acc que creamos arriba
