from src.domain._tools.enum import BaseEnum
from typing import Any
from uuid import UUID


def type_message(_type: Any) -> str:
    types = {int: "integer", str: "string", UUID: "uuid"}

    return f"must be a {types.get(_type, 'valid type')}"


def email_message() -> str:
    return "must be a valid email"


def password_message() -> str:
    return "must be a strong password"


def length_message(limit: int, min) -> str:
    operator_text = "greater than" if min else "less than"
    return f"must be {operator_text} {limit}"


def enum_message(value: BaseEnum) -> str:
    options = value.show_options()
    return f"must be a valid value. Options: {options}"
