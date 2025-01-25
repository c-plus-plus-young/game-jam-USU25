from idlelib.macosx import isCocoaTk

import pygame
from text import advanceableText
from music import playMusic, playSound
from scene import Scene
from Thinker import Thinker
from Player import Player
import random
pygame.init()

# font init
pygame.font.init()
font = pygame.font.Font("fonts/Modak-Regular.ttf", 30)
textItems = []
isTalking = False

# window dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Background setup
background = pygame.image.load('images/hub.jpg').convert()
background_width, background_height = background.get_size()
currentScene = Scene(background=background)
backgrounds = ['images/background1.jpg','images/background2.jpg','images/background3.jpg','images/background4.jpg', 'images/background5.jpg']


#scenes set up
scenes = []
def saveScene():
    scene = Scene(currentScene.x, currentScene.y, currentScene.background)
    scenes.append(scene)

def nextScene():
    saveScene()
    background = pygame.image.load(backgrounds[random.randint(0,4)]).convert()
    scene = Scene(background=background)
    return scene

def backScene():
    return scenes.pop()





clock = pygame.time.Clock()
player = Player(SCREEN_WIDTH, SCREEN_HEIGHT)

#player movement
velocity = 10
north = south = east = west = False
animating = 0




#map data:
gameMap = (0, 0, 0)

entityList = pygame.sprite.Group()
entityList.add(player)

#create the hub thinkers
for i in range(4):
    entityList.add(Thinker(background_width, background_height))

# Main loop=======================================================
run = True

while run:

    screen.fill(gameMap)

    # background
    screen.blit(currentScene.background, (currentScene.x, currentScene.y))

    # sprites
    entityList.update()
    entityList.draw(screen)

    if (len(textItems) > 0):
        pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(15, 510, 770, 80))
        text1 = font.render(textItems[0], True, (255, 255, 255))
        screen.blit(text1, (25, 515))
    if (len(textItems) > 1):
        text2 = font.render(textItems[1], True, (255, 255, 255))
        screen.blit(text2, (25, 550))




    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        elif event.type == pygame.USEREVENT:
            screen.fill((100, 100, 100))

        # Player Movement:
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                north = True
            if event.key == pygame.K_s:
                south = True
            if event.key == pygame.K_a:
                west = True
            if event.key == pygame.K_d:
                east = True
            if event.key == pygame.K_SPACE:
                if not isTalking:
                    for entity in entityList.sprites():
                        if pygame.sprite.collide_rect(entity, player):  # Check if entity collides with player
                            if entity != player:
                                entity.isTalking = True
                                isTalking = True
                                textItems = ["hello I am a frog", "blah blah blah", "i'm teleporting you now"]
                else:
                    textItems = textItems[1:]
                    if len(textItems) == 0:
                        for entity in entityList.sprites():
                            entity.isTalking = False
                        isTalking = False
                        currentScene = nextScene()

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


    # background scrolling logic
    if north and currentScene.y < 250:
        currentScene.y += velocity
        player.north = True
    else:
        player.north = False
        
    if south and currentScene.y > -(background_height - SCREEN_HEIGHT + 250):  # prevent scrolling past the bottom edge
        currentScene.y -= velocity
        player.south = True
    else:
        player.south = False
        
    if east and currentScene.x > -(background_width - SCREEN_WIDTH + 350):
        currentScene.x -= velocity
        player.east = True
    else:
        player.east = False
        
    if west and currentScene.x < 350:
        currentScene.x += velocity
        player.west = True
    else:
        player.west = False
    

    # update the display
    pygame.display.flip()
    clock.tick(60)
    animating = animating + 1

    # Update entity positions
    for entity in entityList.sprites():
        if isinstance(entity, Thinker):
            x, y = entity.getPosition()
            entity.rect.center = (currentScene.x+x, currentScene.y+y)


pygame.quit()