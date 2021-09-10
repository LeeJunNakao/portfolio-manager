from toolz import pipe
from typing import Callable, List, Tuple
from src.domain._tools.classes import GenericDomain, error
from src.domain._tools.validation_fns import validate_type, validate_email, validate_password


class User(GenericDomain):
    def __init__(self, name: str, email: str, password: str):
        self._errors = self._validate_args_types(name, email, password)
        super().__init__(name=name, email=email, password=password)
             
    def _validate_args_types(self, name: str, email: str, password: str) -> List[error]:
        return pipe([], 
            self._validate_name(name),
            self._validate_email(email), 
            self._validate_password(password)
        )

    def _validate_name(self, name: str) -> Callable[[List[error]], List[error]]:
        is_valid = validate_type(name, str)
        return lambda error_list: [*error_list] if is_valid else [*error_list, ("name", "must be a string")]

    def _validate_email(self, email: str) -> Callable[[List[error]], List[error]]:
        is_valid = validate_email(email)
        return lambda error_list: [*error_list] if is_valid else [*error_list, ("email", "must be a valid email")]
    
    def _validate_password(self, password: str) -> Callable[[List[error]], List[error]]:
        is_valid = validate_password(password)
        return lambda error_list: [*error_list] if is_valid else [*error_list, ("password", "must be a strong password")]
