import pygame

import ctypes

from adrianoid.balls import Balls
from adrianoid.fps_counter import FPSCounter
from adrianoid.paddle import Paddle

ctypes.windll.user32.SetProcessDPIAware()

class Adrianoid:
    def __init__(self):
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

    def on_init(self):
        pygame.init()
        infoObject = pygame.display.Info()
        self.weight = infoObject.current_w
        self.height = infoObject.current_h
        self.weight = 1920
        self.height = 1080
        self._display_surf = pygame.display.set_mode((self.weight, self.height), pygame.SRCALPHA | pygame.DOUBLEBUF | pygame.FULLSCREEN | pygame.SCALED)
        # self._display_surf = pygame.display.set_mode((self.weight, self.height), pygame.SRCALPHA | pygame.DOUBLEBUF)

        self.keys_pressed = pygame.key.get_pressed()
        self._running = True

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            self.keys_pressed = pygame.key.get_pressed()

    def on_loop(self):
        for i in self.balls.balls:
            i.move(self.delta_t, self.game_speed)
        if self.keys_pressed[pygame.K_a]:
            self.paddle.move_left(self.delta_t, self.game_speed)
        if self.keys_pressed[pygame.K_d]:
            self.paddle.move_right(self.delta_t, self.game_speed)
        if self.keys_pressed[pygame.K_ESCAPE]:
            self._running = False

    def on_render(self):
        self._display_surf.fill((50, 50, 100))
        self._display_surf.blit(self.paddle.image, (self.paddle.absolute_x, self.paddle.absolute_y))
        for i in self.balls.balls:
            self._display_surf.blit(i.image, (i.absolute_x, i.absolute_y))
        self.render_fps()
        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init():
            self._running = False

        clock = pygame.time.Clock()
        while self._running:
            clock.tick()
            self.delta_t = clock.get_time()/1000
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


if __name__ == "__main__":
    app = Adrianoid()
    app.on_execute()
