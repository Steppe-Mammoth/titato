from typing import Type, Literal
import pytest

from titato.core.player.player import PlayerBase, Player
from titato.core.player.players import PlayersBase, Players
from titato.core.player.symbol import SymbolBase, Symbol
from titato.exceptions.core_exceptions import PlayerInstanceError, PlayersIsEmptyError
from tests.builder import build_player_list

PLAYERS: Type[PlayersBase] = Players
PLAYER: Type[PlayerBase] = Player
SYMBOL: Type[SymbolBase] = Symbol


def fast_build_player_list(size: Literal[1, 2, 3] = 3):
    return build_player_list(player_t=PLAYER, symbol_t=SYMBOL, size=size)


def test_init_players():
    player_list = fast_build_player_list()
    ps = PLAYERS(players=player_list)

    assert ps.players_list == player_list
    assert ps.current_player == player_list[0]


def test_bad_verify_players_list():
    player_list = fast_build_player_list()
    player_list.append('Sergo_2008')

    with pytest.raises(PlayerInstanceError):
        PLAYERS(players=player_list)

    with pytest.raises(PlayersIsEmptyError):
        PLAYERS(players=[])


def test_set_next_player1():
    player_list = fast_build_player_list()
    ps = PLAYERS(players=player_list)

    p_now = ps.set_get_next_player()
    assert p_now == ps.current_player == player_list[0]

    p_now = ps.set_get_next_player()
    assert p_now == ps.current_player == player_list[1]

    p_now = ps.set_get_next_player()
    assert p_now == ps.current_player == player_list[2]

    p_now = ps.set_get_next_player()
    assert p_now == ps.current_player == player_list[0]


def test_set_next_player2():
    player_list = fast_build_player_list()
    ps = PLAYERS(players=player_list)

    assert ps.current_player == player_list[0]

    p_now = ps.set_get_next_player()
    assert p_now == ps.current_player == player_list[1]

    p_now = ps.set_get_next_player()
    assert p_now == ps.current_player == player_list[2]


def test_shuffle_players():
    player_list = fast_build_player_list()
    ps = PLAYERS(players=player_list)
    assert ps.players_list == player_list

    ps.shuffle_players()
    assert player_list != ps.players_list

    assert ps.current_player == ps.players_list[0]
