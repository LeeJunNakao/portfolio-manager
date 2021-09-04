import re
from typing import List, Match
from src.domain._exceptions import InvalidAttributes
from src.domain._exceptions.fns import getErrorsAttributes

email_regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"


class User():
    def __init__(self, name: str, email: str, password: str):
        self._errors = []
        self.name = name
        self.email = email
        self.password = password
        self._verify_errors()

    def _validate_name(self, name: str):
        if type(name) != str:
            self._errors.append(getErrorsAttributes("name", "string"))

    def _validate_email(self, email: str):
        if type(email) != str:
            self._errors.append(getErrorsAttributes("email", "string"))
        elif not re.match(email_regex, email):
            self._errors.append(getErrorsAttributes("email", "valid email"))

    def _verify_errors(self):
        if len(self._errors):
            raise InvalidAttributes(self._errors)

    def __setattr__(self, name: str, value) -> None:
        if name == "name":
            self._validate_name(value)
        if name == "email":
            self._validate_email(value)

        super().__setattr__(name, value)

    def __repr__(self) -> str:
        return f"name: {self.name}, email: {self.email}"
