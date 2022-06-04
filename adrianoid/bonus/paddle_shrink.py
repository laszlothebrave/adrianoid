from adrianoid.bonus.bonus import Bonus


class PaddleShrink(Bonus):
    def __init__(self, screen_width, screen_height, x, y):
        super().__init__(screen_width, screen_height, x, y)
        self.animation_length=6
        self.load_animation(288)

    def apply_bonus(self,balls,paddle,score_counter):
        paddle.change_width(-2)