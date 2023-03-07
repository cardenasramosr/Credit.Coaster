from schemas.user import User


class Account:
    def __init__(self, user: User, balance: float):
        self.user = user
        self.balance = balance
