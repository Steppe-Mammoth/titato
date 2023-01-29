import pytest

from titato.core.table.cell import Cell
from titato.core.player.symbol import Symbol
from titato.exceptions.core_exceptions import SymbolError


def test_init_cell_true():
    for symbol_name in ['X', 'QWQ', 1, 2, [234]]:
        symbol = Symbol(name=symbol_name)
        Cell(symbol=symbol)


def test_init_cell_error():
    for bad_symbol in ['X', 'QWQ', 1, 2, [234]]:
        with pytest.raises(SymbolError):
            Cell(symbol=bad_symbol)
