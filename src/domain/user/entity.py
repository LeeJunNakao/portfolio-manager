from toolz.functoolz import curry
from src.domain._tools.validation import validation_handler
from src.domain._tools.functional import reversed_curry
from toolz import pipe
from typing import Callable, List
from src.domain.GenericDomain import GenericDomain, error
from src.domain._exceptions.message_handler import (
    get_len_validation,
    get_email_validation,
    get_password_validation,
    get_type_validation,
)


class User(GenericDomain):
    def __init__(self, name: str, email: str, password: str):
        self._errors = self._validate_args_types(name, email, password)
        super().__init__(name=name, email=email, password=password)

    def _validate_args_types(self, name: str, email: str, password: str) -> List[error]:
        return pipe(
            [],
            self._validate_name(name),
            self._validate_email(email),
            self._validate_password(password),
        )

    def __repr__(self) -> str:
        return str({"name": self.name, "email": self.email})  # type: ignore

    @curry
    def _validate_name(self, name: str, errors_list: List[error]) -> List[error]:
        MIN_LENGTH = 5
        MAX_LENGTH = 30

        name_validation = validation_handler(
            name,
            reversed_curry(get_type_validation, "name", str),
            reversed_curry(get_len_validation, "name", MIN_LENGTH, min=True),
            reversed_curry(get_len_validation, "name", MAX_LENGTH),
        )

        return [*errors_list, *name_validation]

    @curry
    def _validate_email(
        self, email: str, errors_list: List[error]
    ) -> Callable[[List[error]], List[error]]:
        MAX_LENGTH = 100
        email_validation = validation_handler(
            email,
            reversed_curry(get_type_validation, "email", str),
            reversed_curry(get_len_validation, "email", MAX_LENGTH),
            get_email_validation,
        )

        return [*errors_list, *email_validation]

    @curry
    def _validate_password(
        self, password: str, errors_list: List[error]
    ) -> Callable[[List[error]], List[error]]:
        MIN_LENGTH = 8
        MAX_LENGTH = 20

        password_validation = validation_handler(
            password,
            reversed_curry(get_type_validation, "password", str),
            reversed_curry(get_len_validation, "password", MIN_LENGTH, min=True),
            reversed_curry(get_len_validation, "password", MAX_LENGTH),
            get_password_validation,
        )

        return [*errors_list, *password_validation]
