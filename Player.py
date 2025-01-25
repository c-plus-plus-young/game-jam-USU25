import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height):
        pygame.sprite.Sprite.__init__(self)

        self.north = self.south = self.east = self.west = False
        self.northImages = []
        self.southImages = []
        self.eastImages = []
        self.westImages = []

        self.animationSpeed = 10
        self.frameCounter = 0
        self.currentFrame = 0

        # Add images to North, South, East and West sprite sheets
        for i in range(1, 3):
            img = pygame.image.load(r'images/wizard' + str(i) + '.png').convert_alpha()
            img = pygame.transform.scale(img, (110, 110))
            self.southImages.append(img)
        for i in range(3, 5):
            img = pygame.image.load(r'images/wizard' + str(i) + '.png').convert_alpha()
            img = pygame.transform.scale(img, (110, 110))
            self.eastImages.append(img)
        for i in range(5, 7):
            img = pygame.image.load(r'images/wizard' + str(i) + '.png').convert_alpha()
            img = pygame.transform.scale(img, (110, 110))
            self.westImages.append(img)
        for i in range(7, 9):
            img = pygame.image.load(r'images/wizard' + str(i) + '.png').convert_alpha()
            img = pygame.transform.scale(img, (110, 110))
            self.northImages.append(img)
        self.image = self.northImages[0]
        self.rect = self.image.get_rect(center=(screen_width // 2, screen_height // 2))  # Center player on screen

    def move(self, x_speed, y_speed):
        # The player stays in place, so no movement is needed
        pass

    def update(self):
        if self.north or self.south or self.west or self.east:

            # Increment the frame counter
            self.frameCounter += 1
            
            # Switch frames based on the animation speed
            if self.frameCounter >= self.animationSpeed:
                self.frameCounter = 0
                self.currentFrame += 1
                self.frameCounter += 1  # Move to the next frame
                
                # Reset to the first frame if we've gone past the last frame
                if self.currentFrame >= len(self.southImages):
                    self.currentFrame = 0
                
                # Update the image to the new frame
                if self.north:
                    self.image = self.northImages[self.currentFrame]
                elif self.south:
                    self.image = self.southImages[self.currentFrame]
                elif self.west:
                    self.image = self.westImages[self.currentFrame]
                elif self.east:
                    self.image = self.eastImages[self.currentFrame]
                
                self.rect = self.image.get_rect(center=self.rect.center)  # Keep the sprite's position centered