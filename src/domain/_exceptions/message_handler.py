from typing import Any, Iterable, List, Sized, Tuple, Union
from .protocols import error
from src.domain._tools.validation_fns import (
    validate_max_length,
    validate_type,
    validate_min_length,
    validate_email,
    validate_password,
)


def get_validation(name: str, message: str, is_valid: bool) -> List[error]:
    return [] if is_valid else [(name, message)]


def get_type_validation(value: Any, name: str, _type: Any) -> List[error]:
    types = {int: "integer", str: "string"}
    return get_validation(
        name, f"must be a {types.get(_type, 'valid type')}", validate_type(value, _type)
    )


def get_email_validation(value: str, name: str = "email") -> List[error]:
    return get_validation(name, "must be a valid email", validate_email(value))


def get_password_validation(value: str, name: str = "password") -> List[error]:
    return get_validation(name, "must be a strong password", validate_password(value))


def get_len_validation(
    value: Sized,
    name: str,
    limit: int,
    min: bool = False,
) -> List[error]:
    operator_text = "greater than" if min else "less than"
    validate = validate_min_length if min else validate_max_length
    return get_validation(
        name, f"must be {operator_text} {limit}", validate(value, limit)
    )
