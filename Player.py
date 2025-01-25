import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height):
        pygame.sprite.Sprite.__init__(self)
        self.northImages = []
        self.southImages = []
        self.eastImages = []
        self.westImages = []

        # Add images to North, South, East and West sprite sheets
        for i in range(1, 3):
            img = pygame.image.load(r'images/wizard' + str(i) + '.png').convert_alpha()
            img = pygame.transform.scale(img, (100, 100))
            self.southImages.append(img)
        for i in range(3, 5):
            img = pygame.image.load(r'images/wizard' + str(i) + '.png').convert_alpha()
            img = pygame.transform.scale(img, (100, 100))
            self.eastImages.append(img)
        for i in range(5, 7):
            img = pygame.image.load(r'images/wizard' + str(i) + '.png').convert_alpha()
            img = pygame.transform.scale(img, (100, 100))
            self.westImages.append(img)
        for i in range(7, 9):
            img = pygame.image.load(r'images/wizard' + str(i) + '.png').convert_alpha()
            img = pygame.transform.scale(img, (100, 100))
            self.northImages.append(img)
        self.image = self.northImages[0]
        self.rect = self.image.get_rect(center=(screen_width // 2, screen_height // 2))  # Center player on screen

    def move(self, x_speed, y_speed):
        # The player stays in place, so no movement is needed
        pass