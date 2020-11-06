### Snake game with Python

Dev. by : Radwane Ait Ouhani

This game is OOP based with 2 classes:
* 
* The `Snake` class : with attributes `length`,`positions`,`direction` (random at first),`color` and `score`. It has the methods : `get_head_position`,`turn`,`move`,`reset`,`draw` and `handle_keys`
* The `Food` class : with attributes `position`,`randomize_position` (random at first) and `color`. It has the methods : `randomize_position` and `draw`

It uses mainly `pygame`. The font used is `monospace` with size 16.
`pygame` are initialized so that the game run smoothly :
* The screen dimensions choosen are : `480x480`
* The framerate is set to 10

For further details, see the code : `snake_game.py`

## Game play:

Using arrows, the snake goes up,down,left and right. Collisions between the head and the tail of the snake are detected and result in a new game. 
Food are placed randomly. The score of the game is incremented with 1 each time the snake eats the food. 
A high score is updated each time accordinly and displayed alongside the score in the upper left of the screen. 

 
