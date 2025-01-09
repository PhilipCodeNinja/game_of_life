import pygame
from constants import *

class Cell():
    def __init__(self, x, y, cell_size):
        self.x = x
        self.y = y
        self.cell_size = cell_size
        self.alive = False
        self.gen = 0
        # self.hitbox = [[self.x*self.cell_size + 1, self.x*self.cell_size - 1]  # x range - from left x + 1px to right x - 1px
        #                [self.y*self.cell_size + 1, self.y*self.cell_size - 1]] # y range - from top y + 1px to bottom x - 1 px
    
    # update should update cell, alive or dead, generation and call draw()
    def update(self):
        if self.alive:
            # We're giving the cell a max as we want to color older cells differently
            self.gen = min(self.gen + 1, MAX_CELL_GEN)
            # put self.draw here
            # make sure it has screen var from above,
            # 
        else:
            self.gen = 0
            

    def toggle(self):
        if self.alive:
            self.alive = False
        elif not self.alive:
            self.alive = True
            self.gen = 1
    
    # draws a red rectangle at the center of each coordinate
    def draw(self, screen):
        if self.alive:
            pygame.draw.rect(screen,
                            CELL_COLORS[self.gen - 1],
                            # (0, 255, 0),
                            (self.x*self.cell_size + 1,
                             self.y*self.cell_size + 1,
                             self.cell_size - 1,
                             self.cell_size - 1))
            # print("Cell colors: ", CELL_COLORS[self.gen - 1])
        elif not self.alive:
            pygame.draw.rect(screen,
                             BACKGROUND_COLOR,
                             (self.x*self.cell_size + 1,
                              self.y*self.cell_size + 1,
                              self.cell_size - 1,
                              self.cell_size - 1))
        

    def shout(self):
        # Print tests:
        if self.alive:
            print("Cell: x -", self.x , " y - ", self.y, " I live, gen: ", self.gen)
        else:
            print("Cell: x -", self.x , " y - ", self.y, " I dead")
