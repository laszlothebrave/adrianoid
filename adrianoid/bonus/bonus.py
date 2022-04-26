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
        self.image = []
        for i in range(7):
            image = pygame.Surface((int(self.width), int(self.height)), pygame.SRCALPHA, 32)
            img = pygame.image.load(Path("grafiks", str(231+i)+"-Breakout-Tiles.png"))
            img = pygame.transform.scale(img, (self.width, self.height))
            image.blit(img, (0, 0))
            self.image.append(image)
        self.image_counter = 0
        self.last_image_update = 0
        self.speed = 50

    def move(self, delta_t, game_speed):
        self.y_delta = delta_t * game_speed * self.speed
        self.y += self.y_delta

    def update_image_counter(self, time):
        print(time)
        if time - self.last_image_update > 600:
            self.last_image_update = time
            self.image_counter = (self.image_counter + 1)% 7