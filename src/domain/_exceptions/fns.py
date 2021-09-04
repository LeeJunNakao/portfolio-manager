from . import AttributesError


def getErrorsAttributes(name: str, _type: str) -> AttributesError:
    return {"name": name, "type": _type}
