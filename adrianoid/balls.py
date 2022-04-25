from adrianoid.ball import Ball


class Balls:
    def __init__(self, screen_width, screen_height):
        self.balls = []
        self.balls.append(Ball(screen_width, screen_height))