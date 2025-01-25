import pygame
from text import advanceableText
from music import playMusic
from scene import Scene
import random


#Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for i in range(4):
            img = pygame.image.load(r'images/image' + str(i) + '.png').convert_alpha()
            img = pygame.transform.scale(img, (50, 50))  # Resize player image to 50x50
            self.images.append(img)
        self.image = self.images[0]
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))  # Center player on screen

    def move(self, x_speed, y_speed):
        # The player stays in place, so no movement is needed
        pass

# Thinker class
class Thinker(pygame.sprite.Sprite):
    def __init__(self, backgroundWidth = 50, backgroundHeight = 50):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load(r'images/player_image.png').convert_alpha()
        img = pygame.transform.scale(img, (50, 50))  # Resize player image to 50x50
        self.image = img
        self.rect = self.image.get_rect(center=(random.randint(0, backgroundWidth), random.randint(0 ,backgroundHeight)))

    def move(self, x_speed, y_speed):
        # The player stays in place, so no movement is needed
        pass


pygame.init()

# window dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Background setup
background = pygame.image.load('images/background1.jpg').convert()
background_width, background_height = background.get_size()
currentScene = Scene(background=background)


#scenes set up
scenes = []
def saveScene():
    scene = Scene(currentScene.x, currentScene.y, currentScene.background)
    scenes.append(scene)

def nextScene():
    saveScene()
    background = pygame.image.load('images/background2.jpg').convert()
    scene = Scene(background=background)
    return scene

def backScene():
    return scenes.pop()



thinker = Thinker()



clock = pygame.time.Clock()
player = Player()

#player movement
north = False
south = False
east = False
west = False
velocity = 1

#Custom Events
MAP_EVENT = pygame.USEREVENT + 1
map_data_red = { "mapData" : (255,0,0)}
mapChangeRed = pygame.event.Event(MAP_EVENT, **map_data_red)


#map data:
gameMap = (0, 0, 0)

entityList = pygame.sprite.Group()
entityList.add(player)
entityList.add(thinker)



# Movement
north = south = east = west = False
xVelocity = 10
yVelocity = 10

# Main loop=======================================================
run = True

while run:

    screen.fill(gameMap)

    # background
    screen.blit(currentScene.background, (currentScene.x, currentScene.y))

    # player
    entityList.draw(screen)
    

    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        elif event.type == pygame.USEREVENT:
            screen.fill((100, 100, 100))

        #Player Movement:
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                
                north = True
            if event.key == pygame.K_s:
                
                south = True
            if event.key == pygame.K_a:
                
                west = True
            if event.key == pygame.K_d:
            
                east = True
        elif event.type == pygame.KEYUP:
        
            if event.key == pygame.K_w:
                north = False
            if event.key == pygame.K_s:
                south = False
            if event.key == pygame.K_a:
                west = False
            if event.key == pygame.K_d:
                east = False
            if event.key == pygame.K_b:
                currentScene = backScene()
            if event.key == pygame.K_n:
                currentScene = nextScene()

        elif event.type == MAP_EVENT:
            gameMap = event.mapData

    # background scrolling logic
    if north and currentScene.y < 0:
        currentScene.y += yVelocity
        player.image = player.images[3]
    if south and currentScene.y > -(background_height - SCREEN_HEIGHT):  # prevent scrolling past the bottom edge
        currentScene.y -= yVelocity
        player.image = player.images[0]
    if east and currentScene.x > -(background_width - SCREEN_WIDTH):
        currentScene.x -= xVelocity
        player.image = player.images[2]
    if west and currentScene.x < 0:
        currentScene.x += xVelocity
        player.image = player.images[1]

    # update the display
    pygame.display.flip()
    clock.tick(60)

    #Update entity positions
    for thinker in entityList:
        pass


pygame.quit()



#
