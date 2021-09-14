from toolz.functoolz import curry, pipe
from uuid import UUID
from src.domain._tools.validation import validation_handler
from src.domain._tools.functional import reversed_curry
from typing import Any, Optional, List
from src.domain.GenericDomain import GenericDomain
from src.domain._exceptions.protocols import error
from src.domain._exceptions.message_handler import (
    get_type_validation,
    get_len_validation,
)


class Portfolio(GenericDomain):
    def __init__(self, name: str, owner_id: UUID, id_: Optional[Any] = None):
        self._errors = self._validate_args_types(name, owner_id)
        GenericDomain.__init__(self, name=name, id_=id_, owner_id=owner_id)
        self._set_id(id_)

    def _validate_args_types(self, name: str, owner_id: UUID) -> List[error]:
        return pipe([], self._validate_name(name), self._validate_owner_id(owner_id))

    @curry
    def _validate_name(self, name: str, list_error: List[error]) -> List[error]:
        MIN_LENGTH = 2
        MAX_LENGTH = 30

        name_validation = validation_handler(
            name,
            reversed_curry(get_type_validation, "name", str),
            reversed_curry(get_len_validation, "name", MIN_LENGTH, min=True),
            reversed_curry(get_len_validation, "name", MAX_LENGTH),
        )

        return [*list_error, *name_validation]

    @curry
    def _validate_owner_id(self, owner_id: UUID, list_error: List[error]):
        validation_owner_id = validation_handler(
            owner_id, reversed_curry(get_type_validation, "owner_id", UUID)
        )

        return [*list_error, *validation_owner_id]
