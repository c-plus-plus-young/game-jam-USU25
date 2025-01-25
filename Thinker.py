import pygame
import random

# Thinker class
class Thinker(pygame.sprite.Sprite):
    def __init__(self, backgroundNum, backgroundWidth = 50, backgroundHeight = 50):
        pygame.sprite.Sprite.__init__(self)
        self.isTalking = False
        self.isThinking = False
        self.idleImages = []
        self.talkingImages = []
        self.animationSpeed = 15
        self.frameCounter = 0
        self.currentFrame = 0
        self.backgroundNum = backgroundNum


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
        self.x = random.randint(0 + 30, backgroundWidth - 30)
        self.y = random.randint(0 + 30, backgroundHeight - 30)
        self.rect = self.image.get_rect(center=(self.x, self.y))

    def getPosition(self):
        return self.x, self.y
    
    #got a little bitty help from chat gpt on this one. 
    def update(self):
        # Increment the frame counter
        self.frameCounter += 1
        # Switch frames based on the animation speed
        if self.frameCounter >= self.animationSpeed:
            self.frameCounter = 0
            self.currentFrame += 1
            self.frameCounter += 1  # Move to the next frame
            
            # Reset to the first frame if we've gone past the last frame
            if self.currentFrame >= len(self.idleImages):
                self.currentFrame = 0
            
            # Update the image to the new frame
            if self.isTalking:
                self.image = self.talkingImages[self.currentFrame]
            else:
                self.image = self.idleImages[self.currentFrame]
            self.rect = self.image.get_rect(center=self.rect.center)  # Keep the sprite's position centered