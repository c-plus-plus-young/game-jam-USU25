import pygame
import random

# Thinker class
class Thinker(pygame.sprite.Sprite):
    def __init__(self, backgroundWidth = 50, backgroundHeight = 50):
        pygame.sprite.Sprite.__init__(self)
        self.isTalking = False
        self.idleImages = []
        self.talkingImages = []

        # Add talking sprites and idle sprites to NPC
        for i in range(1, 3):
            img = pygame.image.load(r'images/frog' + str(i) + '.png').convert_alpha()
            img = pygame.transform.scale(img, (100, 100))
            self.idleImages.append(img)
        for i in range(2, 4):
            img = pygame.image.load(r'images/frog' + str(i) + '.png').convert_alpha()
            img = pygame.transform.scale(img, (100, 100))
            self.talkingImages.append(img)
        self.image = self.idleImages[0]

        # Set initial position of NPC
        self.x = random.randint(0, backgroundWidth)
        self.y = random.randint(0 ,backgroundHeight)
        self.rect = self.image.get_rect(center=(self.x, self.y))

    def getPosition(self):
        return self.x, self.y