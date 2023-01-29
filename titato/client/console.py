import sys
from abc import ABC, abstractmethod

from prettytable import PrettyTable

from titato.core.game.ai import AIDefault, AIBase
from titato.core.game.game_xo import Game
from titato.core.game.result import ResultCode, GameStateT_co, GameState, GameStateBase
from titato.core.player.player import PlayerBase

from titato.core.player.players import PlayersBase
from titato.core.table.annotations import CellIndexT
from titato.core.table.table import TableBase
from titato.exceptions.core_exceptions import CellAlreadyUsedError, TableIndexError


class GameConsoleBase(Game, ABC):
    def __init__(self, players: PlayersBase, table: TableBase, game_state: GameStateT_co, ai: AIBase):
        super().__init__(players=players, table=table, game_state=game_state)
        self.ai = ai

    @abstractmethod
    def get_step(self, player: PlayerBase) -> CellIndexT:
        """
        A function to determine the player step\n
        * For a player with a role.user requests a move in the console
        * For a player with role.android, the move is calculated automatically
        Returns the step index.
        """
        ...

    @abstractmethod
    def start_game(self) -> GameStateT_co:
        """
        Starts a loop that ends when the game ends \n
        * For a player with a role.user requests a move in the console
        * For a player with a role.android, the move is calculated automatically
        * Prints the game table after each turn \n
        Returns the final result of the game.
        """
        ...

    @abstractmethod
    def print_table(self):
        ...


class GameConsole(GameConsoleBase):
    def __init__(self, players: PlayersBase,
                 table: TableBase,
                 game_state: GameStateT_co = GameState(),
                 ai: AIBase = AIDefault(), ):

        super().__init__(players=players, table=table, game_state=game_state, ai=ai)

    @classmethod
    def _print_step_info(cls, player: PlayerBase, index_row: int, index_column: int):
        print(f'Step taken: {player.name} <{player.symbol.name}> | ↓: {index_row} | →: {index_column} |')

    @classmethod
    def _print_info_player(cls, player: PlayerBase):
        p = player
        role = 'ANDROID' if p.is_android else 'USER'
        print(f'Player: {p.name} < {p.symbol.name} > | Role: {role} | Count steps: {p.count_steps}')

    @classmethod
    def print_result(cls, result: GameStateBase):
        text = None

        match result.code:
            case ResultCode.WINNER:
                player = result.win_player
                text = f"WIN: {player.name} < {player.symbol.name} > | COMB: < {result.win_combination} >"

            case ResultCode.ALL_CELLS_USED:
                text = "PEACE: ALL USED CELLS"
        print(text)

    def print_table(self):
        table = PrettyTable()

        table.field_names = ['↓/→'] + [str(i_column) for i_column in range(self.table.param.COLUMN)]
        for i_row, row in enumerate(self.table.game_field):
            cells_symbols = [cell.symbol.name if cell is not None else "*" for cell in row]
            table.add_row([f"{i_row}:"] + cells_symbols)

        print(table)

    def get_step(self, player: PlayerBase) -> CellIndexT:
        if player.is_android:
            step = self.ai_get_step(player=player)
        else:
            step = self._get_step_for_user()
        return step

    def _get_step_for_user(self) -> tuple[int]:
        step = None
        while step is None:
            try:
                step = self._input_step_player()
            except ValueError:  # make exception
                print("ERROR: Non correct format: Please again\n"
                      "* Enter 2 integer: First for row ↓ index; Second for column → index")
        return step

    @classmethod
    def _input_step_player(cls) -> tuple[int]:
        res = input("ENTER STEP : < ↓ > < → >: ")
        if res == 'exit':
            sys.exit()

        step = tuple(map(int, res.split()))
        if len(step) != 2:
            raise ValueError
        return step

    def start_game(self) -> GameStateT_co:
        print(f'Start Game\n'
              f'[Info: Expected two integers - e.g: < 0 2 > / Enter < exit > to quit]')

        while self.game_state.code is ResultCode.NO_RESULT:
            result = i_row = i_column = None
            p_now = self.players.current_player

            self.print_table()
            self._print_info_player(player=p_now)

            while result is None:
                i_row, i_column = self.get_step(player=p_now)
                try:
                    result = self.step_result(index_row=i_row, index_column=i_column, player=p_now)
                except CellAlreadyUsedError:
                    print("ERROR: This cell is used. Select another cell")
                except TableIndexError:
                    print("ERROR: This cell is not available, Select another cell")

            self._print_step_info(player=p_now, index_row=i_row, index_column=i_column)
            self.print_result(result)

            if result.code is ResultCode.NO_RESULT:
                self.players.set_get_next_player()

        self.print_table()
        return self.game_state
