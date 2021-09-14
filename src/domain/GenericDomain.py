from typing import Any, Optional, Tuple
from uuid import uuid1
from src.domain._exceptions import InvalidAttributesException

attribute_name = str
error_message = str
error = Tuple[attribute_name, error_message]


class GenericDomain:
    def __init__(self, **kwargs):
        if len(self._errors):
            raise InvalidAttributesException(self._errors)
        self.__asdict = {}
        self._set_attributes(**kwargs)

    def __repr__(self) -> str:
        return str(self.__asdict)

    def _set_attributes(self, **kwargs) -> None:
        for key, value in kwargs.items():
            setattr(self, key, value)
            self.__asdict.update({key: value})

    def _set_id(self, id: Optional[Any]):
        if id is None:
            self._set_attributes(_id=uuid1())
