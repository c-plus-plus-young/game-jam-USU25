import pygame
# Thinker class
class ThoughtBubble(pygame.sprite.Sprite):
     def __init__(self, x, y):
          pygame.sprite.Sprite.__init__(self)
          self.x = x
          self.y = y
          self.frames = []
          self.loopFrames = []
          self.animationSpeed = 50
          self.frameCounter = 0
          self.currentFrame = 0
          self.looping = False
          for i in range(1, 5):
               img = pygame.image.load(r'images/thought' + str(i) + '.png').convert_alpha()
               img = pygame.transform.scale(img, (150, 150))
               self.frames.append(img)
          for i in range(5, 7):
               img = pygame.image.load(r'images/thought' + str(i) + '.png').convert_alpha()
               img = pygame.transform.scale(img, (150, 150))
               self.loopFrames.append(img)
       
          self.image = self.frames[0]
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
               if self.currentFrame >= len(self.frames) and not self.looping:
                    self.currentFrame = 0
               if self.currentFrame >= len(self.loopFrames) and self.looping:
                    self.currentFrame = 0

               if self.looping:
                    self.image = self.loopFrames[self.currentFrame]
               else:
                    self.image = self.frames[self.currentFrame]
                    self.looping = True
               self.rect = self.image.get_rect(center=self.rect.center)  # Keep the sprite's position centered