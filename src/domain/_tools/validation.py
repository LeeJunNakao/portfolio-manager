from typing import Any, Callable, Iterable, List
from src.domain._exceptions.protocols import error
from src.domain._tools.functional import executable_iterator, caster

passed_value = Any
message_handler = Callable[[Any], List[error]]


def validation_handler(item: passed_value, *fns: message_handler) -> List[error]:
    """
    The item provided will be passed to provided functions, in sequence.
    It will pass item through functions until one of functions return a not empty list.
    """

    validators = iter(map(lambda fn: caster(fn, item), fns))
    list_errors = executable_iterator(validators)
    return list_errors
