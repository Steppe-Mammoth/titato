from titato.core.player.symbol import Symbol
from titato.core.game.cheker import CheckerBase, CheckerDefault
from tests.builder import build_table

CHECKER: CheckerBase = CheckerDefault()

symbol_x = Symbol("X")
symbol_o = Symbol("O")


def set_steps_return_tables():
    t1 = build_table(3, 3, 3)
    t2 = build_table(3, 3, 3)
    t3 = build_table(5, 5, 5)

    t1.set_symbol_cell(0, 0, symbol=symbol_o)  #
    t1.set_symbol_cell(1, 1, symbol=symbol_o)
    t1.set_symbol_cell(1, 0, symbol=symbol_x)
    t1.set_symbol_cell(2, 1, symbol=symbol_x)
    t1.set_symbol_cell(0, 1, symbol=symbol_o)  #
    t1.set_symbol_cell(2, 2, symbol=symbol_x)
    t1.set_symbol_cell(0, 2, symbol=symbol_o)  #

    t2.set_symbol_cell(0, 1, symbol=symbol_o)  #
    t2.set_symbol_cell(1, 1, symbol=symbol_o)  #
    t2.set_symbol_cell(2, 0, symbol=symbol_x)
    t2.set_symbol_cell(0, 0, symbol=symbol_x)
    t2.set_symbol_cell(2, 2, symbol=symbol_x)
    t2.set_symbol_cell(0, 2, symbol=symbol_x)
    t2.set_symbol_cell(2, 1, symbol=symbol_o)  #

    t3.set_symbol_cell(0, 0, symbol=symbol_o)
    t3.set_symbol_cell(1, 1, symbol=symbol_o)
    t3.set_symbol_cell(2, 2, symbol=symbol_o)
    t3.set_symbol_cell(3, 3, symbol=symbol_o)
    t3.set_symbol_cell(4, 4, symbol=symbol_o)
    t3.set_symbol_cell(1, 2, symbol=symbol_x)
    t3.set_symbol_cell(4, 0, symbol=symbol_x)

    return t1, t2, t3


def test_result():
    t1, t2, t3 = set_steps_return_tables()
    result_O_table1 = CHECKER.result_player(symbol=symbol_o, table=t1.game_field, combinations=t1.combinations)
    result_X_table1 = CHECKER.result_player(symbol=symbol_x, table=t1.game_field, combinations=t1.combinations)

    result_O_table2 = CHECKER.result_player(symbol=symbol_o, table=t2.game_field, combinations=t2.combinations)
    result_X_table2 = CHECKER.result_player(symbol=symbol_x, table=t2.game_field, combinations=t2.combinations)

    result_O_table3 = CHECKER.result_player(symbol=symbol_o, table=t3.game_field, combinations=t3.combinations)
    result_X_table3 = CHECKER.result_player(symbol=symbol_x, table=t3.game_field, combinations=t3.combinations)

    assert result_O_table1 == ((0, 0), (0, 1), (0, 2))
    assert result_X_table1 is None

    assert result_O_table2 == ((0, 1), (1, 1), (2, 1))
    assert result_X_table2 is None

    assert result_O_table3 == ((0, 0), (1, 1), (2, 2), (3, 3), (4, 4))
    assert result_X_table3 is None
