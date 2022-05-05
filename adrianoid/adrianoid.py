import random

import pygame

import ctypes

from adrianoid import paddle
from adrianoid.background import Background
from adrianoid.balls import Balls
from adrianoid.bonus.ball_multiplication import BallMultiplication
from adrianoid.bonus.ball_speed_up import BallSpeedUp
from adrianoid.bonus.bonus import Bonus
from adrianoid.bonus.paddle_extend import PaddleExtend
from adrianoid.bonus.score50 import Score50
from adrianoid.bonus.score500 import Score500
from adrianoid.brick.brick import Brick
from adrianoid.brick.green_brick import GreenBrick
from adrianoid.fps_counter import FPSCounter
from adrianoid.paddle import Paddle
from adrianoid.score_counter import ScoreCounter

ctypes.windll.user32.SetProcessDPIAware()


class Adrianoid:
    def __init__(self):
        self.time = None
        self.fps_cur = None
        self.fps = None
        self.keys_pressed = None
        self._running = True
        self._display_surf = None
        self.weight = 0
        self.height = 0
        self.on_init()
        self.start_time = 0
        self.delta_t = 0
        self.game_speed = 1
        self.paddle = Paddle(self.weight, self.height)
        pygame.font.init()
        self.my_font = pygame.font.SysFont('Comic Sans MS', 130)
        self.fps = FPSCounter()
        self.balls = Balls(self.weight, self.height)
        self.background = Background()
        self.bricks = []
        for x in range(-7, 8, 1):
            for y in range(8):
                if random.randint(0,1) == 0:
                    self.bricks.append(Brick(self.weight, self.height, -x, y))
                else:
                    self.bricks.append(GreenBrick(self.weight,self.height,-x,y))

        self.bonuses = []
        self.coor = [0, 0, 0, 0]
        self.score_counter = ScoreCounter()

    def on_init(self):
        pygame.mixer.pre_init()
        pygame.mixer.init(48000, -16, 8, 4098)
        pygame.init()
        pygame.mixer.set_num_channels(16)
        infoObject = pygame.display.Info()
        self.weight = infoObject.current_w
        self.height = infoObject.current_h
        self.weight = 1920
        self.height = 1080
        #self._display_surf = pygame.display.set_mode((self.weight, self.height),
                                                     #pygame.SRCALPHA | pygame.DOUBLEBUF | pygame.FULLSCREEN | pygame.SCALED)
        self._display_surf = pygame.display.set_mode((self.weight, self.height),
                                                     pygame.SRCALPHA | pygame.DOUBLEBUF | pygame.SCALED)

        self.keys_pressed = pygame.key.get_pressed()
        self._running = True

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            self.keys_pressed = pygame.key.get_pressed()

    def on_loop(self):
        if self.keys_pressed[pygame.K_s]:
            self.paddle.lock_ball = True
        else:
            self.paddle.lock_ball = False

        for i in self.balls.balls:
            i.move(self.delta_t, self.game_speed, self.paddle, self.coor)
        for i in self.bonuses:
            i.move(self.delta_t, self.game_speed)
        if self.keys_pressed[pygame.K_a]:
            self.paddle.move_left(self.delta_t, self.game_speed)
        if self.keys_pressed[pygame.K_d]:
            self.paddle.move_right(self.delta_t, self.game_speed)
        if self.keys_pressed[pygame.K_ESCAPE]:
            self._running = False
        for ball in self.balls.balls:
            for brick in self.bricks:
                if ball.bounce_brick(brick):
                    self.bonuses.append(BallMultiplication(self.weight, self.height, brick.x, brick.y))
                    self.bricks.remove(brick)
                    self.score_counter.add_score(brick.points)
        for bonus in self.bonuses:
            if self.paddle.catch_bonus(bonus):
                bonus.apply_bonus(self.balls,self.paddle,self.score_counter)
                self.bonuses.remove(bonus)

    def on_render(self):
        self._display_surf.fill((50, 50, 100))
        self._display_surf.blit(self.background.background0, (0, 0))
        self._display_surf.blit(self.paddle.image, (self.paddle.x, self.paddle.y))
        pygame.draw.line(self._display_surf, (120, 120, 120), (self.coor[0], self.coor[1]), (self.coor[2], self.coor[3]), 5)
        for i in self.balls.balls:
            self._display_surf.blit(i.image, (i.x, i.y))
        for brick in self.bricks:
            self._display_surf.blit(brick.image, (brick.x, brick.y))
        for bonus in self.bonuses:
            self._display_surf.blit(bonus.image[bonus.image_counter], (bonus.x, bonus.y))
            bonus.update_image_counter(self.time)
        self.render_fps()
        self.render_score()
        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        clock = pygame.time.Clock()
        while self._running:
            clock.tick()
            self.time = pygame.time.get_ticks()
            self.delta_t = clock.get_time() / 1000
            self.fps_cur = clock.get_fps()
            self.fps.add_measurement(clock.get_fps())
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()

    def render_fps(self):
        text_surface = self.my_font.render(str(self.fps.get_fps()), False, (255, 0, 0))
        self._display_surf.blit(text_surface, (0, 0))

    def render_score(self):
        self._display_surf.blit(self.score_counter.text_surface, (1700, 0))

if __name__ == "__main__":
    app = Adrianoid()
    app.on_execute()
