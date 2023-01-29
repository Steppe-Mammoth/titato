from typing import Type

import pytest

from titato.core.player.symbol import SymbolBase, Symbol
from titato.core.table.param import TableParam
from titato.core.table.table import Table, TableBase, create_2d_list
from titato.exceptions.core_exceptions import CellAlreadyUsedError,\
    TableIndexError, TableParamInstanceError, AllCellsUsedError, ListCombinationsError
from tests.builder import build_table

SYMBOL: Type[SymbolBase] = Symbol
TABLE: Type[TableBase] = Table


def fast_build_table(row: int, column: int, comb: int, ):
    return build_table(row=row, column=column, comb=comb, table_t=TABLE)


symbol_x = SYMBOL('X')
symbol_o = SYMBOL('O')


def test_table_init_user_true():  # TABLE
    param1 = (3, 3, 3)
    param2 = (4, 4, 4)
    param3 = (46, 10, 9)

    table1 = fast_build_table(*param1)
    table2 = fast_build_table(*param2)
    table3 = fast_build_table(*param3)

    g_table1 = create_2d_list(*param1[:2])
    g_table2 = create_2d_list(*param2[:2])
    g_table3 = create_2d_list(*param3[:2])

    assert table1.game_field == g_table1
    assert table2.game_field == g_table2
    assert table3.game_field == g_table3


def test_param_instance_error():
    with pytest.raises(ValueError):
        TableParam(3, 3, 4)


def test_verify_table_param_error():  #
    params = ("2323232", 3, (3, 3, 3))

    for param in params:
        with pytest.raises(TableParamInstanceError):
            TABLE(param)


def test_verify_user_combinations_table_error():  #
    param = TableParam(3, 3, 3)
    combinations = ((((1, 2, 3),),),
                    (((1, 2), (3, 4)), ((2, 4), (4,))),
                    (((1, "2"), (3, 4)), ((5, 4), (1, 4)), ((9, 9),)),
                    (2,), 2, 46, [232, [[[23232, 23]]]],
                    )

    for comb in combinations:
        with pytest.raises(ListCombinationsError):
            TABLE(param, combinations_list=comb)


def test_verify_user_combinations_table_true():
    param = TableParam(3, 3, 3)
    combinations = ((((1, 2),),),
                    (((1, 2), (3, 4)),),
                    (((1, 2), (3, 4)), ((5, 4), (1, 4)), ((9, 5), (1, 0))) * 44
                    )
    for combs in combinations:
        TABLE(param=param, combinations_list=combs)


def test_set_symbol_cell_table():
    table = fast_build_table(3, 3, 3)

    table.set_symbol_cell(index_row=2, index_column=2, symbol=symbol_o)
    assert table.game_field[2][2].symbol == symbol_o

    table.set_symbol_cell(index_row=1, index_column=1, symbol=symbol_x)
    assert table.game_field[1][1].symbol == symbol_x

    table.set_symbol_cell(index_row=1, index_column=0, symbol=symbol_x)
    assert table.game_field[1][0].symbol == symbol_x


def test_bad_set_symbol_cell_index_error():
    table = fast_build_table(3, 3, 3)

    with pytest.raises(TableIndexError):
        table.set_symbol_cell(index_row=1, index_column=3, symbol=symbol_x)

    with pytest.raises(TableIndexError):
        table.set_symbol_cell(index_column=3, index_row=1, symbol=symbol_o)

    with pytest.raises(TableIndexError):
        table.set_symbol_cell(index_column=3, index_row=3, symbol=symbol_o)

    with pytest.raises(TableIndexError):
        table.set_symbol_cell(index_column=-1, index_row=2, symbol=symbol_o)

    with pytest.raises(TableIndexError):
        table.set_symbol_cell(index_column=2, index_row=-1, symbol=symbol_o)


def test_bad_set_symbol_cell_already_used_error():
    table = fast_build_table(3, 3, 3)

    table.set_symbol_cell(index_column=2, index_row=1, symbol=symbol_o)
    table.set_symbol_cell(index_column=1, index_row=2, symbol=symbol_o)
    table.set_symbol_cell(index_column=0, index_row=1, symbol=symbol_o)

    with pytest.raises(CellAlreadyUsedError):
        table.set_symbol_cell(index_column=2, index_row=1, symbol=symbol_x)

    with pytest.raises(CellAlreadyUsedError):
        table.set_symbol_cell(index_column=1, index_row=2, symbol=symbol_o)

    with pytest.raises(CellAlreadyUsedError):
        table.set_symbol_cell(index_column=0, index_row=1, symbol=symbol_x)


def test_count_free_cell():
    table = fast_build_table(3, 3, 3)

    expected_free_cell = 9
    assert table.count_free_cells == expected_free_cell

    table.set_symbol_cell(1, 2, symbol=symbol_o)
    expected_free_cell -= 1
    assert table.count_free_cells == expected_free_cell

    table.set_symbol_cell(0, 0, symbol=symbol_x)
    expected_free_cell -= 1
    assert table.count_free_cells == expected_free_cell

    table.set_symbol_cell(1, 1, symbol=symbol_o)
    expected_free_cell -= 1
    assert table.count_free_cells == expected_free_cell

    table.set_symbol_cell(1, 0, symbol=symbol_x)
    expected_free_cell -= 1
    assert table.count_free_cells == expected_free_cell


def test_bad_set_all_cells_used_error():
    table = fast_build_table(3, 3, 3)
    table._count_free_cells = 1

    table.set_symbol_cell(1, 2, symbol=symbol_o)
    expected_free_cell = 0
    assert table.count_free_cells == expected_free_cell

    with pytest.raises(AllCellsUsedError):
        table.set_symbol_cell(1, 0, symbol=symbol_x)
