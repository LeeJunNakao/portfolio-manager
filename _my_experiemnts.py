from enum import Enum


class BaseE(Enum):
    @classmethod
    def _missing_(cls, value):
        return cls.NONE


class Color(BaseE):
    RED = "red"
    BLUE = "blue"
    NONE = None


print(Color("dasdas"))
