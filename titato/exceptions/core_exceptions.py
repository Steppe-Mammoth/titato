class CellAlreadyUsedError(Exception):
    def __init__(self, used_symbol: str, new_symbol: str):
        self.used_cell = used_symbol
        self.new_cell = new_symbol

    def __str__(self):
        return f"""
        THIS CELL IS USED. Cell symbol now = {self.used_cell}, you send = {self.new_cell}
        """


class AllCellsUsedError(Exception):
    def __init__(self, game_table):
        self.game_table = game_table

    def __str__(self):
        print_table = '\n'.join([str(row) for row in self.game_table])
        return f"""
        The table is completely filled, there are no free cells left
        Result:{print_table}
        """


class TableIndexError(Exception):
    def __init__(self, index_column, index_row, table_param):
        self.index_column = index_column
        self.index_row = index_row
        self.table_param = table_param

    def __str__(self):
        return f"""
        NOT ALLOWED INDEX for setting symbol in game field
        INDEX_COLUMN: You send <{self.index_column}> | Possible: MAX <{self.table_param.COLUMN - 1}> MIN <0> index.
        INDEX_ROW: You send <{self.index_row}> | Possible: MAX <{self.table_param.ROW - 1}> MIN <0> index.
        """


class TableParamInstanceError(Exception):
    def __str__(self):
        return """
        Incorrect instance of the TableParam class.
        - Create user parameter used class TableParam
        """


class TableInstanceError(Exception):
    def __str__(self):
        return """
        Incorrect instance of the Table class. 
        - Pass table instance that are descendants of the TableBase class
        """


class SymbolError(Exception):
    def __str__(self):
        return """
        Incorrect instance of the Symbol class. 
        - Pass symbol instance that are descendants of the SymbolBase class
        - Example: Symbol(name='X')
        """


class PlayersIsEmptyError(Exception):
    def __str__(self):
        return """
        The list of player is empty.
        - The list of player must be in the format: Sequence[PlayerBase] and contain at least one player
        """


class BadRoleError(Exception):
    def __str__(self):
        return """
        Incorrect player role. Pass the roles listed in the Role Enum class as an argument
        - Example: Role.User
        """


class PlayerInstanceError(Exception):
    def __str__(self):
        return """
        Incorrect instance of the Player class. 
        - Pass player instance that are descendants of the PlayerBase class
        """


class PlayersInstanceError(Exception):
    def __str__(self):
        return """
        Incorrect instance of the Players class. 
        - Pass player instance that are descendants of the PlayersBase class
        """


class CheckerError(Exception):
    def __str__(self):
        return """
        Incorrect object of the Player class. 
        - Pass checker instance or object that are descendants of the PlayerBase class
        """


class ListCombinationsError(Exception):
    combination_expected = """
    \t* Type: tuple[tuple[tuple[i_row: int, i_column: int], ...], ...]
    \t* Value: (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ... )
    """

    def __init__(self, combs_list):
        self.combs_list = combs_list

    def __str__(self):
        return f"""
        Incorrect format with combinations_list:
        Each combination in the list must match the format:
        * combs_list[i_comb][i_cell][0]: int -> is index row, and
        * combs_list[i_comb][i_cell][1]: int -> is index column.
        Your combination: {self.combs_list}
        For example, a format combination is expected: {self.combination_expected}
        """


class ResultCodeError(Exception):
    def __str__(self):
        return """
        Incorrect Result code. Use only the attributes listed in the Enum ResultCode class.
        - Example: ResultCode.WINNER / ResultCode.ALL_CELLS_USED
        """