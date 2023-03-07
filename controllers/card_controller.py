from schemas.account import Account
from schemas.card import Card


class CardController:

    @staticmethod
    def create_card(account: Account, nip: int) -> Card: #Para crear card se requiere de un valor tipo Account y un nip tipo int
        card = Card(account, nip) #Crea card llamando los valores que le mandamos, account y nip
        return card #Regresa card que creamos arriba
