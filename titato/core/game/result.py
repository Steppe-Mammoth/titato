from abc import ABC, abstractmethod
from enum import Enum
from typing import Optional, TypeVar

from titato.core.player.player import PlayerBase, verify_player_instance
from titato.core.table.annotations import CombTypeT
from titato.exceptions.core_exceptions import ResultCodeError

GameStateT_co = TypeVar('GameStateT_co', bound='GameStateBase', covariant=True)


class ResultCode(Enum):
    NO_RESULT = 0
    ALL_CELLS_USED = 1
    WINNER = 2


class GameStateBase(ABC):
    def __init__(self):
        self._code: ResultCode = ResultCode.NO_RESULT
        self._win_player: Optional[PlayerBase] = None
        self._win_combination: Optional[CombTypeT] = None

    @property
    def code(self) -> ResultCode:
        return self._code

    @property
    def win_player(self) -> Optional[PlayerBase]:
        return self._win_player

    @property
    def win_combination(self) -> Optional[CombTypeT]:
        return self._win_combination

    @property
    @abstractmethod
    def is_finished(self) -> bool:
        ...

    @property
    @abstractmethod
    def is_continues(self) -> bool:
        ...

    @property
    @abstractmethod
    def is_winner(self) -> bool:
        ...

    @property
    @abstractmethod
    def is_draw(self) -> bool:
        ...

    @abstractmethod
    def update(self,
               code: Optional[ResultCode] = None,
               win_player: Optional[PlayerBase] = None,
               win_combination: Optional[CombTypeT] = None):
        ...


class GameState(GameStateBase):
    __slots__ = "_code", "_win_player", "_win_combination"

    @property
    def is_finished(self) -> bool:
        return self._code != ResultCode.NO_RESULT

    @property
    def is_continues(self) -> bool:
        return self._code == ResultCode.NO_RESULT

    @property
    def is_winner(self) -> bool:
        return self._code == ResultCode.WINNER

    @property
    def is_draw(self) -> bool:
        return self._code == ResultCode.ALL_CELLS_USED

    def update(self,
               code: Optional[ResultCode] = None,
               win_player: Optional[PlayerBase] = None,
               win_combination: Optional[CombTypeT] = None):

        if code:
            verified_result_code(code)
            self._code = code

        if win_player:
            verify_player_instance(win_player)
            self._win_player = win_player

        if win_combination:
            self._win_combination = win_combination


def verified_result_code(code: ResultCode):
    if not isinstance(code, ResultCode):
        raise ResultCodeError('Only ResultsCode object ')  # create raise
