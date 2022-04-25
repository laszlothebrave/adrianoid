class MyObject:
    def __init__(self, screen_width, screen_height):
        self.x = 50
        self.y = 90
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.base_length = 15
        self.length_multiplayer = 1
        self.base_speed = 10
        self.speed_multiplayer = 1
        self.height = 5 * self.screen_height / 100
        self.width = self.base_length * self.length_multiplayer * self.screen_width / 100
        self.image = pygame.Surface((int(self.width), int(self.height)))
        self.image.fill(MAGENTA)
        self.absolute_x = self.x * self.screen_width / 100 - self.width / 2
        self.absolute_y = self.y * self.screen_height / 100 - self.height / 2