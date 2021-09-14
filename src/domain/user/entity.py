from toolz import pipe, curry
from uuid import uuid1
from src.domain._tools.validation import validation_handler
from src.domain._tools.functional import reversed_curry
from typing import List, Optional
from src.domain.GenericDomain import GenericDomain, error
from src.domain._exceptions.message_handler import (
    get_len_validation,
    get_email_validation,
    get_password_validation,
    get_type_validation,
)


class User(GenericDomain):
    def __init__(self, name: str, email: str, password: str, _id: Optional[int] = None):
        self._errors = self._validate_args_types(name, email, password)
        GenericDomain.__init__(self, name=name, email=email, password=password, _id=_id)
        self._set_id(_id)

    def _set_id(self, id: Optional[int]):
        if id is None:
            self._set_attributes(_id=uuid1())

    def _validate_args_types(self, name: str, email: str, password: str) -> List[error]:
        return pipe(
            [],
            self._validate_name(name),
            self._validate_email(email),
            self._validate_password(password),
        )

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
    def _validate_email(self, email: str, errors_list: List[error]) -> List[error]:
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
    ) -> List[error]:
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
