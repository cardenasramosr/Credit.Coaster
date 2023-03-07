
from controllers.user_controller import UserController
from schemas.account import Account
from schemas.user import User


def test_create_user():
    # Arrange
    name = "John Doe"
    birthdate = "1980-01-01"
    phone = "123-123-1234"

    # Act
    user = UserController.create_user(name, birthdate, phone)

    # Assert
    assert isinstance(user, User)
    assert user.name == name
    assert user.birthdate == birthdate
    assert user.phone == phone
