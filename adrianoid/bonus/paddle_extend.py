from adrianoid.bonus.bonus import Bonus


class PaddleExtend(Bonus):
    def __init__(self, screen_width, screen_height, x, y):
        super().__init__(screen_width, screen_height, x, y)
        self.animation_length=6
        self.load_animation(294)

    def apply_bonus(self,balls,paddle,score_counter):
        paddle.change_width(4)