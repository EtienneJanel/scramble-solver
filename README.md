# Python 3x3 Puzzle solver
(or scramble square)
Python 3.6


# Presentation
the scrambe square is a 3x3 puzzle as per below. The objective is to complete the puzzle with all edges matching:

![alt text](https://raw.githubusercontent.com/EtienneJanel/scramble-solver/master/puzzle_example.PNG)

# Our objective
Create a simple script that uses recursion - brute force - in order to solve the puzzle.
In our solver, each one of the four drawings has a number from 1 to 4 where Head = +1 ; Tail = -1
![alt text](https://raw.githubusercontent.com/EtienneJanel/scramble-solver/master/puzzle_example.PNG)

mapping:
    {1:'duck head', -1:'duck tail',
    2:'orangutan head', -2:'orangutan tail',
    3:'sloth head', -3:'sloth tail',
    4:'snake head', -4:'snake tail'}

# Sources
Sramble squares vendor:<br>
ex: https://www.scramblesquares.com/

A graph theoretical approach to solving Scramble Squares puzzles (with Mali Zhang), Involve, 5, no. 3 (2012), pp. 313-325.<br>
http://users.wfu.edu/masonsk/scramblesquares.pdf<br>

Python Sudoku Solver - Computerphile (2020)<br>
https://www.youtube.com/watch?v=G_UYXzGuqvM<br>
