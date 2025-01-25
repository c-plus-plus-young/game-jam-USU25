import pygame

# Thinker class
class Thinker(pygame.sprite.Sprite):
    def __init__(self, backgroundNum, type, backgroundWidth = 50, backgroundHeight = 50):
        pygame.sprite.Sprite.__init__(self)
        self.isTalking = False
        self.isThinking = False
        self.idleImages = []
        self.talkingImages = []
        self.animationSpeed = 17
        self.frameCounter = 0
        self.currentFrame = 0
        self.backgroundNum = backgroundNum
        self.dialogue = []
        self.type = type
        self.collected = False
        #
        # def update():
        #     if self.collected == True:
        #         self.Rec.


        # Frog NPC
        if type == "frog":
            # Set initial position of NPC
            self.x = 140
            self.y = 200

            # Add talking sprites and idle sprites to NPC
            for i in range(1, 3):
                img = pygame.image.load(r'images/frog' + str(i) + '.png').convert_alpha()
                img = pygame.transform.scale(img, (130, 130))
                self.idleImages.append(img)
            for i in range(2, 4):
                img = pygame.image.load(r'images/frog' + str(i) + '.png').convert_alpha()
                img = pygame.transform.scale(img, (130, 130))
                self.talkingImages.append(img)

            # Create dialogue for NPC
            self.dialogue = ["Hello I am a frog", "Ribbit", "Silly frog thing"]

        # Rat NPC
        elif type == "rat":
            # Set initial position of NPC
            self.x = 490
            self.y = 200

            # Add talking sprites and idle sprites to NPC
            for i in range(1, 3):
                img = pygame.image.load(r'images/rat' + str(i) + '.png').convert_alpha()
                img = pygame.transform.scale(img, (150, 150))
                self.idleImages.append(img)
            for i in range(1, 3):
                img = pygame.image.load(r'images/rat' + str(i) + '.png').convert_alpha()
                img = pygame.transform.scale(img, (150, 150))
                self.talkingImages.append(img)

            # Create dialogue for NPC
            self.dialogue = ["Hello I am a rat", "Squeak", "Silly rat thing"]

        # Plant NPC
        elif type == "plant":
            # Set initial position of NPC
            self.x = 830
            self.y = 200

            # Add talking sprites and idle sprites to NPC
            for i in range(1, 3):
                img = pygame.image.load(r'images/plant' + str(i) + '.png').convert_alpha()
                img = pygame.transform.scale(img, (150, 150))
                self.idleImages.append(img)
            for i in range(1, 3):
                img = pygame.image.load(r'images/plant' + str(i) + '.png').convert_alpha()
                img = pygame.transform.scale(img, (150, 150))
                self.talkingImages.append(img)

            # Create dialogue for NPC
            self.dialogue = ["Hello I am a plant", "Plant noise", "Silly plant thing"]

        elif type == "soap":
            # Set initial position of NPC
            self.x = 830
            self.y = 200
            img = pygame.image.load("images/soap.png").convert_alpha()
            self.idleImages.append(img)
            self.talkingImages.append(img)
            self.dialogue = ["COLLECTED SOAP"]
            self.isThinking = False
        elif type == "pail":
            # Set initial position of NPC
            self.x = 830
            self.y = 200
            img = pygame.image.load("images/pail.png").convert_alpha()
            self.idleImages.append(img)
            self.talkingImages.append(img)
            self.dialogue = ["COLLECTED PAIL"]
            self.isThinking = False
        elif type == "duckie":
            # Set initial position of NPC
            self.x = 830
            self.y = 200
            img = pygame.image.load("images/duckie.png").convert_alpha()
            self.idleImages.append(img)
            self.talkingImages.append(img)
            self.dialogue = ["COLLECTED RUBBER DUCK"]
            self.isThinking = False


        self.image = self.idleImages[0]
        self.rect = self.image.get_rect(center=(self.x, self.y))

        # # Set initial position of NPC
        # self.x = random.randint(0 + 30, backgroundWidth - 30)
        # self.y = random.randint(0 + 30, backgroundHeight - 30)
        # self.rect = self.image.get_rect(center=(self.x, self.y))

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