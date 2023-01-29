from typing import Optional, TypeVar
from abc import ABC, abstractmethod

from titato.core.table.combinations import CombDefault, verify_combs_list
from titato.core.table.param import TableParam, verify_table_param_instance
from titato.core.table.annotations import CombsTypeT
from titato.core.table.cell import Cell

from titato.core.player.symbol import SymbolBase
from titato.exceptions.core_exceptions import CellAlreadyUsedError,\
    TableIndexError, TableInstanceError, AllCellsUsedError


ClearGameFieldT = tuple[list[None], ...]
GameFieldT = tuple[list[Cell | None], ...]

TableT_co = TypeVar('TableT_co', bound='TableBase', covariant=True)


def create_2d_list(row: int, column: int) -> ClearGameFieldT:
    return tuple([None for _ in range(row)] for _ in range(column))


def verify_game_table(game_table, size_row, size_column):
    if not all((len(game_table) == size_row,
                all([len(column) == size_column for column in game_table]))):
        raise ValueError('VERIFY GAME TABLE')


class TableBase(ABC):
    def __init__(self, param: TableParam):
        self._param = param

    @property
    def param(self) -> TableParam:
        return self._param

    @property
    @abstractmethod
    def game_field(self) -> GameFieldT:
        ...

    @property
    @abstractmethod
    def combinations(self) -> CombsTypeT:
        ...

    @property
    @abstractmethod
    def count_free_cells(self) -> int:
        ...

    @abstractmethod
    def set_symbol_cell(self, index_row: int, index_column: int, symbol: SymbolBase):
        """
        * Sets the transferred character in the specified cell by the row and column indices of the table \n
        * Subtracts the number of free cells by -1 after successful installation.
        """
        ...

    @abstractmethod
    def _remove_free_cell(self):
        ...


class Table(TableBase):
    __slots__ = "_param", "_game_field", "_combinations", "_count_free_cells"

    def __init__(self, param: TableParam, combinations_list: Optional[CombsTypeT] = None):
        """
        :param param: Instance class TableParam
        :param combinations_list: The list of winning combinations is used to
          determine the winning cells for the player.
          Each combination in the list must match the format:
          combs_list[i_comb][i_cell][0]: int -> is index row, and
          combs_list[i_comb][i_cell][1]: int -> is index column.
          If not specified manually,
          then the combinations will be calculated automatically according to the given values from the < self.param >
        """
        verify_table_param_instance(param)
        if not combinations_list:
            combinations_list: CombsTypeT = CombDefault.get_combinations(size_row=param.ROW,
                                                                         size_column=param.COLUMN,
                                                                         size_combination=param.COMBINATION)
        verify_combs_list(combinations_list)
        super().__init__(param)

        self._combinations = combinations_list
        self._count_free_cells = param.ROW * param.COLUMN
        self._game_field = create_2d_list(row=param.ROW, column=param.COLUMN)

    @property
    def game_field(self) -> GameFieldT:
        return self._game_field

    @property
    def combinations(self) -> CombsTypeT:
        return self._combinations

    @property
    def count_free_cells(self) -> int:
        return self._count_free_cells

    def _remove_free_cell(self):
        self._count_free_cells -= 1

    def set_symbol_cell(self, index_row: int, index_column: int, symbol: SymbolBase):
        if self.count_free_cells == 0:
            raise AllCellsUsedError(game_table=self.game_field)

        param = self.param
        table = self.game_field

        if not (param.ROW - 1 >= index_row >= 0) or not (param.COLUMN - 1 >= index_column >= 0):
            raise TableIndexError(index_column, index_row=index_row, table_param=param)

        if used_cell := table[index_row][index_column]:  # Cell != None. None == empty cell
            raise CellAlreadyUsedError(used_cell.symbol.name, new_symbol=symbol.name)

        table[index_row][index_column] = Cell(symbol=symbol)
        self._remove_free_cell()


def verify_table_instance(table: TableBase):
    if not isinstance(table, TableBase):
        raise TableInstanceError
