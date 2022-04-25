from pathlib import Path

import pygame


class Ball:
    def __init__(self, screen_width, screen_height):
        self.x_delta = None
        self.y_delta = None
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.radius = 20
        self.speed= 350
        self.x = (self.screen_width-300)/2-self.radius
        self.y = self.screen_height/2-self.radius
        self.image = pygame.Surface((int(2*self.radius), int(2*self.radius)),pygame.SRCALPHA, 32)
        img=pygame.image.load(Path("grafiks","337-Breakout-Tiles.png"))
        img= pygame.transform.scale(img, (self.radius*2, self.radius*2))
        self.image.blit(img,(0,0))
        self.dir_x = 0
        self.dir_y = 1
        self.border_width=58
        self.border_width_top = 37

    def move(self, delta_t, game_speed):
        self.bounce_of_walls()
        self.x_delta =  delta_t * game_speed * self.speed* self.dir_x
        self.x +=  self.x_delta


        self.y_delta = delta_t * game_speed * self.speed * self.dir_y
        self.y += self.y_delta


    def bounce_of_walls(self):
        if self.border_width >= self.x:
            self.dir_x=abs(self.dir_x)
        if self.x >= self.screen_width-300-self.border_width-self.radius*2:
            self.dir_x = -abs(self.dir_x)
        if self.border_width_top >= self.y:
            self.dir_y = abs(self.dir_y)
        if self.y >= self.screen_height-2*self.radius:
            self.dir_y = -abs(self.dir_y)
            self.dir_x = 0
            self.dir_y = 0

    def bounce_paddle(self, paddle):
        if self.y + 2*self.radius> paddle.y and self.y + self.radius< paddle.y-paddle.height/2:
            if self.x+self.radius > paddle.x and self.x + self.radius < paddle.x + paddle.width/3:
                self.dir_y = -abs(self.dir_y)
                self.dir_x = self.dir_x - 0.5
            if self.x+self.radius > paddle.x and self.x + self.radius < paddle.x + paddle.width:
               self.dir_y = -abs(self.dir_y)
            if self.x + self.radius > paddle.x and self.x + self.radius > paddle.x + 2/3*paddle.width:
                self.dir_y = -abs(self.dir_y)
                self.dir_x = self.dir_x + 0.5

    def bounce_brick(self,brick):
        if brick.x + brick.width > self.x + self.radius > brick.x and \
            brick.y < self.y + self.radius > brick.y - self.radius:
            print(self.x, brick.x, self.y, self.radius, brick.y, brick.width)
            self.dir_y= -abs(self.dir_y)





