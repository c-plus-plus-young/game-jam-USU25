import pygame
import random

# Thinker class
class Thinker(pygame.sprite.Sprite):
    def __init__(self, backgroundWidth = 50, backgroundHeight = 50):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load(r'images/player_image.png').convert_alpha()
        img = pygame.transform.scale(img, (50, 50))  # Resize player image to 50x50
        self.image = img
        self.x = random.randint(0, backgroundWidth)
        self.y = random.randint(0 ,backgroundHeight)
        self.rect = self.image.get_rect(center=(self.x, self.y))

    def move(self, x_speed, y_speed):
        # The player stays in place, so no movement is needed
        pass

    def getPosition(self):
        return self.x, self.y