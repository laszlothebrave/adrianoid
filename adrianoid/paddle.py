from pathlib import Path

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


# wymiary pola do gry to: prawy margines 58; lewy 358

class Paddle:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.length = 15
        self.base_speed = 10
        self.speed_multiplayer = 100
        self.height = 2 * self.screen_height / 100
        self.width = self.length * self.screen_width / 100
        self.x = 50 / 100 * (self.screen_width - 300) - self.width / 2
        self.y = 90 / 100 * self.screen_height
        self.image = pygame.Surface((int(self.width), int(self.height)), pygame.SRCALPHA, 32)
        img = pygame.image.load(Path("grafiks", "317-Breakout-Tiles.png"))
        img = pygame.transform.scale(img, (self.width, self.height))
        self.image.blit(img, (0, 0))
        self.frame_width = 58
        self.catch_bonus_sound = pygame.mixer.Sound(str(Path('sound', 'Arkanoid SFX (9).wav')))

    def move_right(self, delta_t, game_speed):
        if self.x < self.screen_width - 300 - self.width - self.frame_width:
            self.x += delta_t * game_speed * self.base_speed * self.speed_multiplayer

    def move_left(self, delta_t, game_speed):
        if self.frame_width < self.x:
            self.x -= delta_t * game_speed * self.base_speed * self.speed_multiplayer

    def catch_bonus(self, bonus):
        if self.x + self.width > bonus.x > self.x - bonus.width and \
                self.y - bonus.height < bonus.y < self.y + self.height:
            self.catch_bonus_sound.play()
            return True
        return False
