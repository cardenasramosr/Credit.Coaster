from controllers.account_controller import AccountController
from controllers.card_controller import CardController
from controllers.user_controller import UserController
from schemas.card import Card


def test_create_card():
    # Arrange
    balance = 10_000
    nip = 1234

    user = UserController.create_user("John Doe", "1980-01-01", "123-123-1234")
    account = AccountController.create_account(user, balance)

    # Act
    card = CardController.create_card(account, nip)

    # Assert
    assert isinstance(card, Card)
    assert card.nip == 1234
    assert id(card.account) == id(account)
