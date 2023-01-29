from abc import ABC, abstractmethod
from enum import Enum
from typing import TypeVar

from titato.core.player.symbol import SymbolBase, verify_symbol
from titato.exceptions.core_exceptions import BadRoleError, PlayerInstanceError

PlayerT_co = TypeVar('PlayerT_co', bound='PlayerBase', covariant=True)


class Role(Enum):
    USER = 1
    ANDROID = 2


class PlayerBase(ABC):
    def __init__(self, name: str, symbol: SymbolBase, role: Role):
        self.name = name
        self._symbol = symbol
        self._role = role
        self._count_steps = 0

    @property
    def role(self) -> Role:
        return self._role

    @property
    def symbol(self) -> SymbolBase:
        return self._symbol

    @property
    def count_steps(self) -> int:
        return self._count_steps

    @property
    @abstractmethod
    def is_android(self) -> bool:
        ...

    @property
    @abstractmethod
    def is_user(self) -> bool:
        ...

    def add_count_step(self):
        self._count_steps += 1


class Player(PlayerBase):
    Role = Role

    __slots__ = "name", "_symbol", "_count_steps", "_role"

    def __init__(self, name: str, symbol: SymbolBase, role: Role = Role.USER):
        verify_role(role=role)
        verify_symbol(symbol)
        super().__init__(name=name, symbol=symbol, role=role)

    @property
    def is_android(self) -> bool:
        return self.role == self.Role.ANDROID

    @property
    def is_user(self) -> bool:
        return self.role == self.Role.USER


def verify_role(role: Role):
    if not type(role) is Role or role not in Role:
        raise BadRoleError


def verify_player_instance(player: PlayerBase):
    if not isinstance(player, PlayerBase):
        raise PlayerInstanceError
