from typing import Sequence, Optional, Type
from abc import ABC, abstractmethod

from titato.core.player.symbol import SymbolBase
from titato.core.table.annotations import CombTypeT, CombsTypeT
from titato.core.table.cell import Cell
from titato.exceptions import CheckerError


class CheckerBase(ABC):
    @abstractmethod
    def result_player(self,
                      symbol: SymbolBase,
                      table: Sequence[list[Cell | None]],
                      combinations: CombsTypeT) -> Optional[CombTypeT]:
        """
        The function checks in the given table for matches of the given symbol
        in each combination in the combinations given by the argument.\n
        If it exists – returns the winning combination for the transmitted symbol.
        """
        ...


class CheckerDefault(CheckerBase):

    @classmethod
    def result_player(cls,
                      symbol: SymbolBase,
                      table: Sequence[list[Optional[Cell]]],
                      combinations: CombsTypeT) -> Optional[CombTypeT]:

        for combination in combinations:
            count_matches = 0

            for index_row, index_column in combination:
                cell = table[index_row][index_column]

                if (cell is not None) and (cell.symbol == symbol):  # cell has an identical symbol
                    count_matches += 1

            if len(combination) == count_matches:
                win_comb = combination  # ((0, 0), (0, 1), (0, 2))
                return win_comb


def verify_checker_instance(checker: Type[CheckerBase] | CheckerBase):
    if not any(((
            isinstance(checker, type) and issubclass(checker, CheckerBase) and checker != CheckerBase),
            isinstance(checker, CheckerBase))):
        raise CheckerError
