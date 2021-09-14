from enum import Enum
from typing import Any


class EnumVar(Enum):
    INVALID_OPTION = None


class BaseEnum(Enum):
    """
    If value provided does't exist, it will return DEFAULT option.
    The child class must implement DEFAULT options.
    """

    @classmethod
    def _missing_(cls, value: object) -> Any:
        return cls.DEFAULT  # type: ignore

    @classmethod
    def show_options(cls):
        return [
            option.value
            for option in list(cls)
            if option.value is not EnumVar.INVALID_OPTION
        ]
