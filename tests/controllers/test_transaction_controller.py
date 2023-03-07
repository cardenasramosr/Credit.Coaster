import pytest as pytest

from controllers.account_controller import AccountController
from controllers.card_controller import CardController
from controllers.transaction_controller import TransactionController
from controllers.user_controller import UserController


def test_create_correct_transaction():
    # Arrange
    balance = 10_000
    nip = 1234
    transaction_amount = 5_000

    user = UserController.create_user("John Doe", "1980-01-01", "123-123-1234")
    account = AccountController.create_account(user, balance)
    card = CardController.create_card(account, nip)

    # Act
    transaction = TransactionController.create_transaction(card, transaction_amount, nip)

    # Assert
    assert account.balance == balance - transaction.amount


def test_transaction_with_wrong_nip():
    # Arrange
    balance = 10_000
    nip = 1234
    wrong_nip = 9999
    transaction_amount = 5_000

    user = UserController.create_user("John Doe", "1980-01-01", "123-123-1234")
    account = AccountController.create_account(user, balance)
    card = CardController.create_card(account, nip)

    # Act / Assert
    with pytest.raises(ValueError):
        TransactionController.create_transaction(card, transaction_amount, wrong_nip)


def test_transaction_with_invalid_amount():
    # Arrange
    balance = 10_000
    nip = 1234
    transaction_amount = 15_000

    user = UserController.create_user("John Doe", "1980-01-01", "123-123-1234")
    account = AccountController.create_account(user, balance)
    card = CardController.create_card(account, nip)

    # Act / Assert
    with pytest.raises(ValueError):
        TransactionController.create_transaction(card, transaction_amount, nip)
