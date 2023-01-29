# Do not use methods from this builder, it is for testing purposes only.

from typing import Type, Literal

from titato.core.player.player import PlayerT_co, Player, Role
from titato.core.player.symbol import SymbolBase, Symbol
from titato.core.table.table import TableBase, Table, TableParam


def build_table(row: int,
                column: int,
                comb: int,
                table_t: Type[TableBase] = Table):
    param1 = TableParam(ROW=row, COLUMN=column, COMBINATION=comb)
    return table_t(param1)


def build_player(name: str,
                 symbol: SymbolBase,
                 player_t: Type[PlayerT_co],
                 role: Player.Role = Role.USER) -> PlayerT_co:
    player: PlayerT_co = player_t(name=name, role=role, symbol=symbol)
    return player


def build_player_list(player_t: Type[PlayerT_co] = Player,
                      symbol_t: Type[SymbolBase] = Symbol,
                      size: Literal[1, 2, 3] = 3) -> list[PlayerT_co]:
    players_list = []

    names = ('Vasya-1', 'Egor-2', 'Android Vera-3')
    roles = (Role.USER, Role.USER, Role.ANDROID)
    symbol_name = ['X', 'O', 'I']

    for i in range(size):
        players_list.append(player_t(name=names[i], symbol=symbol_t(symbol_name[i]), role=roles[i]))

    return players_list
