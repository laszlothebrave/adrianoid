import pygame
BLACK = (0, 0, 0)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)


class Paddle:
    def __init__(self, screen_width, screen_height):
        self.x = 50
        self.y = 90
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.base_length = 15
        self.length_multiplayer = 1
        self.base_speed = 10
        self.speed_multiplayer = 1
        self.height = 5 * self.screen_height / 100
        self.width = self.base_length * self.length_multiplayer * self.screen_width / 100
        self.image = pygame.Surface((int(self.width), int(self.height)))
        self.image.fill(MAGENTA)
        self.absolute_x = self.x * self.screen_width / 100 - self.width / 2
        self.absolute_y = self.y * self.screen_height / 100 - self.height / 2

    def move_right(self, delta_t, game_speed):
        if self.x < 100 - self.base_length * self.length_multiplayer / 2:
            self.x += delta_t * game_speed * self.base_speed * self.speed_multiplayer
            self.absolute_x = self.x * self.screen_width / 100 - self.width / 2

    def move_left(self, delta_t, game_speed):
        if self.base_length * self.length_multiplayer / 2 < self.x:
            self.x -= delta_t * game_speed * self.base_speed * self.speed_multiplayer
            self.absolute_x = self.x * self.screen_width / 100 - self.width / 2



