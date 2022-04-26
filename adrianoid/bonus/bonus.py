from pathlib import Path

import pygame


class Bonus:
    def __init__(self, screen_width, screen_height, x, y):
        self.x_delta = None
        self.y_delta = None
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.height = 3 * self.screen_height / 100
        self.width = 6* (self.screen_width-300) / 100
        self.x = x
        self.y = y
        self.image = pygame.Surface((int(self.width), int(self.height)), pygame.SRCALPHA, 32)
        img = pygame.image.load(Path("grafiks", "234-Breakout-Tiles.png"))
        img = pygame.transform.scale(img, (self.width, self.height))
        self.image.blit(img, (0, 0))
        self.speed = 50

    def move(self, delta_t, game_speed):
        self.y_delta = delta_t * game_speed * self.speed
        self.y += self.y_delta