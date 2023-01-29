import random
from abc import ABC, abstractmethod
from typing import Sequence, TypeVar
from itertools import cycle

from titato.core.player.player import PlayerBase, verify_player_instance, PlayerT_co
from titato.exceptions.core_exceptions import PlayersInstanceError, PlayersIsEmptyError

PlayersT_co = TypeVar('PlayersT_co', bound='PlayersBase', covariant=True)


class PlayersBase(ABC):
    def __init__(self, players: list[PlayerT_co]):
        self._player_list = players

    @property
    def players_list(self) -> list[PlayerT_co]:
        return self._player_list

    @property
    @abstractmethod
    def current_player(self) -> PlayerT_co:
        ...

    @abstractmethod
    def set_get_next_player(self) -> PlayerT_co:
        """
        Replaces the current player with the next player in queue and returns it. \n
        New current player available via self.current_player
        """
        ...

    def shuffle_players(self):
        """
        Shuffles the list of player and replaces the queue
        Sets the new current player from the updated queue as the current player \n
        available via self.current_player method.
        """
        ...


class Players(PlayersBase):
    __slots__ = '_player_list', '_current_player'

    def __init__(self, players: list[PlayerT_co]):
        verify_player_list(players=players)
        super().__init__(players.copy())

        self._current_player = None
        self.__queue = None

    @property
    def current_player(self) -> PlayerT_co:
        if not self._current_player:
            self.set_get_next_player()
        return self._current_player

    def set_get_next_player(self) -> PlayerT_co:
        return next(self)

    def shuffle_players(self):
        random.shuffle(self._player_list)
        self.__queue = iter(self)
        self.set_get_next_player()

    def __iter__(self):
        return cycle(self._player_list)

    def __next__(self) -> PlayerT_co:
        if not self.__queue:
            self.__queue = iter(self)

        player = next(self.__queue)
        self._current_player = player
        return player


def verify_players_instance(players: PlayersBase):
    if not isinstance(players, PlayersBase):
        raise PlayersInstanceError


def verify_player_list(players: Sequence[PlayerBase]):
    if len(players) == 0:
        raise PlayersIsEmptyError
    for p in players:
        verify_player_instance(p)
