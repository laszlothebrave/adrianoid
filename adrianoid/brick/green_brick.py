from pathlib import Path

import pygame

from adrianoid.brick.brick import Brick


class GreenBrick(Brick):
    def __init__(self,screen_width, screen_height, grid_x, grid_y):
        super().__init__(screen_width, screen_height, grid_x, grid_y)
        img = pygame.image.load(Path("grafiks", "012-Breakout-Tiles.png"))
        img = pygame.transform.scale(img, (self.width, self.height))
        self.image.blit(img, (0, 0))
        self.points=20