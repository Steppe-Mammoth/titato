import random
from abc import ABC, abstractmethod
from enum import Enum
from typing import Sequence, NamedTuple, Optional

from titato.core.player.symbol import SymbolBase
from titato.core.table.annotations import CellIndexT, CombsTypeT, CombTypeT
from titato.core.table.cell import Cell


ListCombsType = list[list[CellIndexT]]
ResultCombs = CellIndexT | CombTypeT | ListCombsType


class AIResultCode(Enum):
    BestCell = 1
    BestCombs = 2
    EmptyCells = 3


class AIResult(NamedTuple):
    result_code: AIResultCode
    value: ResultCombs


class AIBase(ABC):
    @abstractmethod
    def get_step(self,
                 symbol: SymbolBase,
                 table: Sequence[list[Cell | None]],
                 combinations: CombsTypeT) -> CellIndexT:
        """
        The function finds the best option for the AI step.\n
        Returns a tuple of two elements, in which the first is the index of the row,
        and the second is the index of the column of the two-dimensional table.
        """
        ...


class AIDefault(AIBase):
    @classmethod
    def get_step(cls,
                 symbol: SymbolBase,
                 table: Sequence[list[Cell | None]],
                 combinations: CombsTypeT) -> CellIndexT:
        cell_index: CellIndexT
        result = cls._find_best_step(symbol, table=table, combinations=combinations)

        match result.result_code:

            case AIResultCode.BestCell:
                cell_index = result.value
            case AIResultCode.BestCombs:
                cell_index = random.choice(random.choice(result.value))
            case AIResultCode.EmptyCells:
                cell_index = random.choice(result.value)
            case _ as err:
                raise ValueError(f'Find Error. Not supported value: {err}')

        return cell_index

    @classmethod
    def _find_best_step(cls, symbol, table: Sequence[list[Cell | None]], combinations: CombsTypeT) -> AIResult:

        result_code = None
        value: Optional[ResultCombs] = None

        my_priority_steps = []
        enemy_win_cell = ()
        empty_cells = set()

        for combination in combinations:

            count_my_cell_in_comb = 0
            count_enemy_cell_in_comb = 0
            count_empty_in_comb = 0
            empty_cells_in_comb = []

            for step_comb in combination:
                index_row, index_column = step_comb
                cell = table[index_row][index_column]

                if cell is None:
                    count_empty_in_comb += 1
                    empty_cells_in_comb.append(step_comb)

                elif cell.symbol == symbol:
                    count_my_cell_in_comb += 1
                else:
                    count_enemy_cell_in_comb += 1

            if count_enemy_cell_in_comb == 0:  # Only my_cell + empty_cell in combination
                if count_empty_in_comb == 1:  # One my step left to win this combination
                    result_code = AIResultCode.BestCell
                    value = empty_cells_in_comb[0]
                    break

                elif not my_priority_steps or len(my_priority_steps[0]) > count_empty_in_comb:
                    my_priority_steps = list([empty_cells_in_comb])

                elif len(my_priority_steps[0]) == count_empty_in_comb:
                    my_priority_steps.append(empty_cells_in_comb)

            elif count_my_cell_in_comb == 0:  # Only enemy_cell + empty_cell in combination
                if count_empty_in_comb == 1:  # One enemy step left to win this combination
                    enemy_win_cell = empty_cells_in_comb[0]

            else:
                empty_cells.update(empty_cells_in_comb)

        if result_code and value:
            pass

        elif enemy_win_cell:
            result_code = AIResultCode.BestCell
            value: CellIndexT = enemy_win_cell

        elif my_priority_steps:
            result_code = AIResultCode.BestCombs
            value: ListCombsType = my_priority_steps
        else:
            result_code = AIResultCode.EmptyCells
            value: CombTypeT = tuple(empty_cells)

        return AIResult(result_code=result_code, value=value)
