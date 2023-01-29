# titato
___Library of the game tic-tac-toe + AI.___ _Experimental functionality with dynamic parameters of the game field_

___

## Main advantages:
+ **Unlimited number of players in one game**
+ **Creating a playing field of any size**:
+ + *With size parameters required: **row**, **column** and **winning combination***
+ **Artificial Intelligence algorithm works with any game settings**

___

  
```python
# Visualization of dynamic settings of the playing field
                                                                               10 x 10  player vs player vs player
                                                                        +-----+---+---+---+---+---+---+---+---+---+---+
                                   6 x 6  player vs player              | ↓/→ | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
                               +-----+---+---+---+---+---+---+          +-----+---+---+---+---+---+---+---+---+---+---+
 3 x 3 player vs player        | ↓/→ | 0 | 1 | 2 | 3 | 4 | 5 |          |  0: | * | * | * | * | * | * | * | * | * | * |
   +-----+---+---+---+         +-----+---+---+---+---+---+---+          |  1: | X | * | * | * | * | * | * | O | * | * |
   | ↓/→ | 0 | 1 | 2 |         |  0: | * | * | * | * | X | * |          |  2: | * | X | * | * | * | * | O | * | * | * |
   +-----+---+---+---+         |  1: | * | * | * | * | O | * |          |  3: | * | * | P | * | * | P | * | * | * | * |
   |  0: | O | * | X |         |  2: | * | * | * | * | O | * |          |  4: | * | * | * | X | O | * | * | * | * | * |
   |  1: | * | O | * |         |  3: | X | X | X | X | O | X |          |  5: | * | * | * | O | X | * | * | * | * | * |
   |  2: | X | * | O |         |  4: | * | * | * | * | O | * |          |  6: | * | * | O | * | * | X | * | * | * | * |
   +-----+---+---+---+         |  5: | * | * | * | * | O | * |          |  7: | * | O | * | * | * | * | X | * | O | * |
                               +-----+---+---+---+---+---+---+          |  8: | O | * | * | * | * | * | * | * | * | * |
                                                                        |  9: | * | * | X | P | P | P | P | O | P | P |
                                                                        +-----+---+---+---+---+---+---+---+---+---+---+
```


___
___


## ***Documentation***

[*Start a quick game in the console*](https://github.com/Steppe-Mammoth/titato#start-a-quick-game-in-the-console-gameconsole)

[**API:**](https://github.com/Steppe-Mammoth/titato#api) 
* [Game](https://github.com/Steppe-Mammoth/titato#game) 
* [Table](https://github.com/Steppe-Mammoth/titato#table) 
* [Players](https://github.com/Steppe-Mammoth/titato#players) 
* [Player](https://github.com/Steppe-Mammoth/titato#player) 
* [Game State](https://github.com/Steppe-Mammoth/titato#game-state) 
* [AI](https://github.com/Steppe-Mammoth/titato#ai) 

[*Translations into other languages:*](https://github.com/Steppe-Mammoth/titato#translations-into-other-languages)

___

## Introduction to the library:

### *Start a quick game in the console `GameConsole`*
*Demo game in console*

<details>
 <summary> 🤖 Expand </summary>

_We can set any size for the game table, and many players for the game_
- _AI and the list of winning combinations for players are adjusted automatically_

_We will use this. **Instead of the classic 3×3 table — let's create 7×7, and 3 players**
Let the bots play with each other this time. Let's look at it._

```python
from titato.client import GameConsole
from titato.core.player import Player, Players, Symbol
from titato.core.table import Table, TableParam


if __name__ == "__main__":
    p1 = Player(name="PETROS_ANDROID:1", symbol=Symbol('X'), role=Player.Role.ANDROID)
    p2 = Player(name="AMIGOS_ANDROID:2", symbol=Symbol('O'), role=Player.Role.ANDROID)
    p3 = Player(name="GENTOS_ANDROID:3", symbol=Symbol('K'), role=Player.Role.ANDROID)

    # p4 = Player(name="PLAYER", symbol=Symbol('P'), role=Player.Role.USER)

    players = Players(players=[p1, p2, p3])
    table = Table(param=TableParam(ROW=7, COLUMN=7, COMBINATION=5))

    game = GameConsole(players=players, table=table)
    game.start_game()
```

<details>
  <summary>Attempt #1</summary>
  
```python
WIN: PETROS_ANDROID:1 < X > | COMB: < ((1, 1), (2, 2), (3, 3), (4, 4), (5, 5)) >
+-----+---+---+---+---+---+---+---+
| ↓/→ | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
+-----+---+---+---+---+---+---+---+
|  0: | O | * | * | * | K | X | K |
|  1: | K | X | * | * | O | * | X |
|  2: | X | K | X | O | K | O | X |
|  3: | K | O | K | X | X | K | O |
|  4: | K | O | X | X | X | O | X |
|  5: | O | O | K | O | O | X | X |
|  6: | * | * | O | K | * | K | K |
+-----+---+---+---+---+---+---+---+
```
</details>

<details>
  <summary>Attempt #2</summary>
  
```python
PEACE: ALL USED CELLS
+-----+---+---+---+---+---+---+---+
| ↓/→ | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
+-----+---+---+---+---+---+---+---+
|  0: | X | K | K | O | O | O | X |
|  1: | K | X | X | K | X | O | K |
|  2: | X | K | O | O | O | X | K |
|  3: | O | X | K | K | O | K | X |
|  4: | X | O | K | O | O | X | O |
|  5: | X | X | O | X | X | K | K |
|  6: | K | K | X | O | K | O | X |
+-----+---+---+---+---+---+---+---+
```
</details>

<details>
  <summary>Attempt #3</summary>
  
```python
WIN: AMIGOS_ANDROID:2 < O > | COMB: < ((3, 1), (3, 2), (3, 3), (3, 4), (3, 5)) >
+-----+---+---+---+---+---+---+---+
| ↓/→ | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
+-----+---+---+---+---+---+---+---+
|  0: | * | * | * | * | K | * | * |
|  1: | * | * | * | * | K | * | * |
|  2: | * | X | * | * | * | * | * |
|  3: | * | O | O | O | O | O | X |
|  4: | * | * | * | * | K | * | * |
|  5: | * | * | * | * | * | * | * |
|  6: | K | X | X | X | O | X | K |
+-----+---+---+---+---+---+---+---+
```
</details>


<details>
  <summary> * Brief description of GameConsole </summary> 

The `.start_game` method activates a while a loop with an exit condition,
if the game will be logically finished (There is a win / All cells are occupied == `game_console.game_state.is_finished`)

* For queued players that return True for the `player.is_android` method, automatic cell search is applied, 
players who return True for `player.is_user` will be prompted to enter indexes in the console

</details>




__If you want to load the processor with a hundred bots in a 1000×1000 field — no one will interfere!__

_Let's go further._

</details>

___


## API:
    
```python
from titato.core.game import Game
from titato.core.player import Player, Players, Symbol
from titato.core.table import Table, TableParam

p1 = Player(name="VERA_ANDROID", symbol=Symbol('X'), role=Player.Role.ANDROID)
p2 = Player(name="BOGDAN_PLAYER", symbol=Symbol('O'), role=Player.Role.USER)

players = Players(players=[p1, p2])
table = TableDefault(param=TableParam(ROW=3, COLUMN=3, COMBINATION=3))

game = Game(players=players, table=table)
```
+ ___These variables will be used when describing the methods___

___

### GAME 
___Main.___ _The process of the game, the processing of moves, the issuing of the result._


<details>
  <summary>📂 Expand </summary> 

___

#### - Take a step. `game.step`:
```python
def step(self, index_row: int, index_column: int, player: PlayerBase)
```
```python
# input
game.step(index_row=1, index_column=0, player=p2)  
game.step(index_row=1, index_column=2, player=p2)  
game.step(index_row=1, index_column=1, player=p2) 
```
```python
# output
+-----+---+---+---+   ->   +-----+---+---+---+   ->   +-----+---+---+---+  
| ↓/→ | 0 | 1 | 2 |   ->   | ↓/→ | 0 | 1 | 2 |   ->   | ↓/→ | 0 | 1 | 2 |
+-----+---+---+---+   ->   +-----+---+---+---+   ->   +-----+---+---+---+
|  0: | * | * | * |   ->   |  0: | * | * | * |   ->   |  0: | * | * | * |
|  1: | O | * | * |   ->   |  1: | O | * | O |   ->   |  1: | O | O | O |
|  2: | * | * | * |   ->   |  2: | * | * | * |   ->   |  2: | * | * | * |
+-----+---+---+---+   ->   +-----+---+---+---+   ->   +-----+---+---+---+
```

The function sets the player symbol `player.symbol` in the cell at the specified indices.
After successful installation, the `player.count_steps` counter is incremented by +1,
and `game.table.count_free_cells` is decreased by -1

Note:
* _If the transferred indexes do not match the possible ones in the table — an error_ `TableIndexError`
* _If you try to set a new symbol on an already occupied cell — error_ `CellAlreadyUsedError`
___

#### - Get the result. `game.result`:

```python
def result(self, player: PlayerBase) -> GameStateT
```
_Let's check the result of our previous 3 steps (in the block above), we expect winnings_

```python
# input
res = game.result(player=p2)
    
match res.code:
    case ResultCode.NO_RESULT:
        print('STATUS: NO RESULT')
    case ResultCode.WINNER:
        print(f'STATUS: WINNER. Player: {res.win_player.name}, Win comb: {res.win_combination}')
    case ResultCode.ALL_CELLS_USED:
        print('STATUS: DRAW')
``` 
```python   
# output
STATUS: WINNER. Player: BOGDAN_PLAYER, Win comb: ((1, 0), (1, 1), (1, 2))
```

For a given player, the function performs 2 checks:
* _Check for winnings. Compares player moves with winning combinations `game.table.combinations`_
* _Checking for a tie. Checks with free cell count `game.table.count_free_cells`_
  
When one of the two probabilities is valid, the `game.set_winner` or `game.set_draw` method is automatically called  
After checks and possible modifications — returns the object: `game.game_state`


Note:
* `assert res == game.game_state # True`
* _To check that one of the triggers that logically ends the game worked — call the game_state method: `.is_finished`,
if True — you have a win or a draw. You can also use `.is_winner` or `.is_draw`.  
For more details, see GameState section_

___

#### - Take a step and return the result. `game.step_result`:

```python
def step_result(self, index_row: int, index_column: int, player: PlayerBase) -> GameStateT
```
* **Unifying function**. _Replaces the successive call of `game.step` and `game.result`,
returns the result_

---

#### - AI. Get the index of the best cell for the player. `game.ai_get_step`:

```python
def ai_get_step(self, player: PlayerBase) -> CellIndex
```

AI returns a tuple with the two indices (`index_row: int, index_column: int`) of the cell
    
* _For more details, see AI section_

---

#### - AI. Make a move for a player. `game.ai_step`:

```python
def ai_step(self, player: PlayerBase)
```
* **Unifying function**. _Replaces the successive call of  `game.ai_get_step` and `game.step`_

---

#### - AI. Make a move for the player and return the result. `game.ai_step_result`:

```python
def ai_step_result(self, player: PlayerBase) -> GameStateT
```
* **Unifying function**. _Replaces the successive call of  `game.ai_get_step` and `game.step_result`,
returns the result_

___

#### - Set the winner. `game.set_winner`:

```python
def set_winner(self, player: PlayerBase, win_combination)
```

Updates the game result in the `game.game_state` object, replacing `game.game_state.code` with
`ResultCode.WINNER`, and
adds the winning result to the `game.game_state.win_player` and `game.game_state.win_combination` fields

Note:

* _This method is automatically called in the `game.result` method if the win trigger fires_
* _The result is updated via the `game.game_result.update` method_

___

#### - Set a draw `game.set_draw`:

```python
def set_draw(self)
```

Updates the game result in the `game.game_state`, object, replacing `game.game_state.code`
with `ResultCode.ALL_CELLS_USED` 

Note:

* _This method is automatically called in the `game.result` method if a draw trigger fires_
* _The result is updated via the `game.game_result.update` method_



</details>


___

___


### TABLE
_Sets moves, combinations for the game board_

<details>
  <summary>📂 Expand </summary> 

```python
table = game.table
```

___
#### - Get a playing field. `table.game_field`:

```python
@property
def game_field(self) -> GameFieldType
 ```  
Returns a 2D list of the playing field

Note:
+ _It is also available in: `game.game_field`_

___
#### - Get a list of winning combinations. `table.combinations`:    

```python
@property
def combinations(self) -> CombsType
```  

Returns a list of all winning combinations for this table
* _Combinations are created automatically according to the parameters of the table,
or manually passed to the constructor of the Table class instance_

___

#### - Get the number of free cells. `table.count_free_cells`:   

```python
@property
def count_free_cells(self) -> int
```  
Returns the number of free cells in the game filed

___

#### - Set the symbol in the cell. `table.set_symbol_cell`:   

```python
@property
def set_symbol_cell(self, index_row: int, index_column: int, symbol: SymbolBase)
``` 

Sets the passed character at the specified indices of the playing field.
Decreases the number of free cells by -1
    
Note:
* _It is this method that is automatically called in `game.step`_
    
</details>  

___
___



### PLAYERS
 
_List of players and queue_ 
   
<details>
  <summary>📂 Expand </summary> 
  

```python
players = game.players
```  
___

#### - Get a list of players. `players.player_list`:   

```python
@property
def players_list(self) -> list[PlayerT]:
```  

Returns a list of all players

Note:
* _This list changes after using the `players.shuffle_players` method_
    
___


#### - Get the current player. `players.current_player`:   

```python
@property
def current_player(self) -> PlayerT
```  

Returns the current player from the queue
    
___

#### - Set and get the next player. `players.set_get_next_player`:        

```python
def set_get_next_player(self) -> PlayerT
```  

Replaces the current player with the next player in the queue and returns it

Note:
* _After that, this player is available in the `players.current_player' method_
    
___

#### - Shuffle the players list. `players.shuffle_players`:        
```python
def shuffle_players(self)
```  
Shuffles the player list and replaces the current queue with a new one.
    
Note:
* _The first player from the new queue will be set as the current one, and is available in `players.current_player`_
</details>  

___

___


### PLAYER

_The player, his date_

<details>
  <summary>📂 Expand </summary> 

```python
# titato.core.player.player.py

class Role(Enum):
    USER = 1
    ANDROID = 2
```  
```python
player = game.current_player
```  
___

#### - Get a role.. `player.role`:   
```python
@property
def role(self) -> Role
```
___

#### - Get a symbol. `player.symbol`:   
```python
@property
def symbol(self) -> SymbolBase
```  
Returns an object of class Symbol of the player

___

#### - Get the player step count `player.count_steps`:   
```python
@property
def count_steps(self) -> int
```  
Returns the number of steps taken by the player

___

#### - Is this an android? `player.is_android`:   
```python
@property
def is_android(self) -> bool
```  
Returns True if the player has role `Role.ANDROID`
Otherwise — False

___

#### - Is this a user? `player.is_user`:  
```python
@property
def is_user(self) -> bool
```  
Returns True if the player has role `Role.USER`  
Otherwise — False

___

#### - Add step for player. `player.add_count_step`:  
```python
def add_count_step(self)
```  

Adds +1 to the player's step counter

Note:
* This method is automatically called in `table.set_symbol_cell`


</details>  

___
___


### GAME STATE

Current game information

<details>
  <summary>📂 Expand </summary> 

```python
# titato.core.game.result.py

class ResultCode(Enum):
    NO_RESULT = 0
    ALL_CELLS_USED = 1
    WINNER = 2
```  

```python
game_state = game.game_state
```  

___

#### - Get game status code. `game_result.code`:   
```python
@property
def code(self) -> ResultCode
```  

Returns the status code of the game

Note:

* _The initial value is set to `Result Code.NO_RESULT`_

___


#### - Get the winning player. `game_result.win_player`:   
```python
@property
def win_player(self) -> Optional[PlayerBase]
```

Returns the winning player if it was added by the `game_result.update` method

___


#### - Get a winning combination. `game_result.win_combination`:   
```python
@property
def win_combination(self) -> Optional[CombType]
```  

Returns the winning combination if it was added by the `game_result.update` method

___


#### - Game is over? `game_result.is_finished`:   
```python
@property
def is_finished(self) -> bool
```  

Returns True if `game_result.code` is `ResultCode.ALL_CELLS_USED` or `ResultCode.WINNER`  
Otherwise — False

___


#### - Is the game still on? `game_result.is_continues`:   
```python
@property
def is_continues(self) -> bool
```  
Returns True if `game_result.code` is `ResultCode.NO_RESULT`  
Otherwise — False

___


#### - Is there a win? `game_result.is_winner`:   
```python
@property
def is_winner(self) -> bool
```  
Returns True if `game_result.code` is `ResultCode.WINNER`  
Otherwise — False

___


#### - Is there a draw? `game_result.is_draw`:   
```python
@property
def is_draw(self) -> bool
```  
Returns True if `game_result.code` is `ResultCode.ALL_CELLS_USED`  
Otherwise — False

___


#### - Update result. `game_result.update`:   
```python
def update(self,
           code: Optional[ResultCode] = None,
           win_player: Optional[PlayerBase] = None,
           win_combination: Optional[CombType] = None)
```  
Updates data about the current game result.

Note:

* _`game_result.code` - automatically updated when the `game.set_draw` or `game.set_winner` method is used_
* _`game_result.win_player` and `game_result.win_combination` -  
automatically updated when the `game.set_winner` method is used_  
For more details, see section Game, methods: `game.set_draw` and `game.set_winner`

</details>

___
___


### AI

A short work example:

<details>
  <summary> 📂 Expand </summary> 

```python
p1 = Player(name="PLAYER", symbol=Symbol('X'))
p2 = Player(name="ANDROID", symbol=Symbol('O'))
...
```
```python
game.step(2, 2, player=p1)
game.step(0, 0, player=p1)

game.ai_step(p2)  # result in second table

+-----+---+---+---+   ->   +-----+---+---+---+
| ↓/→ | 0 | 1 | 2 |   ->   | ↓/→ | 0 | 1 | 2 |
+-----+---+---+---+   ->   +-----+---+---+---+
|  0: | X | * | * |   ->   |  0: | X | * | * |
|  1: | * | * | * |   ->   |  1: | * | O | * |
|  2: | * | * | X |   ->   |  2: | * | * | X |
+-----+---+---+---+   ->   +-----+---+---+---+
```
* The AI algorithm understands that the opponent's next move is likely to collect a winning combination, so it blocks it

Let's consider the second situation

```python
game.step(0, 0, player=p1)  # X
game.step(2, 0, player=p1)  # X

game.step(0, 2, player=p2)  # O
game.step(2, 2, player=p2)  # O

game.ai_step(p2)  # result in second table

+-----+---+---+---+   ->   +-----+---+---+---+
| ↓/→ | 0 | 1 | 2 |   ->   | ↓/→ | 0 | 1 | 2 |
+-----+---+---+---+   ->   +-----+---+---+---+
|  0: | X | * | O |   ->   |  0: | X | * | O |
|  1: | * | * | * |   ->   |  1: | * | * | O |
|  2: | X | * | O |   ->   |  2: | X | * | O |
+-----+---+---+---+   ->   +-----+---+---+---+
```
* The AI algorithm prioritizes its own winnings,
with the understanding that there will be no next winning move for the opponent
___
</details>


___
___


## Translations into other languages:


<details>
 <summary>UA 🇺🇦</summary>

___

## Знайомство з бібліотекою

### Старт швидкої гри в консолі. `GameConsole`
Демо гра в консолі

<details>
 <summary> 🤖 Розгорнути </summary>

_Ми можемо задати будь-який розмір для ігрової таблиці та безліч гравців для гри_ 
- _AI й перелік виграшних комбінацій для гравців підлаштуються автоматично_

_Скористаємося цим. **Замість класичної таблиці 3х3 - створимо 7х7, та 3 гравці**  
Цього разу боти хай грають один з одним. Поглянемо на це_

```python
from titato.client import GameConsole
from titato.core.player import Player, Players, Symbol
from titato.core.table import Table, TableParam


if __name__ == "__main__":
    p1 = Player(name="PETROS_ANDROID:1", symbol=Symbol('X'), role=Player.Role.ANDROID)
    p2 = Player(name="AMIGOS_ANDROID:2", symbol=Symbol('O'), role=Player.Role.ANDROID)
    p3 = Player(name="GENTOS_ANDROID:3", symbol=Symbol('K'), role=Player.Role.ANDROID)

    # p4 = Player(name="PLAYER", symbol=Symbol('P'), role=Player.Role.USER)

    players = Players(players=[p1, p2, p3])
    table = Table(param=TableParam(ROW=7, COLUMN=7, COMBINATION=5))

    game = GameConsole(players=players, table=table)
    game.start_game()
```

<details>
  <summary>Спроба №1</summary>
  
```python
WIN: PETROS_ANDROID:1 < X > | COMB: < ((1, 1), (2, 2), (3, 3), (4, 4), (5, 5)) >
+-----+---+---+---+---+---+---+---+
| ↓/→ | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
+-----+---+---+---+---+---+---+---+
|  0: | O | * | * | * | K | X | K |
|  1: | K | X | * | * | O | * | X |
|  2: | X | K | X | O | K | O | X |
|  3: | K | O | K | X | X | K | O |
|  4: | K | O | X | X | X | O | X |
|  5: | O | O | K | O | O | X | X |
|  6: | * | * | O | K | * | K | K |
+-----+---+---+---+---+---+---+---+
```
</details>

<details>
  <summary>Спроба №2</summary>
  
```python
PEACE: ALL USED CELLS
+-----+---+---+---+---+---+---+---+
| ↓/→ | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
+-----+---+---+---+---+---+---+---+
|  0: | X | K | K | O | O | O | X |
|  1: | K | X | X | K | X | O | K |
|  2: | X | K | O | O | O | X | K |
|  3: | O | X | K | K | O | K | X |
|  4: | X | O | K | O | O | X | O |
|  5: | X | X | O | X | X | K | K |
|  6: | K | K | X | O | K | O | X |
+-----+---+---+---+---+---+---+---+
```
</details>

<details>
  <summary>Спроба №3</summary>
  
```python
WIN: AMIGOS_ANDROID:2 < O > | COMB: < ((3, 1), (3, 2), (3, 3), (3, 4), (3, 5)) >
+-----+---+---+---+---+---+---+---+
| ↓/→ | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
+-----+---+---+---+---+---+---+---+
|  0: | * | * | * | * | K | * | * |
|  1: | * | * | * | * | K | * | * |
|  2: | * | X | * | * | * | * | * |
|  3: | * | O | O | O | O | O | X |
|  4: | * | * | * | * | K | * | * |
|  5: | * | * | * | * | * | * | * |
|  6: | K | X | X | X | O | X | K |
+-----+---+---+---+---+---+---+---+
```
</details>



<details>
  <summary> * Короткий опис  GameConsole</summary> 

Метод `.start_game` активує цикл while з умовою виходу,
якщо гра буде логічно закінчено (Є виграш / Всі клітинки зайняті == `game_console.game_state.is_finished`)

* Для гравців в черзі, які повертають True для методу `player.is_android` застосовуються автоматичний пошук клітинки, 
а для гравців які повернуть True для `player.is_user` буде запропоновано ввести індекси в консолі

</details>


__Як захочете нагрузити процесор сотнею ботів в 1000х1000 полі — ніхто не завадить!__
_Підемо далі_

</details>

___
___

## API:

    
```python
from titato.core.game import Game
from titato.core.player import Player, Players, Symbol
from titato.core.table import Table, TableParam

p1 = Player(name="VERA_ANDROID", symbol=Symbol('X'), role=Player.Role.ANDROID)
p2 = Player(name="BOGDAN_PLAYER", symbol=Symbol('O'), role=Player.Role.USER)

players = Players(players=[p1, p2])
table = TableDefault(param=TableParam(ROW=3, COLUMN=3, COMBINATION=3))

game = Game(players=players, table=table)
```
+ ___Ці змінні будуть використовуватись при описі методів___

___

### GAME 
___Головний.___ _Процес гри, обробка ходів, видача результату._


<details>
  <summary>📂 Розгорнути</summary> 

___

#### - Зробити крок. `game.step`:
```python
def step(self, index_row: int, index_column: int, player: PlayerBase)
```
```python
# input
game.step(index_row=1, index_column=0, player=p2)  
game.step(index_row=1, index_column=2, player=p2)  
game.step(index_row=1, index_column=1, player=p2) 
```
```python
# output
+-----+---+---+---+   ->   +-----+---+---+---+   ->   +-----+---+---+---+  
| ↓/→ | 0 | 1 | 2 |   ->   | ↓/→ | 0 | 1 | 2 |   ->   | ↓/→ | 0 | 1 | 2 |
+-----+---+---+---+   ->   +-----+---+---+---+   ->   +-----+---+---+---+
|  0: | * | * | * |   ->   |  0: | * | * | * |   ->   |  0: | * | * | * |
|  1: | O | * | * |   ->   |  1: | O | * | O |   ->   |  1: | O | O | O |
|  2: | * | * | * |   ->   |  2: | * | * | * |   ->   |  2: | * | * | * |
+-----+---+---+---+   ->   +-----+---+---+---+   ->   +-----+---+---+---+
```
Функція встановлює символ гравця `player.symbol` в клітинку за вказаними індексами.  
Після успішного встановлення лічильник `player.count_steps` збільшується на +1,
а `game.table.count_free_cells` зменшується на -1

Примітка:
* _Якщо передані індекси не збігаються з можливими в таблиці - помилка_ `TableIndexError`
* _Якщо ви намагаєтесь встановити новий символ на вже зайняту клітинку - помилка_ `CellAlreadyUsedError`

___

#### - Отримати результат. `game.result`:

```python
def result(self, player: PlayerBase) -> GameStateT
```
_Перевіримо результат наших попередніх 3-ох кроків (в блоці вище), очікуємо виграш_
```python
# input
res = game.result(player=p2)
    
match res.code:
    case ResultCode.NO_RESULT:
        print('STATUS: NO RESULT')
    case ResultCode.WINNER:
        print(f'STATUS: WINNER. Player: {res.win_player.name}, Win comb: {res.win_combination}')
    case ResultCode.ALL_CELLS_USED:
        print('STATUS: DRAW')
``` 
```python   
# output
STATUS: WINNER. Player: BOGDAN_PLAYER, Win comb: ((1, 0), (1, 1), (1, 2))
```
Для заданого гравця функція проводить 2 перевірки:
* _Пошуку виграшу. Звіряється з виграшними комбінаціями `game.table.combinations`_
* _Перевірка на нічию. Звіряється з показником вільних клітинок `game.table.count_free_cells`_
  
Коли одна з двох вірогідностей дійсна, автоматично викликається метод `game.set_winner` або `game.set_draw`
Після перевірок та можливих модифікацій — повертає об'єкт: `game.game_state`

Примітка: 
* `assert res == game.game_state  # True`
* _Щоб перевірити що одна з тригерів які логічно завершує гру спрацювала — викликаємо в game_state метод: `.is_finished`,
якщо True - в нас є виграш або нічия. Також можете використати `.is_winner` або `.is_draw`.  
Детальніше див. розділ GameState_

___

#### - Зробити крок і повернути результат. `game.step_result`:

```python
def step_result(self, index_row: int, index_column: int, player: PlayerBase) -> GameStateT
```
* **Об'єднувальний метод**. _Заміняє почерговий виклик  `game.step` і `game.result`, повертає результат останнього_

---

#### - AI. Отримати індекс найкращої клітинки для гравця. `game.ai_get_step`:

```python
def ai_get_step(self, player: PlayerBase) -> CellIndex
```
AI повертає кортеж з двома індексами (`index_row: int, index_column: int`) клітинки
    
* _Детальніше див. розділ AI_

---

#### - AI. Зробити хід для гравця. `game.ai_step`:

```python
def ai_step(self, player: PlayerBase)
```
* **Об'єднувальний метод**. _Заміняє почерговий виклик.  `game.ai_get_step` і `game.step`_

---

#### - AI. Зробити хід для гравця і повернути результат. `game.ai_step_result`:

```python
def ai_step_result(self, player: PlayerBase) -> GameStateT
```
* **Об'єднувальний метод**. _Заміняє почерговий виклик  `game.ai_get_step` і `game.step_result`,
повертає результат останнього_
   

___

#### - Встановити переможця. `game.set_winner`:

```python
def set_winner(self, player: PlayerBase, win_combination)
```

Оновлює результат гри в об'єкті `game.game_state`, замінюючи  `game.game_state.code` на `ResultCode.WINNER`, і
додає результат виграшу в поля `game.game_state.win_player` і `game.game_state.win_combination` 

Примітка:

* _Цей метод автоматично викликається в роботі методу `game.result`, якщо спрацьовує тригер перемоги_
* _Оновлення результату виконується через метод `game.game_result.update`_
 
___

#### - Встановити нічию. `game.set_draw`:

```python
def set_draw(self)
```

Оновлює результат гри в об'єкті `game.game_state`, замінюючи `game.game_state.code` на `ResultCode.ALL_CELLS_USED`,  

Примітка:

* _Цей метод автоматично викликається в роботі методу `game.result`, якщо спрацьовує тригер нічиєї_
* _Оновлення результату виконується через метод `game.game_result.update`_

  
  
</details>


___
___


### TABLE
_Виставляння ходів, комбінації для таблиці_

<details>
  <summary>📂 Розгорнути</summary> 

```python
table = game.table
```

___
#### - Отримати ігрове поле. `table.game_field`:

```python
@property
def game_field(self) -> GameFieldType
 ```  
Повертає двовимірний список ігрового поля 

Примітка:
+ _Також доступний в `game.game_field`_

___
#### - Отримати список виграшних комбінацій. `table.combinations`:    

```python
@property
def combinations(self) -> CombsType
```  
Повертає список всіх виграшних комбінацій для цієї таблиці
* _Комбінації створюються автоматично за параметрами таблиці,
або передаються вручну в конструктор екземпляра класу Table_

___

#### - Отримати кількість вільних клітинок. `table.count_free_cells`:   

```python
@property
def count_free_cells(self) -> int
```  
Повертає кількість вільних клітинок в таблиці

___

#### - Встановити символ в клітку. `table.set_symbol_cell`:   

```python
@property
def set_symbol_cell(self, index_row: int, index_column: int, symbol: SymbolBase)
``` 
Встановлює переданий символ за вказаними індексами ігрового поля.  
Зменшує рахунок вільних клітинок на -1  
    
Примітка:
* _Цей метод автоматично викликається в `game.step`_
    
</details>  

___
___

### PLAYERS
 
_Список гравців і черга_ 
   
<details>
  <summary>📂 Розгорнути</summary> 
  

```python
players = game.players
```  
___

#### - Отримати список гравців. `players.player_list`:   

```python
@property
def players_list(self) -> list[PlayerT]:
```  
Повертає список всіх гравців  

Примітка:
* _Цей список змінюється після застосування методу `players.shuffle_players`_
    
___


#### - Отримати поточного гравця. `players.current_player`:   

```python
@property
def current_player(self) -> PlayerT
```  
Повертає поточного гравця з черги
    
___

#### - Встановити й отримати наступного гравця. `players.set_get_next_player`:        

```python
def set_get_next_player(self) -> PlayerT
```  
Заміняє поточного гравця на наступного з черги й повертає його

Примітка:
* _Після цього цей гравець доступний в методі `players.current_player`_
    
___

#### - Перемішати список гравців. `players.shuffle_players`:        
```python
def shuffle_players(self)
```  
Перемішує список гравців й заміняє чинну чергу на нову.  
    
Примітка:
* _Перший гравець з нової черги буде встановлений як теперішній, і доступний в `players.current_player`_

</details>  

___

___
### PLAYER

_Гравець, його данні_

<details>
  <summary>📂 Розгорнути</summary> 

```python
# titato.core.player.player.py

class Role(Enum):
    USER = 1
    ANDROID = 2
```  
```python
player = game.current_player
```  
___

#### - Отримати роль. `player.role`:   
```python
@property
def role(self) -> Role
```  
Повертає роль гравця

___

#### - Отримати символ. `player.symbol`:   
```python
@property
def symbol(self) -> SymbolBase
```  
Повертає об'єкт класу Symbol гравця

___

#### - Отримати кількість кроків гравця. `player.count_steps`:   
```python
@property
def count_steps(self) -> int
```  
Повертає кількість зроблених кроків гравця

___

#### - Це андроїд? `player.is_android`:   
```python
@property
def is_android(self) -> bool
```  
Повертає True якщо гравець з роллю `Role.ANDROID`  
Інакше - False

___

#### - Це юзер? `player.is_user`:  
```python
@property
def is_user(self) -> bool
```  
Повертає True якщо гравець з роллю `Role.USER`  
Інакше - False

___

#### - Додати крок для гравця. `player.add_count_step`:  
```python
def add_count_step(self)
```  
Додає +1 до лічильника кроків гравця  

Примітка:
* Цей метод автоматично викликається в `table.set_symbol_cell`


</details>  

___
___

### GAME STATE

Поточний результат гри

<details>
  <summary>📂 Розгорнути </summary> 

```python
# titato.core.game.result.py

class ResultCode(Enum):
    NO_RESULT = 0
    ALL_CELLS_USED = 1
    WINNER = 2
```  

```python
game_state = game.game_state
```  

___

#### - Отримати код гри. `game_result.code`:   
```python
@property
def code(self) -> ResultCode
```  
Повертає статус код гри:

Примітка:

* _Початкове значення встановлене як `ResultCode.NO_RESULT`_

___


#### - Отримати виграшного гравця. `game_result.win_player`:   
```python
@property
def win_player(self) -> Optional[PlayerBase]
```
Повертає виграшного гравця, якщо він був доданий методом `game_result.update`

___


#### - Отримати виграшну комбінацію. `game_result.win_combination`:   
```python
@property
def win_combination(self) -> Optional[CombType]
```  
Повертає виграшну комбінацію, якщо вона була доданий методом `game_result.update`

___


#### - Гра закінчена? `game_result.is_finished`:   
```python
@property
def is_finished(self) -> bool
```  
Повертає True якщо `game_result.code` має значення `ResultCode.ALL_CELLS_USED` або `ResultCode.WINNER`  
Інакше - False

___


#### - Гра продовжується? `game_result.is_continues`:   
```python
@property
def is_continues(self) -> bool
```  
Повертає True якщо `game_result.code` має значення `ResultCode.NO_RESULT`  
Інакше - False

___


#### - Є виграш? `game_result.is_winner`:   
```python
@property
def is_winner(self) -> bool
```  
Повертає True якщо `game_result.code` має значення `ResultCode.WINNER`  
Інакше - False

___


#### - Є нічия? `game_result.is_draw`:   
```python
@property
def is_draw(self) -> bool
```  
Повертає True якщо `game_result.code` має значення `ResultCode.ALL_CELLS_USED`  
Інакше - False

___


#### - Оновити результат. `game_result.update`:   
```python
def update(self,
           code: Optional[ResultCode] = None,
           win_player: Optional[PlayerBase] = None,
           win_combination: Optional[CombType] = None)
```  
Оновлює дані про поточний результат гри.

Примітка:

* _`game_result.code` - автоматично оновлюється коли застосовується метод `game.set_draw` або `game.set_winner`_
* _`game_result.win_player` і `game_result.win_combination` -  
автоматично оновлюється коли застосовується метод `game.set_winner`_  
Детальніше див. розділ Game, методи: `game.set_draw` і `game.set_winner`

</details>

___
___

### AI

Короткий приклад роботи

<details>
  <summary> 📂 Розгорнути </summary> 


```python
p1 = Player(name="PLAYER", symbol=Symbol('X'))
p2 = Player(name="ANDROID", symbol=Symbol('O'))
...
```
```python
game.step(2, 2, player=p1)
game.step(0, 0, player=p1)

game.ai_step(p2)  # result in second table

+-----+---+---+---+   ->   +-----+---+---+---+
| ↓/→ | 0 | 1 | 2 |   ->   | ↓/→ | 0 | 1 | 2 |
+-----+---+---+---+   ->   +-----+---+---+---+
|  0: | X | * | * |   ->   |  0: | X | * | * |
|  1: | * | * | * |   ->   |  1: | * | O | * |
|  2: | * | * | X |   ->   |  2: | * | * | X |
+-----+---+---+---+   ->   +-----+---+---+---+
```
* AI алгоритм розуміє, що наступний хід для суперника ймовірно збере виграшну комбінацію, тому перекриває його

Розглянемо другу ситуацію
```python
game.step(0, 0, player=p1)  # X
game.step(2, 0, player=p1)  # X

game.step(0, 2, player=p2)  # O
game.step(2, 2, player=p2)  # O

game.ai_step(p2)  # result in second table

+-----+---+---+---+   ->   +-----+---+---+---+
| ↓/→ | 0 | 1 | 2 |   ->   | ↓/→ | 0 | 1 | 2 |
+-----+---+---+---+   ->   +-----+---+---+---+
|  0: | X | * | O |   ->   |  0: | X | * | O |
|  1: | * | * | * |   ->   |  1: | * | * | O |
|  2: | X | * | O |   ->   |  2: | X | * | O |
+-----+---+---+---+   ->   +-----+---+---+---+
```

* AI алгоритм ставить в пріоритет свій виграш, розуміючи що наступного виграшного ходу для суперника — вже не буде
___

</details>


</details>

___
___
