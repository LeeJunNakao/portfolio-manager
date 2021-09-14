from src.domain._tools.enum import BaseEnum
from typing import Any, List, Sized
from .protocols import error
from src.domain._tools.validation_fns import (
    validate_max_length,
    validate_type,
    validate_min_length,
    validate_email,
    validate_password,
    validate_enum,
)
from src.domain._exceptions.messages import (
    type_message,
    email_message,
    password_message,
    length_message,
    enum_message,
)


def get_validation(name: str, message: str, is_valid: bool) -> List[error]:
    return [] if is_valid else [(name, message)]


def get_type_validation(value: Any, name: str, type_: Any) -> List[error]:
    return get_validation(name, type_message(type_), validate_type(value, type_))


def get_email_validation(value: str, name: str = "email") -> List[error]:
    return get_validation(name, email_message(), validate_email(value))


def get_password_validation(value: str, name: str = "password") -> List[error]:
    return get_validation(name, password_message(), validate_password(value))


def get_len_validation(
    value: Sized,
    name: str,
    limit: int,
    min: bool = False,
) -> List[error]:
    validate = validate_min_length if min else validate_max_length
    return get_validation(name, length_message(limit, min), validate(value, limit))


def get_enum_validation(value: BaseEnum, name: str) -> List[error]:
    return get_validation(name, enum_message(value), validate_enum(value))
