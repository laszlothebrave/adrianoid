from adrianoid.bonus.bonus import Bonus


class BallSpeedDown(Bonus):
    def __init__(self, screen_width, screen_height, x, y):
        super().__init__(screen_width, screen_height, x, y)
        self.animation_length=7
        self.load_animation(258)

    def apply_bonus(self, balls, paddle,score_counter):
        for ball in balls.balls:
            ball.change_speed(-200)
