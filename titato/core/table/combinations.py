from enum import Enum
from abc import ABC, abstractmethod
from functools import lru_cache
from typing import Optional

from titato.core.table.annotations import CombsTypeT, CombTypeT, CellIndexT
from titato.exceptions.core_exceptions import ListCombinationsError
from titato.setting import SIZE_CACHE_COMBINATIONS


class Vectors(Enum):
    RIGHT = 'index_row, index_cell + temp_index'
    DOWN = 'index_row + temp_index, index_cell'
    DOWN_RIGHT = 'index_row + temp_index, index_cell + temp_index'
    DOWN_LEFT = 'index_row + temp_index, index_cell - temp_index'


class CombBase(ABC):
    @abstractmethod
    def get_combinations(self, size_row: int,
                         size_column: int,
                         size_combination: int) -> CombsTypeT:
        """
        For the passed arguments of the two-dimensional table, \n
        it finds combinations that will be used to check the winnings for the player, or to find a move for the AI \n
        :param size_row: The number of rows of a two-dimensional table.
        :param size_column: The number of columns of a two-dimensional table.
        :param size_combination: The amount cells filled in a row for a winning result.
        :return: The array is defined in the CombsType annotation.
        """
        ...


class CombDefault(CombBase):
    @classmethod
    @lru_cache(maxsize=SIZE_CACHE_COMBINATIONS)
    def get_combinations(cls, size_row: int, size_column: int, size_combination: int) -> CombsTypeT:
        combinations = []

        for index_row in range(size_row):
            for index_column in range(size_column):
                for vector in Vectors:
                    comb = cls._get_combination_from_cell(vector=vector,
                                                          step=(index_row, index_column),
                                                          size_row=size_row,
                                                          size_column=size_column,
                                                          size_combination=size_combination)
                    if comb:
                        combinations.append(comb)

        return tuple(combinations)

    @classmethod
    def _get_combination_from_cell(cls,
                                   vector: Vectors,
                                   step: tuple[int, int],
                                   size_row: int,
                                   size_column: int,
                                   size_combination: int) -> Optional[CombTypeT]:
        index_row, index_cell = step  # args for eval
        temp_index = size_combination - 1  # arg for eval
        expected_index_row, expected_index_column = eval(vector.value)  # The last expected indices in the given vector

        # If the expected indices are within the acceptable range
        if (0 <= expected_index_row <= size_row - 1) and (0 <= expected_index_column <= size_column - 1):
            comb_vector = []

            for temp_index in range(size_combination):
                temp_index_cell: CellIndexT = eval(vector.value)
                comb_vector.append(temp_index_cell)

            return tuple(comb_vector)


def verify_combs_list(combs_list: CombsTypeT):
    try:
        for comb in combs_list:
            for cell_index in comb:
                if not (len(cell_index) == 2 and isinstance(cell_index[0], int) and isinstance(cell_index[1], int)):
                    raise ListCombinationsError(combs_list=combs_list)
    except TypeError:
        raise ListCombinationsError(combs_list=combs_list)
