from typing import List, TypedDict


class AttributesError(TypedDict):
    name: str
    type: str


class InvalidAttributes(Exception):
    def __init__(self, attributes: List[AttributesError]):
        errors = [
            f"{attribute.get('name')} must be {attribute.get('type')}" for attribute in attributes
        ]
        self.message = ", ".join(errors)
        super().__init__(self.message)

    @property
    def as_dict(self):
        return {"message": self.message}
