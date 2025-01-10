import pygame
import pygame.pypm
from constants import *
from cell import Cell
from grid import Grid
from logic import *

def main():
    
    # initialize game
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    # Glock part I
    dt = 0
    timer = TICK_DURATION
    clock = pygame.time.Clock()


    # initizialized grid of dead cells only
    my_grid = Grid(GRID_SIZE)


    # set window title
    pygame.display.set_caption("Game of Life")
    running = True
    PAUSE = True
    while running:

        # fill screen
        screen.fill(BACKGROUND_COLOR)

        # draw lines
        for x in range(0, WIDTH, CELL_SIZE):  # Vertical lines
            pygame.draw.line(screen, GRID_LINE_COLOR, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, CELL_SIZE):  # Horizontal lines
            pygame.draw.line(screen, GRID_LINE_COLOR, (0, y), (WIDTH, y))

        current_time = pygame.time.get_ticks()


        # key events
        for event in pygame.event.get():
            # click grid and activate cells
            if (event.type == pygame.MOUSEBUTTONDOWN) and PAUSE:
                cursor_x, cursor_y = pygame.mouse.get_pos()
                my_grid.update_grid(cursor_x, cursor_y, PAUSE)
            # unpause game # TODO: should also pause later
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    PAUSE = not PAUSE

        # FIX BELOW ------------------------------------------
        if not PAUSE:
            if timer > 0:
                timer -= dt
            else:
                timer = 0
            if timer == 0:
                my_grid.update_cells()
                new_grid = calculate_next_grid(my_grid)
                my_grid = new_grid
                timer = TICK_DURATION
                # last_call_time = current_time
        # FIX ABOVE ------------------------------------------



        my_grid.draw(screen)
        
        pygame.display.flip()

        # Klock part II
        dt = clock.tick(60)/1000
        
        
        # subloop - if game running
        # # toggle playing on some key # TODO

if __name__ == "__main__":
    main()