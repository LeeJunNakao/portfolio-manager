from uuid import UUID, uuid1
from src.domain._exceptions import InvalidAttributesException
import pytest
from src.domain.portfolio.entity import Portfolio
from src.domain._exceptions.messages import (
    type_message,
    length_message,
)


@pytest.fixture
def valid_portfolio_data():
    return {"name": "stocks", "owner_id": uuid1()}


@pytest.fixture
def invalid_portfolio_data():
    return {"name": True, "owner_id": "ASB-154544"}


class TestPorfolio:
    def test_invalid_type(self, invalid_portfolio_data):
        with pytest.raises(InvalidAttributesException) as execinfo:
            Portfolio(**invalid_portfolio_data)

        assert type_message(str) in execinfo.value.message
        assert type_message(UUID) in execinfo.value.message

    def test_min_lenght(self, valid_portfolio_data):
        MIN_LENGTH = 2

        with pytest.raises(InvalidAttributesException) as execinfo:
            Portfolio(**{**valid_portfolio_data, "name": "a"})

        assert length_message(MIN_LENGTH, True) in execinfo.value.message

    def test_max_lenght(self, valid_portfolio_data):
        MAX_LENGTH = 30

        with pytest.raises(InvalidAttributesException) as execinfo:
            Portfolio(
                **{
                    **valid_portfolio_data,
                    "name": "The longest portfolio name you have ever seen",
                }
            )

        assert length_message(MAX_LENGTH, False) in execinfo.value.message
