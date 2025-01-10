from grid import *
from cell import *

# grid should initialize itself with the right size and Cells


# synchronous update
def calculate_next_grid(old_grid):
    new_grid = Grid(GRID_SIZE)
    for y_index in range(len(old_grid.grid)):
        for x_index in range(len(old_grid.grid[y_index])):
            current_cell_neigbors = calculate_live_neighbors(old_grid, x_index, y_index)
            current_cell_alive = old_grid.grid[y_index][x_index].alive
            current_cell_gen = old_grid.grid[y_index][x_index].gen
            # for all cells check
            # current cell alive
            if current_cell_alive:
                # will live
                if current_cell_neigbors in LIVE_LIVE:
                    new_grid.grid[y_index][x_index].alive = True
                    new_grid.grid[y_index][x_index].gen = current_cell_gen
                    new_grid.grid[y_index][x_index].update() # increases gen by on
                # will die
                elif current_cell_neigbors in LIVE_DEAD:
                    pass # new grid, cell will stay dead
            else:
                # will live
                if current_cell_neigbors in DEAD_LIVE:
                    new_grid.grid[y_index][x_index].toggle()
                else:
                    pass # new grid, cell will stay dead
    return new_grid



# TODO - HERE ARE WHERE THE ERRORS LIE
# calculate number of live neigbors for each cell
def calculate_live_neighbors(this_grid, x, y):
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    live_neigbors = 0
    for dx, dy in directions:
        try:
            if this_grid.grid[y + dy][x + dx].alive:
                live_neigbors += 1
        except IndexError:
            continue
    return live_neigbors

# implement asynchronous update