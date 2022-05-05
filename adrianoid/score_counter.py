import pygame


class ScoreCounter:
    def __init__(self):
        self.current_score=0
        self.my_font = pygame.font.SysFont('Segoe Print', 75)
        self.text_surface = self.my_font.render(str(self.current_score), False, (255, 234, 0))

    def add_score(self,score_number):
        self.current_score = self.current_score+score_number
        self.text_surface = self.my_font.render(str(self.current_score), False, (255, 234, 0))