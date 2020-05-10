
from tkinter import *
from PIL import ImageTk, Image

class Show_puzzle():
    """If the solution is found, show puzzle images with tkinter"""
    
    def __init__(self, list_solution):
        root = Tk()
        canvas = Canvas(root, width = 700, height = 700)
        canvas.pack()
        
        tk_images = [ImageTk.PhotoImage(Image.open(f"./img/{tile.name}.png").rotate(90* tile.rotation)) for tile in list_solution]
        
        c=0
        # Create 3x3 grid
        for y in range(3):
            for x in range(3):
                canvas.create_image(228*x, 228*y, anchor = NW,
                                    image=tk_images[c])
                c+=1
        root.mainloop()
        

class Solution:
    """takes a grid 3x3 and 9tiles as argument,
    shows the solution if exists (list)
    as well as the image"""
    
    def __init__(self, list_tiles):
        self.grid = [[0,0,0], [0,0,0], [0,0,0]]    
        
        self.s_grid = None
        self.s_tiles = None
        self.recursion(-1,0, self.grid, list_tiles)
        
        if self.s_grid != None:
            print('here is the solution! 🙆‍')
            [print(i) for i in self.s_grid]
            print('place tile with north like:')
            print(self.s_tiles)
            Show_puzzle(self.solution_as_list())
        else:
            print('No solution found\nmaybe another time 🤯')
            return None

    def solution_as_list(self):
        return [item for sublist in self.s_grid for item in sublist]
        
    def possible(self, y, x, new_tile):
        """From the new_tile we are about to place,
        check neighbor North👆 and West👈 only
        we assume the next tile (east and south) are empty"""
        if new_tile.used == False:
            if y > 0:
                north = new_tile.north + self.grid[y-1][x].south
            else:
                north = 0

            if x > 0:
                west = new_tile.west + self.grid[y][x-1].east
            else:
                west = 0

            if north == 0 and west == 0:
                """it's a match! 👏"""
                return True
        return False

    def recursion(self, x,y, grid, list_tiles):
        """Search ! 🐶"""

        # 1. increment coordinate x,y
        if x == 2 and y ==2:
            # We should have the solution 
            self.s_grid = grid
            self.s_tiles = [tile.north for tile in list_tiles]
        elif x == 2:
            y += 1
            x = 0
        else:
            x += 1

        # 2. For each tile in the list, test it on the next empty space
        for tile in list_tiles:
            # Test the 4 position for each tile
            for _ in range(4):
                if self.possible(y, x, tile):
                    grid[y][x] = tile
                    tile.used = True

                    self.recursion(x,y, grid, list_tiles)

                    # if we exit the above recursion we have either:
                    #  -found the solution:
                    if grid[2][2]:
                        return

                    #  -remove the current tile
                    grid[y][x] = 0
                    tile.used = False
                # If we checked all the remaining tiles we can turn this one
                tile.turn()

        return       