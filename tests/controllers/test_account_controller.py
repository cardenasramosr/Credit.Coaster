
from controllers.user_controller import UserController
from schemas.account import Account
from controllers.account_controller import AccountController
def test_create_account():
    # Arrange
    balance = 10_000

    user = UserController.create_user("John Doe", "1980-01-01", "123-123-1234")

    # Act
    account = AccountController.create_account(user, balance)

    # Assert
    assert isinstance(account, Account)
    assert account.balance == balance
    assert id(account.user) == id(user)
