from schemas.card import Card


class Transaction:
    def __init__(self, card: Card, amount: float):
        self.card = card #Se llama la funcion card y se agrega el número de tarjeta
        self.amount = amount #Se llama la funcion amount y se agrega el monto 
