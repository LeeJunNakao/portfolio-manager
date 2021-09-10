import re
from typing import Any

def validate_type(value: Any, _type: Any) -> bool:
        return True if type(value) == _type else False

def validate_email(value: str) -> bool:
    email_regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"

    return True if re.match(email_regex, value) else False

def validate_password(value: str) -> bool:
    has_lowercase = re.search("[a-z]", value) is not None
    has_uppercase = re.search("[A-Z]", value) is not None
    has_number = re.search("[0-9]", value) is not None
    is_min_length_valid = len(value) >= 8
    is_max_length_valid = len(value) <= 20

    return has_lowercase and has_uppercase and has_number and is_min_length_valid and is_max_length_valid
    