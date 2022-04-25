from pathlib import Path

import pygame.image


class Background:
    def __init__(self):
        self.all_backgrounds = pygame.image.load(Path("grafiks", "backgrounds.png"))
        self.background0 = pygame.Surface((224, 240))
        self.background0.blit(self.all_backgrounds,(0,0),(14,370,224,240) )
        self.background0=pygame.transform.scale(self.background0,(1620,1080))
        self.background1 = pygame.Surface((223, 239))
        self.background1.blit(self.all_backgrounds, (0, 0), (370, 246, 223, 239))
        self.background2 = pygame.Surface((223, 239))
        self.background2.blit(self.all_backgrounds, (0, 0), (370, 478, 223, 239))
        self.background3 = pygame.Surface((223, 239))
        self.background3.blit(self.all_backgrounds, (0, 0), (370, 710, 223, 239))
        self.background4 = pygame.Surface((223, 239))
        self.background4.blit(self.all_backgrounds, (0, 0), (370, 972, 223, 239))