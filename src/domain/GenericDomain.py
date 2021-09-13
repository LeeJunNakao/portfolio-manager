from typing import Any, Tuple, List
from src.domain._exceptions import InvalidAttributes

attribute_name = str
error_message = str
error = Tuple[attribute_name, error_message]


class GenericDomain:
    def __init__(self, **kwargs):
        if len(self._errors):
            raise InvalidAttributes(self._errors)
        self.__asdict = {}
        self._set_attributes(**kwargs)

    def __repr__(self) -> str:
        return str(self.__asdict)

    def _set_attributes(self, **kwargs) -> None:
        for key, value in kwargs.items():
            setattr(self, key, value)
            self.__asdict.update({key: value})
