from abc import ABC

from titato.core.player.symbol import SymbolBase, verify_symbol


class CellBase(ABC):
    def __init__(self, symbol: SymbolBase):
        self._symbol = symbol

    @property
    def symbol(self) -> SymbolBase:
        return self._symbol


class Cell(CellBase):
    __slots__ = "_symbol",

    def __init__(self, symbol: SymbolBase):
        verify_symbol(symbol)
        super().__init__(symbol)
