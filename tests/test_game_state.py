from typing import Type
import pytest

from titato.core.game.result import GameStateBase, GameState, ResultCode
from titato.core.player.player import PlayerBase, Player
from titato.core.player.symbol import SymbolBase, Symbol
from titato.exceptions.core_exceptions import ResultCodeError, PlayerInstanceError

GAME_STATE: Type[GameStateBase] = GameState
PLAYER: Type[PlayerBase] = Player
SYMBOL: Type[SymbolBase] = Symbol


def test_init_game_state():
    g_s = GAME_STATE()
    assert g_s.code == ResultCode.NO_RESULT


def test_update_game_state():
    g_s = GAME_STATE()
    win_player = PLAYER(name='Test', symbol=SYMBOL('X'))
    win_comb = ((1, 0), (2, 0), (3, 0))

    g_s.update(code=ResultCode.ALL_CELLS_USED)
    assert g_s.code == ResultCode.ALL_CELLS_USED

    g_s.update(code=ResultCode.WINNER, win_player=win_player, win_combination=win_comb)
    assert g_s.code == ResultCode.WINNER
    assert g_s.win_player == win_player
    assert g_s.win_combination == win_comb


def test_bad_update_game_state():
    g_s = GAME_STATE()
    with pytest.raises(ResultCodeError):
        g_s.update(code="ALL WINNER")

    with pytest.raises(PlayerInstanceError):
        g_s.update(code=ResultCode.WINNER, win_player="NAME: EGPYT")


def test_get_status_game_state():
    g_s = GAME_STATE()
    assert g_s.is_continues is True
    assert g_s.is_finished is False

    g_s.update(code=ResultCode.WINNER)
    assert g_s.is_continues is False
    assert g_s.is_finished is True

    g_s.update(code=ResultCode.ALL_CELLS_USED)
    assert g_s.is_continues is False
    assert g_s.is_finished is True
