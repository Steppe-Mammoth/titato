from abc import ABC

from titato.exceptions.core_exceptions import SymbolError


class SymbolBase(ABC):
    __slots__ = "name"

    def __init__(self, name: str):
        self.name = name


class Symbol(SymbolBase):
    ...


def verify_symbol(symbol):
    if not isinstance(symbol, SymbolBase):
        raise SymbolError
