import pytest
from uuid import UUID
from src.domain.user.entity import User
from src.domain._exceptions import InvalidAttributesException


@pytest.fixture
def valid_user_data():
    return {"name": "James", "email": "james@email.com", "password": "DJsk9282#"}


@pytest.fixture
def invalid_user_data():
    return {"name": 5, "email": False, "password": 82695963}


@pytest.fixture
def short_user_data():
    return {"name": "al", "password": "Aa@1"}


class TestUser:
    def test_invalid_data_type(self, invalid_user_data):
        with pytest.raises(InvalidAttributesException) as excinfo:
            User(**invalid_user_data)

        for item in invalid_user_data.keys():
            assert f"{item} must be a string" in excinfo.value.message

    def test_invalid_email(self, valid_user_data):
        with pytest.raises(InvalidAttributesException) as excinfo:
            User(**{**valid_user_data, "email": "james@email"})

        assert "email must be a valid email" == excinfo.value.message

    def test_weak_password(self, valid_user_data):
        with pytest.raises(InvalidAttributesException) as excinfo:
            User(**{**valid_user_data, "password": "weak_password"})

        assert "password must be a strong password" == excinfo.value.message

    def test_short_user_data(self, valid_user_data, short_user_data):
        with pytest.raises(InvalidAttributesException) as excinfo:
            User(**{**valid_user_data, **short_user_data})

        assert "name must be greater than 5" in excinfo.value.message
        assert "password must be greater than 8" in excinfo.value.message

    def test_valid_user(self, valid_user_data):
        user = User(**valid_user_data)

        assert user.name == valid_user_data.get("name")
        assert user.email == valid_user_data.get("email")
        assert user.password == valid_user_data.get("password")
        assert isinstance(user._id, UUID)
