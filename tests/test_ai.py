from typing import Tuple

from titato.core.game.ai import AIDefault, AIBase
from titato.core.game.cheker import CheckerDefault, CheckerBase
from titato.core.player.player import Player
from titato.core.player.symbol import SymbolBase
from tests.builder import build_table

p_ai = Player(name='AI', symbol=SymbolBase(name='X'))
p_2 = Player(name='Petro', symbol=SymbolBase(name='O'))

AI_FINDER: AIBase.__class__ = AIDefault
CHECKER: CheckerBase.__class__ = CheckerDefault


def test_ai_all_result_for_first_step():
    t = build_table(3, 3, 3)
    ai_all_step = AI_FINDER._find_best_step(symbol=p_ai.symbol, table=t.game_field, combinations=t.combinations)
    ai_get_step = AI_FINDER.get_step(symbol=p_ai.symbol, table=t.game_field, combinations=t.combinations)
    assert ai_all_step.value == [list(comb) for comb in t.combinations]

    assert len(ai_all_step.value) == 8
    assert len(ai_get_step) == 2


def test_ai_one_player_win_3():
    t = build_table(3, 3, 3)
    for i in range(3):
        i_row, i_column = AI_FINDER.get_step(combinations=t.combinations, symbol=p_ai.symbol, table=t.game_field)
        t.set_symbol_cell(index_row=i_row, index_column=i_column, symbol=p_ai.symbol)

    result = CHECKER.result_player(symbol=p_ai.symbol, table=t.game_field, combinations=t.combinations)
    print(result)

    assert isinstance(result, Tuple) and result in t.combinations


def test_ai_all_result_second_step():
    t = build_table(3, 3, 3)
    t.set_symbol_cell(index_row=2, index_column=0, symbol=p_2.symbol)
    t.set_symbol_cell(index_row=1, index_column=0, symbol=p_ai.symbol)  #

    ai_all_step = AI_FINDER._find_best_step(symbol=p_ai.symbol, table=t.game_field, combinations=t.combinations)
    ai_get_step = AI_FINDER.get_step(symbol=p_ai.symbol, table=t.game_field, combinations=t.combinations)

    assert ai_all_step.value == [[(1, 1), (1, 2)]]
    assert ai_get_step in ((1, 1), (1, 2))


def test_ai_battle_1_fail_to_win_enemy_3():  # Перебити гравця не давши зібрати 3/3
    t = build_table(3, 3, 3)
    # comb for player ((1, 2), (1, 0), (*1, 1*))
    t.set_symbol_cell(index_row=1, index_column=2, symbol=p_2.symbol)
    t.set_symbol_cell(index_row=0, index_column=0, symbol=p_ai.symbol)  #
    t.set_symbol_cell(index_row=1, index_column=0, symbol=p_2.symbol)

    i_row, i_column = AI_FINDER.get_step(symbol=p_ai.symbol, table=t.game_field, combinations=t.combinations)
    t.set_symbol_cell(index_row=i_row, index_column=i_column, symbol=p_ai.symbol)  #

    assert t.game_field[1][1].symbol == p_ai.symbol


def test_ai_battle_2_fail_to_win_enemy_3():
    t = build_table(3, 3, 3)
    t.set_symbol_cell(index_row=0, index_column=2, symbol=p_ai.symbol)  #
    t.set_symbol_cell(index_row=2, index_column=0, symbol=p_2.symbol)
    t.set_symbol_cell(index_row=1, index_column=0, symbol=p_ai.symbol)  #
    t.set_symbol_cell(index_row=2, index_column=1, symbol=p_2.symbol)

    ai_get_step = AI_FINDER.get_step(symbol=p_ai.symbol, table=t.game_field, combinations=t.combinations)
    assert ai_get_step == (2, 2)
