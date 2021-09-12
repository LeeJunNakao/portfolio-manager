from typing import Any, Callable, Iterable, List
from toolz.functoolz import curry, pipe
from src.domain._exceptions.protocols import error
from src.domain._tools.functional import reversed_curry, executable_iterator, caster
from src.domain._tools.validation_fns import validate_type, validate_min_length
from src.domain._exceptions.message_handler import (
    get_type_validation,
    get_len_validation,
)

passed_value = Any
message_handler = Callable[[Any], List[error]]


def validation_handler(item: passed_value, *fns: message_handler) -> List[error]:
    validators = map(lambda fn: caster(fn, item), fns)
    return executable_iterator(iter(validators))
