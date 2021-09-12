from toolz import curry, pipe
from typing import Any, Callable, List, Iterable
from inspect import signature


def pipe_until_first(
    element: List[Any], *fns: List[Callable[[Any], List[Any]]]
) -> List[Any]:
    """
    Receive a empty list, and functions that return a list.
    The returned value of each function must be a list, empty or not.
    The function will return the value of the first function that returned
    a not empty list.
    """

    @curry
    def wrapper(fn: Callable[[Any], List[Any]], el: List[Any]):
        return el if len(el) else fn(el)

    return pipe(element, *[wrapper(fn) for fn in fns])


def reversed_curry(
    fn: Callable[[Any], Any], *args: Any, **kwargs: Any
) -> Callable[[Any], Any]:
    """
    It returns a curry function, but the argument passed to the
    returned function will be in the first position.
    """

    params = signature(fn).parameters.values()
    required_params = [param.name for param in params if param.default is param.empty]
    required_params_len = len(required_params)
    required_kwargs = [k for k in kwargs.keys() if k in required_params]

    if len([*args, *required_kwargs]) >= required_params_len:
        return fn(*args, **kwargs)

    def handler(*arguments: Any, **kwarguments: Any):
        required_kwarguments = [k for k in kwarguments.keys() if k in required_params]
        if len([*arguments, *required_kwarguments]) < required_params_len:
            return lambda *a, **k: handler(*a, *arguments, **kwarguments, **k)
        return fn(*arguments, **kwarguments)

    return handler(*args, **kwargs)


def executable_iterator(fns: Iterable[Callable[[None], List[Any]]]):
    """
    Receive a iterator with functions, it will iterate until
    a function return a not empity list.
    """
    try:
        fn = next(fns)
        result = fn()
        return result if len(result) else executable_iterator(fns)
    except StopIteration:
        return []


def caster(fn: Callable[[Any], Any], arg: Any) -> Callable[[Any], Any]:
    """
    Receive a function and argument and return the function.
    Used for lazy functions.
    """

    return lambda: fn(arg)
