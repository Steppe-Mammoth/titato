from dataclasses import dataclass

from titato.exceptions.core_exceptions import TableParamInstanceError


@dataclass(frozen=True)
class TableParam:
    ROW: int
    """The number of rows of a two-dimensional table."""
    COLUMN: int
    """The number of columns of a two-dimensional table"""
    COMBINATION: int
    """The amount cells filled in a row for a winning result"""

    def __post_init__(self):
        if self.ROW < self.COMBINATION or self.COLUMN < self.COMBINATION:
            raise ValueError("ROW and COLUMN size must not be less than COMBINATION")


def verify_table_param_instance(param: TableParam):
    if not isinstance(param, TableParam):
        raise TableParamInstanceError
