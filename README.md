# scramble-solver
brute force solver for scramble square 3x3
Python 3.6

# Presentation
the scrambe square is a 3x3 puzzle, where eah tile has 4 edges, and each edge contains half of an image 
ex:

![alt text](https://www.scramblesquares.com/wp-content/uploads/10132-Cats72dpi.jpg)

# Objective
The objective here is to create a solver that uses recursion and back tracking in order to output the result.
In our solver, each drawing (cat) has a number from 1 to 4 where head = +1 ; Tail = -1
Each tile is then recognised by: Name='p1', Used already in the puzzle = False, Northern edge=+1, East=-4, South=+2, West=-2.


# Sources
Sramble squares vendor:<br>
ex: https://www.scramblesquares.com/

A graph theoretical approach to solving Scramble Squares puzzles (with Mali Zhang), Involve, 5, no. 3 (2012), pp. 313-325.<br>
http://users.wfu.edu/masonsk/scramblesquares.pdf<br>

Python Sudoku Solver - Computerphile (2020)<br>
https://www.youtube.com/watch?v=G_UYXzGuqvM<br>
