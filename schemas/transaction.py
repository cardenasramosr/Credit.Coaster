from schemas.card import Card


class Transaction:
    def __init__(self, card: Card, amount: float):
        self.card = card
        self.amount = amount
