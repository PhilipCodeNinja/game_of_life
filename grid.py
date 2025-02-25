import math
from constants import *
from cell import *

class Grid():


    def __init__(self, grid_size):
        self.timer = 0
        self.size = grid_size
        self.grid = [[Cell(x, y, CELL_SIZE) for x in range(self.size)] for y in range(self.size)]

    # the grid should know what is being clicked, not the cell
    def update_grid(self, x_cursor, y_cursor, pause):
        if pause:
            # calculate cell coordinates
            x_coord = math.floor(x_cursor/CELL_SIZE) # makes sure my pixels get converted to the cells coordinates
            y_coord = math.floor(y_cursor/CELL_SIZE)
            if 0 <= x_coord < self.size and 0 <= y_coord < self.size:
                self.grid[y_coord][x_coord].toggle()

    def draw(self, screen):      
        # redraw all cells
        for row in self.grid:
            for cell in row:
                # cell.shout()
                cell.draw(screen)

    def update_cells(self):      
        # redraw all cells
        for row in self.grid:
            for cell in row:
                # cell.shout()
                cell.update()

    
    def grid_cell(self, y_coord, x_coord):
        return self.grid[y_coord][x_coord]



        # for each cell determine number of neighbors

        # live 0, 1 neigbor - dies

        # live 2, 3 neigbor - lives

        # live 4, 5, 6, 7, 8 neighbors - dies

        # dead 3 neigbors - lives


    # game logic

    # grid should know game of life rules
    # synchronous update:
    # take old grid and return new grid



    # make random asynchronous update and 