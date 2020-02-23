import numpy as np

# -----------------------------------------------------------------#
# Draws are: Flower, Fish, Flag, Bird
# 'grid' is a numpy array composed of tile from p1 to p9
  # where grid[y] is ordinate and grid[x] is abscissa  
# 'tiles' is a dict containing each tile
# 'tile' is a dict as:
  # {"name":'p1', "used":False, 
  # 'north edge':1,'east edge': 2, 'south edge':-2, 'west edge':-3}
# -----------------------------------------------------------------#

def reset():
    # Flower: 1; Fish: 2; Flag: 3; Bird: 4
    
    p1 = {"name":'p1', "used":False, 'n':1,'e': 2, 's':-2, 'w':-3}
    p2 = {"name":'p2', "used":False, 'n':2,'e':-4, 's':4, 'w':3}
    p3 = {"name":'p3', "used":False, 'n':2,'e':3, 's':-4, 'w':1}

    p4 = {"name":'p4', "used":False, 'n':-2,'e':1, 's':-4, 'w':3}
    p5 = {"name":'p5', "used":False, 'n':-1,'e':-4, 's':1, 'w':3}
    p6 = {"name":'p6', "used":False, 'n':4,'e':-3, 's':2, 'w':-1}

    p7 = {"name":'p7', "used":False, 'n':2,'e':-3, 's':-4, 'w':-1}
    p8 = {"name":'p8', "used":False, 'n':-4,'e':1, 's':-2, 'w':3}
    p9 = {"name":'p9', "used":False, 'n':3,'e':-1, 's':4, 'w':-2}

    tiles = {'p1':p1,'p2':p2,'p3':p3,
             'p4':p4,'p5':p5,'p6':p6,
             'p7':p7,'p8':p8,'p9':p9}
    grid = np.array(
            [[None, None, None], 
             [None, None, None], 
             [None, None, None]])
    return tiles, grid

def north(y,x,tile):
    # check north edge of the tile
    # against south edge of the tile below
    global grid
    global tiles
    if y>0 and grid[y-1][x] != None:
        return tiles[tile]['n']+grid[y-1][x]['s'] == 0
    else:
        return True

def east(y,x,tile):
    global grid
    global tiles
    if x<2 and grid[y][x+1] != None:
        return tiles[tile]['e']+grid[y][x+1]['w'] == 0
    else:
        return True
    
def south(y,x,tile):
    global grid
    global tiles
    if y<2 and grid[y+1][x] != None:
        return tiles[tile]['s']+grid[y+1][x]['n'] == 0
    else:
        return True
        
def west(y,x,tile):
    global grid
    global tiles
    if x>0 and grid[y][x-1] != None:
        return tiles[tile]['w']+grid[y][x-1]['e'] == 0    
    else:
        return True

def turn(tile):
    # rotate the tile by 90deg 
    global tiles
    n = tiles[tile]['n']
    e = tiles[tile]['e']
    s = tiles[tile]['s']
    w = tiles[tile]['w']
    
    tiles[tile]['n'] = w
    tiles[tile]['e'] = n
    tiles[tile]['s'] = e
    tiles[tile]['w'] = s

def possible(y,x, tile):
    # check if all the edges can match
    # -- might be wrongly written as Solve() outputs wrong solutions
    global grid
    global tiles
    for i in range(4):
        if north(y,x,tile) and east(y,x,tile) and \
            south(y,x,tile) and west(y,x,tile):
            return True
            break
        else:
            turn(tile)
    return False
    
def solve():
    # recursively check each y and x in grid
    # if tile is possible
    global grid
    global tiles
    for y in range(3):
        for x in range(3):
            if grid[y][x] == None:
                for tile in tiles.keys():
                    if possible(y, x, tile) and not tiles[tile]['used']:
                        grid[y][x] = tiles[tile]
                        tiles[tile]['used'] = True
                        solve()
                        grid[y][x] = None
                        tiles[tile]['used'] = False
                return 
    print(f"solution:\n{grid}")
    input("more?\n")
    
tiles, grid = reset()
solve()
