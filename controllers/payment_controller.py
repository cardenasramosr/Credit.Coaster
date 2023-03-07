from schemas.card import Card
from schemas.payment import Payment


class PaymentController:

    @staticmethod
    def create_payment(card: Card, amount: float) -> Payment: #Para crear payment se requiere de un valor tipo card  y un amount tipo flotante
        acc = card.account

        acc.balance += amount #Le suma el valor de la transaccion 

        payment = Payment(card, amount) #Crea payment llamando los valores que le mandamos, card y amount

        return payment #Regresa payment que creamos arriba
