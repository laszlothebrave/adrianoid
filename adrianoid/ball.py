import cmath
import math
from pathlib import Path

import pygame


class Ball:
    def __init__(self, screen_width, screen_height):
        self.x_delta = None
        self.y_delta = None
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.radius = 20
        self.speed = 500
        self.x = (self.screen_width - 300) / 2 - self.radius
        self.y = self.screen_height / 3 * 2 - self.radius
        # self.x = 900
        # self.y=420
        self.image = pygame.Surface((int(2 * self.radius), int(2 * self.radius)), pygame.SRCALPHA, 32)
        img = pygame.image.load(Path("grafiks", "337-Breakout-Tiles.png"))
        img = pygame.transform.scale(img, (self.radius * 2, self.radius * 2))
        self.image.blit(img, (0, 0))
        self.dir_x = 0
        self.dir_y = 1
        self.border_width = 58
        self.border_width_top = 37
        self.hit_brick_sound = pygame.mixer.Sound(str(Path('sound', 'Arkanoid SFX (6).wav')))
        self.hit_paddle_sound = pygame.mixer.Sound(str(Path('sound', 'Arkanoid SFX (7).wav')))
        self.hit_bottom_sound = pygame.mixer.Sound(str(Path('sound', 'Arkanoid SFX (10).wav')))
        self.sound_channel = 0

    def move(self, delta_t, game_speed):
        self.bounce_of_walls()
        self.x_delta = delta_t * game_speed * self.speed * self.dir_x
        self.x += self.x_delta

        self.y_delta = delta_t * game_speed * self.speed * self.dir_y
        self.y += self.y_delta

    def bounce_of_walls(self):
        if self.border_width >= self.x:
            self.dir_x = abs(self.dir_x)
        if self.x >= self.screen_width - 300 - self.border_width - self.radius * 2:
            self.dir_x = -abs(self.dir_x)
        if self.border_width_top >= self.y:
            self.dir_y = abs(self.dir_y)
        if self.y >= self.screen_height - 2 * self.radius:
            self.dir_y = -abs(self.dir_y)
            # self.dir_x = 0
            # self.dir_y = 0
            self.hit_bottom_sound.play()

    def bounce_paddle(self, paddle):
        if self.y + 2 * self.radius <= paddle.y and self.y + 2 * self.radius + 3*self.y_delta >= paddle.y:
            if self.x + self.radius > paddle.x and self.x + self.radius < paddle.x + paddle.width:
                v= math.sqrt(self.dir_y ** 2 + self.dir_x ** 2)
                self.dir_x += (paddle.x + paddle.width / 2 - (self.x + self.radius)) / (paddle.width / 2) * -1
                self.dir_y = -abs(self.dir_y)
                r = math.sqrt(self.dir_y ** 2 + self.dir_x ** 2)
                self.dir_y = self.dir_y / r*v
                self.dir_x = self.dir_x / r*v
                self.hit_paddle_sound.play()

    def bounce_paddle_polar(self, paddle):
        if self.y + 2 * self.radius < paddle.y and  self.y + 2 * self.radius + 2*self.y_delta >= paddle.y:
            if self.x + self.radius > paddle.x and self.x + self.radius < paddle.x + paddle.width:

                v= math.sqrt(self.dir_y ** 2 + self.dir_x ** 2)
                fi=self.get_polar(self.dir_x, self.dir_y)
                # if fi > 2*math.pi:
                #     fi = fi - 2* math.pi
                # v, fi = cmath.polar(complex(self.x, self.y))
                # print (fi, v)
                fi_delta = (paddle.x + paddle.width / 2 - (self.x + self.radius)) / (paddle.width / 2) * math.pi/6
                new_fi = -(fi + fi_delta)

                print(new_fi, fi_delta)
                # new_fi = max(new_fi, math.pi * -3 / 4)
                # new_fi = min(new_fi, math.pi * -1 / 4)
                new_fi = max(new_fi, math.pi * -11/12)
                new_fi = min(new_fi, math.pi * -1/12)
                self.dir_y = v * math.sin(new_fi)
                self.dir_x = v * math.cos(new_fi)
                self.hit_paddle_sound.play()

    def bounce_brick(self, brick):
        if brick.x + brick.width > self.x + self.radius > brick.x and \
                brick.y > self.y + self.radius > brick.y - self.radius:
            self.dir_y = -abs(self.dir_y)
            self.hit_brick_sound.play()

            return True
        if brick.x + brick.width > self.x + self.radius > brick.x and \
                brick.y + brick.height < self.y + self.radius < brick.y + brick.height + self.radius:
            self.dir_y = abs(self.dir_y)
            self.hit_brick_sound.play()
            return True
        if brick.x > self.x + self.radius > brick.x - self.radius and \
                brick.y + brick.height > self.y + self.radius > brick.y:
            self.dir_x = -abs(self.dir_x)
            self.hit_brick_sound.play()
            return True
        if brick.x + brick.width + self.radius > self.x + self.radius > brick.x + brick.width and \
                brick.y + brick.height > self.y + self.radius > brick.y:
            self.dir_x = abs(self.dir_x)
            self.hit_brick_sound.play()
            return True
        return False



    def get_polar(self, x, y):
        if x == 0 and y > 0:
            return math.pi / 2
        if x == 0 and y < 0:
            return 3 / 2 * math.pi
        if x > 0 and y >= 0:
            return math.atan(y / x)
        if x > 0 and y < 0:
            return math.atan(y / x) + 2 * math.pi
        if x < 0:
            return math.atan(y / x) + math.pi
