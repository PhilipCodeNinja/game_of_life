# Grid and cell settings
GRID_SIZE = 20 # number of cells per row and col #
CELL_SIZE = 20 # in pixels
BACKGROUND_COLOR = "BLACK"
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
TICK_DURATION = 2