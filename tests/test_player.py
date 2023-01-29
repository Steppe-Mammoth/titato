from typing import Type
import pytest

from titato.core.player.player import PlayerBase, Player, Role
from titato.core.player.symbol import SymbolBase, Symbol
from titato.exceptions.core_exceptions import BadRoleError, SymbolError

PLAYER: Type[PlayerBase] = Player
SYMBOL: Type[SymbolBase] = Symbol


def test_player_init():
    symbol = SYMBOL("X")
    role = Role.USER

    p = PLAYER(name='Vasil', symbol=symbol, role=role)
    assert p.role == role
    assert p.count_steps == 0
    assert p.symbol == symbol
    assert p.is_user is True
    assert p.is_android is False

    role = Role.ANDROID
    p = PLAYER(name='Android Vasil', symbol=symbol, role=role)

    assert p.role == role
    assert p.is_user is False
    assert p.is_android is True


def test_bad_verify_player_role():
    symbol = SYMBOL("X")

    with pytest.raises(BadRoleError):
        role = "Android"
        PLAYER(name='Vasil', symbol=symbol, role=role)

    with pytest.raises(BadRoleError):
        role = 1
        PLAYER(name='Vasil', symbol=symbol, role=role)

    with pytest.raises(BadRoleError):
        role = Role
        PLAYER(name='Vasil', symbol=symbol, role=role)


def test_bad_verify_player_symbol():
    role = Role.USER
    with pytest.raises(SymbolError):
        PLAYER(name='Vasil', symbol="O", role=role)

    with pytest.raises(SymbolError):
        PLAYER(name='Vasil', symbol=2, role=role)

    with pytest.raises(SymbolError):
        PLAYER(name='Vasil', symbol=Symbol, role=role)


def test_add_count_step_player():
    symbol = SYMBOL("X")
    role = Role.USER
    p = PLAYER(name='Vasil', symbol=symbol, role=role)

    expected_count_step = 0
    assert p.count_steps == expected_count_step

    for _ in range(10):
        p.add_count_step()
        expected_count_step += 1
        assert p.count_steps == expected_count_step
