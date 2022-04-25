from pathlib import Path

import pygame


class Brick:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.height = 3 * self.screen_height / 100
        self.width = 6* self.screen_width / 100
        self.x = 50 / 100 * (self.screen_width - 300) - self.width/2
        self.y = 40 / 100 * self.screen_height
        self.image = pygame.Surface((int(self.width), int(self.height)), pygame.SRCALPHA, 32)
        img = pygame.image.load(Path("grafiks", "001-Breakout-Tiles.png"))
        img = pygame.transform.scale(img, (self.width, self.height))
        self.image.blit(img, (0, 0))

