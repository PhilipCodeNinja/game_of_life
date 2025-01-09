import pygame
import pygame.pypm
from constants import *
from cell import Cell
from grid import Grid

def main():
    
    # initialize game
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    # Glock part I
    dt = 0
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

        my_grid.update_cells()

        # key events
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                cursor_x, cursor_y = pygame.mouse.get_pos()
                my_grid.update_grid(cursor_x, cursor_y, PAUSE)
                # tell grid where the click happened

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    PAUSE = not PAUSE
                    if PAUSE:
                        print("Paused")
                    else:
                        print("Unpaused")
        # game logic -  state dependent - ignored if PAUSE = True

        my_grid.draw(screen)


        if not PAUSE:
            pass # play game

            

        pygame.display.flip()


        # Glock part II
        dt = clock.tick(60)
        
        
        # subloop - if game running
        # # toggle playing on some key # TODO

if __name__ == "__main__":
    main()