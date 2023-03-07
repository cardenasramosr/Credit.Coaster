from schemas.card import Card
from schemas.transaction import Transaction


class TransactionController:

    @staticmethod
    def create_transaction(card: Card, amount: float, nip: int) -> Transaction: #Requerimos de un valor tipo Card, un amount tipo flotante y un nip tipo entero
        acc = card.account 

        if card.nip != nip:
            raise ValueError("Incorrect NIP") #Si el nip esta incorrecto arroja error y Incorrect NIP

        if acc.balance < amount:
            raise ValueError("Transaction amount exceeds balance.") #Si no hay suficiente dinero en la cuenta arroja este error y Transaction amount exceeds balance.

        acc.balance -= amount #Le resta el valor de la transaccion 

        transaction = Transaction(card, amount) #Crea transaction llamando los valores que le mandamos, card y amount

        return transaction #Regresa transaction que creamos arriba
