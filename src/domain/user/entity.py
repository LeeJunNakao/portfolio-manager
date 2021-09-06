import re
from toolz import pipe
from typing import Any, Dict, List, Match, Optional, TypedDict
from src.domain._exceptions import InvalidAttributes, AttributesError
from src.domain._exceptions.fns import getErrorsAttributes

class ValidationResult:
    def __init__(self, fields: Dict[str, Any], result: Optional[Dict[str, bool]]=None) -> None:
        self.fields = {**fields}
        self.result = {**result} if result else {item: False for item in fields.keys()}

    def __repr__(self) -> str:
        return str({ "fields": self.fields, "result": self.result})
    
    def get_updated_result(self, field, status) -> Dict[str, any]:
        return { "fields": self.fields, "result": {**self.result, field: status}}


class User():
    def __init__(self, name: str, email: str, password: str):
        self._errors: List[AttributesError] = []
        self._verify_args_types(name=name, email=email, password=password)
    
    def _verify_args_types(self,**fields) -> None:
        pipe(ValidationResult(fields), self._validate_name, self._validate_email, self._validate_password, print)
        
    def _validate_name(self, validation_result: ValidationResult) -> ValidationResult:
        result = True if type(validation_result.fields.get("name")) == str else False
        return ValidationResult(**validation_result.get_updated_result("name", result))     

    def _validate_email(self, validation_result: ValidationResult) -> ValidationResult:
        email_regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        result = True if re.match(email_regex, validation_result.fields.get("email")) else False
        return ValidationResult(**validation_result.get_updated_result("email", result))
    
    def _validate_password(self, validation_result: ValidationResult) -> ValidationResult:
        password = validation_result.fields.get("password")
        has_lowercase = re.search("[a-z]", password)
        has_uppercase = re.search("[A-Z]", password)
        has_number = re.search("[0-9]", password)
        is_min_length_valid = len(password) >= 8
        is_max_length_valid = len(password) <= 20

        result = has_lowercase is not None and has_uppercase is not None and has_number is not None and is_min_length_valid and is_max_length_valid
        
        return ValidationResult(**validation_result.get_updated_result("password", result))
