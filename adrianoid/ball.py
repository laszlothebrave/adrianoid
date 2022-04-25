from pathlib import Path

import pygame


class Ball:
    def __init__(self, screen_width, screen_height):
        self.y_delta = None
        self.x = 50
        self.y = 90
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.base_radius = 5
        self.radius_multiplayer = 1
        self.radius = self.base_radius * self.radius_multiplayer
        self.base_speed = 10
        self.speed_multiplayer = 4
        self.absolute_radius = self.radius * self.screen_height / 100
        self.image = pygame.Surface((int(2*self.absolute_radius), int(2*self.absolute_radius)))
        self.image.fill((255, 0, 255))
        img=pygame.image.load(Path("grafiks","piłka.png"))
        img= pygame.transform.scale(img, (120, 120))
        self.image.blit(img,(0,0))
        self.absolute_x = self.x * self.screen_width / 100 - self.absolute_radius
        self.absolute_y = self.y * self.screen_height / 100 - self.absolute_radius
        self.dir_x = 1
        self.dir_y = -1

    def move(self, delta_t, game_speed):
        self.bounce_of_walls()
        self.x += delta_t * game_speed * self.base_speed * self.speed_multiplayer * self.dir_x
        self.absolute_x = self.x * self.screen_width / 100 - self.absolute_radius

        self.y_delta = delta_t * game_speed * self.base_speed * self.speed_multiplayer * self.dir_y
        self.y += self.y_delta
        self.absolute_y = self.y * self.screen_height / 100 - self.absolute_radius

    def bounce_of_walls(self):
        if 0 > self.absolute_x or self.absolute_x > self.screen_width - 2*self.absolute_radius:
            self.dir_x = -self.dir_x
        if 0 > self.absolute_y or self.absolute_y > self.screen_height - 2*self.absolute_radius:
            self.dir_y = -self.dir_y


