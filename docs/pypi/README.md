# titato
___Library of the game tic-tac-toe + AI.___ _Experimental functionality with dynamic parameters of the game field_

___

## Features:
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

[*Documentation on GitHub*](https://github.com/Steppe-Mammoth/titato/tree/dev-1.x#titato)