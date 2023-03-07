from controllers.account_controller import AccountController
from controllers.card_controller import CardController
from controllers.payment_controller import PaymentController
from controllers.user_controller import UserController


def test_create_payment():
    # Arrange
    balance = 10_000
    nip = 1234
    payment_amount = 5_000

    user = UserController.create_user("John Doe", "1980-01-01", "123-123-1234")
    account = AccountController.create_account(user, balance)
    card = CardController.create_card(account, nip)

    # Act
    payment = PaymentController.create_payment(card, payment_amount)

    # Assert
    account.balance = balance + payment.amount
