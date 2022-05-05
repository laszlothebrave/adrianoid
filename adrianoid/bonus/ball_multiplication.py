import copy

from adrianoid.bonus.bonus import Bonus


class BallMultiplication(Bonus):
    def __init__(self, screen_width, screen_height, x, y):
        super().__init__(screen_width, screen_height, x, y)
        self.animation_length=7
        self.load_animation(231)

    def apply_bonus(self, balls, paddle,score_counter):
        cloned_balls=[]
        for ball in balls.balls:
            x=ball.copy()
            x.random_direction()
            cloned_balls.append(x)
        balls.balls.extend(cloned_balls)

