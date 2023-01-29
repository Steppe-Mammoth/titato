from typing import Type, NamedTuple, Sequence, Literal
import pytest

from titato.core.game.cheker import CheckerBase, CheckerDefault
from titato.core.game.game_xo import GameBase, Game
from titato.core.player.player import PlayerBase, Player
from titato.core.player.players import PlayersBase, Players
from titato.core.game.result import GameStateBase, GameState, ResultCode
from titato.core.table.table import TableBase, Table, TableParam
from titato.exceptions.core_exceptions import CellAlreadyUsedError,\
    PlayersInstanceError, CheckerError, TableInstanceError
from tests.builder import build_table, build_player_list


PLAYER: Type[PlayerBase] = Player
PLAYERS: Type[PlayersBase] = Players
TABLE: Type[TableBase] = Table
GAME_STATE: Type[GameStateBase] = GameState
CHECKER: Type[CheckerBase] = CheckerDefault
GAME: Type[GameBase] = Game


class GameElements(NamedTuple):
    game: GameBase
    table: TableBase
    players: PlayersBase
    players_list: Sequence[PlayerBase]
    game_state: GameStateBase


def fast_build_game(row: int = 3,
                    column: int = 3,
                    comb: int = 3,
                    count_players: Literal[1, 2, 3] = 3):
    table = build_table(row, column, comb, table_t=TABLE)
    players_list = build_player_list(player_t=PLAYER, size=count_players)
    players = PLAYERS(players_list)
    game_state = GAME_STATE()
    checker = CHECKER

    game = GAME(players=players,
                table=table,
                game_state=game_state,
                checker=checker)

    return GameElements(game=game, table=table, players=players, players_list=players_list, game_state=game_state)


def test_init_game():
    g = fast_build_game()
    game = g.game

    assert game.table == g.table
    assert game.game_state == g.game_state
    assert game.players == g.players


def test_get_game_table_game():
    g = fast_build_game()
    game = g.game
    assert game.game_field == g.table.game_field


def test_get_current_player_game():
    g1 = fast_build_game()
    game1 = g1.game
    assert game1.current_player == g1.players.current_player == g1.players_list[0]

    g2 = fast_build_game()
    game2 = g2.game
    game2.players.shuffle_players()
    assert game2.current_player == game2.players.players_list[0]


def test_set_get_next_player_game():
    g = fast_build_game(count_players=2)
    game = g.game

    p1 = game.set_get_next_player()
    assert p1 == g.players.players_list[0]

    p2 = game.set_get_next_player()
    assert p2 == g.players.players_list[1]

    p3 = game.set_get_next_player()
    assert p3 == g.players.players_list[0] == p1


def test_set_winner_game():
    w_comb = ((0, 1), (1, 1))
    g = fast_build_game(count_players=2)
    game = g.game
    assert game.game_state.is_finished is False
    game.set_winner(game.current_player, win_combination=w_comb)
    assert game.game_state.is_finished is True
    assert game.game_state.code == ResultCode.WINNER
    assert game.game_state.win_player == game.current_player
    assert game.game_state.win_combination == w_comb


def test_set_draw_game():
    g = fast_build_game(count_players=2)
    game = g.game
    assert game.game_state.is_finished is False
    game.set_draw()
    assert game.game_state.is_finished is True
    assert game.game_state.code == ResultCode.ALL_CELLS_USED


def test_winner_game():
    g = fast_build_game(count_players=2)
    game = g.game

    p1 = game.current_player
    game.step(2, 2, player=p1)
    result = game.result(p1)
    assert result.code == ResultCode.NO_RESULT
    assert result.is_continues is True

    p2 = game.set_get_next_player()
    game.step(1, 2, player=p2)
    result = game.result(p2)
    assert result.code == ResultCode.NO_RESULT
    assert result.is_continues is True

    p1_2 = game.set_get_next_player()
    game.step(0, 2, player=p1_2)
    result = game.result(p1_2)
    assert result.code == ResultCode.NO_RESULT
    assert result.is_continues is True

    p2_2 = game.set_get_next_player()
    game.step(1, 0, player=p2_2)
    result = game.result(p2_2)
    assert result.code == ResultCode.NO_RESULT
    assert result.is_continues is True
    assert result.is_finished is False

    p1_3 = game.set_get_next_player()
    game.step(0, 0, player=p1_3)
    result = game.result(p1_3)
    assert result.code == ResultCode.NO_RESULT
    assert result.is_continues is True

    p2_3 = game.set_get_next_player()
    game.step(1, 1, player=p2_3)
    result = game.result(p2_3)
    assert result.code == ResultCode.WINNER
    assert result.is_continues is False
    assert result.is_finished is True

    assert p1_3 == p1_2 == p1
    assert p2_3 == p2_2 == p2
    assert p2 == game.game_state.win_player
    assert ((1, 0), (1, 1), (1, 2)) == game.game_state.win_combination
    assert game.table.count_free_cells == 3
    assert p2.count_steps == p1.count_steps == 3


def test_ai_winner_game():
    g = fast_build_game(count_players=1)
    game = g.game
    p = game.current_player

    while not game.game_state.is_finished:
        game.ai_step_result(player=p)

    assert p.count_steps == 3
    assert game.game_state.win_player == p


def test_ai_draw_game():
    g = fast_build_game(3, 3, 3, count_players=3)
    game = g.game
    p1, p2, p3 = g.players_list

    while not game.game_state.is_finished:
        game.ai_step_result(player=game.current_player)
        assert p2 == game.set_get_next_player()

        game.ai_step_result(player=game.current_player)
        assert p3 == game.set_get_next_player()

        game.ai_step_result(player=game.current_player)
        assert p1 == game.set_get_next_player()

    assert p1.count_steps == p2.count_steps == p3.count_steps == 3
    assert game.table.count_free_cells == 0


def test_set_in_used_cell_game_error():
    g = fast_build_game(3, 3, 3, count_players=2)
    game = g.game
    p1, p2 = g.players_list
    game.step(1, 1, p1)

    with pytest.raises(CellAlreadyUsedError):
        game.step(1, 1, p1)

    with pytest.raises(CellAlreadyUsedError):
        game.step(1, 1, p2)


def test_bad_verify_players_instance_error_game():
    param = TableParam(3, 3, 3)
    players_list = [param, Players, PlayersBase, 'fdfd', 34343]
    for ps in players_list:
        with pytest.raises(PlayersInstanceError):
            GAME(players=ps, table=Table(param))


def test_bad_verify_table_instance_error_game():
    g = fast_build_game(3, 3, 3, count_players=2)
    players = g.players

    param = TableParam(3, 3, 3)
    table_list = [param, Table, TableBase, 'fdfd', 34343]
    for t in table_list:
        with pytest.raises(TableInstanceError):
            GAME(players=players, table=t)


def test_bad_verify_checker_instance_error_game():
    g = fast_build_game(3, 3, 3, count_players=2)
    players = g.players

    param = TableParam(3, 3, 3)
    checker_list = [param, CheckerBase, 'fdfd', 34343]
    for ch in checker_list:
        with pytest.raises(CheckerError):
            GAME(players=players,
                 table=Table(param),
                 checker=ch)
