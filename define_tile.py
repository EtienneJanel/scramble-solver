class Tile:
    def __init__(self, name, north, east, south, west):
        """defines the image with cardinal points 🧭
        north = up, clockwise
        name: STR
        north, south...: INT (from -4 to +4)            
            positive numbers for 'heads'
            negative for 'tails' of the image
        used: BOOL
        """
        self.name = name
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        
        self.rotation = 0
        
        self.used = False
    
    def turn(self):
        """turn the tile by 90 degrees  🤸‍
        if the tile should not be used in the grid already"""
        north = self.west 
        east = self.north
        south= self.east 
        west = self.south

        self.north = north
        self.east = east
        self.south = south
        self.west = west

        if self.rotation == 3:
            self.rotation = 0
        else:
            self.rotation +=1

        
    def __repr__(self):
        return self.name