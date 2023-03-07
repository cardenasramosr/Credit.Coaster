from schemas.card import Card


class Payment:
    def __init__(self, card: Card, amount: float):
        self.card = card
        self.amount = amount
