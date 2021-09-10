from typing import List, TypedDict, Tuple
from src.domain._tools.classes import error

class InvalidAttributes(Exception):
    def __init__(self, attributes: List[error]):
        errors = [
            f"{name} must be {msg}" for name, msg in attributes
        ]
        self._attributes = attributes
        self.message = ", ".join(errors)
        super().__init__(self.message)

    @property
    def as_dict(self):
        return { 
            "error": { 
                name: msg for name, msg in self._attributes
            }
        }
