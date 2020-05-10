# Python 3x3 Puzzle solver
(or scramble square)
Python 3.6


# Presentation
the scrambe square is a 3x3 puzzle as per below. The objective is to complete the puzzle with all edges matching:

![alt text](https://raw.githubusercontent.com/EtienneJanel/scramble-solver/master/other/puzzle_example.PNG)

You can try it out and print the above puzzle!<br>
If somehow you are stuck, don't hesitate to run main.ipynb to see the solution.<br>
After all there is only **(4^9) × (9!) = 95 126 814 720** different arrangements 🙆‍♂️

# Our objective
Create a simple script that uses recursion - brute force - in order to solve the puzzle.
In our solver, each one of the four drawings has a number from 1 to 4 where Head = +1 ; Tail = -1

![alt text](https://raw.githubusercontent.com/EtienneJanel/scramble-solver/master/other/puzzle_example_coordinates.PNG)

    mapping:
        1:'duck head',      -1:'duck tail',
        2:'orangutan head', -2:'orangutan tail',
        3:'sloth head',     -3:'sloth tail',
        4:'snake head',     -4:'snake tail'

# Structure
**main.ipynb:**        main file that takes the puzzle and solves it<br>
**define_tile.py:**     defines the image with coordinates or cardinal points p1 = Tile("p1",-1,-3,-2,4)<br>
**solution_finder.py:** takes a grid 3x3 and 9 tiles as argument, shows the solution if exists<br>

**./img:**    .png images (p1, p2...) used to show the solution if any<br>
**./emojis:** list of .png raw images to build the tiles in ./img<br>
**./other:**  miscelaneous<br>

# Sources
Sramble squares vendor:<br>
ex: https://www.scramblesquares.com/

A graph theoretical approach to solving Scramble Squares puzzles (with Mali Zhang), Involve, 5, no. 3 (2012), pp. 313-325.<br>
http://users.wfu.edu/masonsk/scramblesquares.pdf<br>

Python Sudoku Solver - Computerphile (2020)<br>
https://www.youtube.com/watch?v=G_UYXzGuqvM<br>

Emojis <br>
https://emojipedia.org/

# TO DO (deadline: never 👍)
- Create interactive version of the puzzle to play it with the mouse
- Finish the script that would randomise the images (emojis) in the puzzle
- Create a script to generate puzzle
- Challenge the solver by adding more tiles (3x4, 4x4,...)
- Build smarter version of the solver and compare the performances
- Host the final version of the game and solver online
