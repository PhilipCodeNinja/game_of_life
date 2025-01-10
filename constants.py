# Grid and cell settings
GRID_SIZE = 50 # number of cells per row and col #
CELL_SIZE = 25 # in pixels
BACKGROUND_COLOR = (120, 100, 100)
GRID_LINE_COLOR = "WHITE"
WIDTH = GRID_SIZE * CELL_SIZE
HEIGHT = GRID_SIZE * CELL_SIZE


# Colors 
# Define a list of gradually darker green colors
CELL_COLORS = [
    (152, 255, 152),  # Mint Green
    (50, 205, 50),    # Lime Green
    (34, 139, 34),    # Forest Green
    (53, 94, 59),     # Hunter Green
    (1, 50, 32)       # Dark Green
]
MAX_CELL_GEN = len(CELL_COLORS)

# how much time should pass per tick
TICK_DURATION = 0.4 # 1 sec
TICK_DURATIONS = [n/10 for n in range(1, 15)]


# number of neigbors for different results
LIVE_LIVE = [2, 3]
LIVE_DEAD = [0, 1, 4, 5, 6, 7, 8]
DEAD_LIVE = [3]