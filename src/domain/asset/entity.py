from uuid import UUID
from typing import List
from toolz import pipe, curry
from src.domain._tools.functional import reversed_curry
from src.domain._exceptions.message_handler import (
    get_enum_validation,
    get_len_validation,
    get_type_validation,
)
from src.domain._tools.validation import validation_handler
from src.domain.GenericDomain import GenericDomain
from src.domain._exceptions.protocols import error
from src.domain._tools.enum import BaseEnum, EnumVar


class AssetCategory(BaseEnum):
    STOCK = "stock"
    COIN = "currency"
    CRIPTO = "criptoasset"
    DEFAULT = EnumVar.INVALID_OPTION


class Asset(GenericDomain):
    def __init__(self, name: str, owner_id: UUID, category: AssetCategory, id_: UUID):
        self._errors = self._validate_args_types(name, owner_id, category)
        GenericDomain.__init__(self, name=name, owner_id=owner_id, category=category)
        self._set_id(id_)

    def _validate_args_types(
        self, name: str, owner_id: UUID, category: AssetCategory
    ) -> List[error]:
        return pipe(
            [],
            self._validate_name(name),
            self._validate_owner_id(owner_id),
            self._validate_category(category),
        )

    @curry
    def _validate_name(self, name: str, list_error: List[error]):
        MIN_LENGTH = 2
        MAX_LENGTH = 30
        validation = validation_handler(
            name,
            reversed_curry(get_type_validation, "name", str),
            reversed_curry(get_len_validation, "name", MIN_LENGTH, min=True),
            reversed_curry(get_len_validation, "name", MAX_LENGTH),
        )

        return [*list_error, *validation]

    @curry
    def _validate_owner_id(self, owner_id: UUID, list_error: List[error]):
        validation = get_type_validation(owner_id, "owner_id", UUID)

        return [*list_error, *validation]

    @curry
    def _validate_category(self, category: AssetCategory, list_error: List[error]):
        validation = get_enum_validation(
            category,
            "category",
        )

        return [*list_error, *validation]
