import pygame
from text import advanceableText
from music import playMusic
from scene import Scene
from Thinker import Thinker
from Player import Player
import random
pygame.init()

# font init
pygame.font.init()
font = pygame.font.Font("fonts/Modak-Regular.ttf", 30)
textItems = []

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
    thinker = Thinker(background_width, background_height)
    entityList.add(thinker)

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

    if animating // 15 >= len(player.northImages):
        animating = 0

    if not thinker.isTalking:
        thinker.image = thinker.idleImages[animating // 15]
    else:
        thinker.image = thinker.talkingImages[animating // 15]

    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        elif event.type == pygame.USEREVENT:
            screen.fill((100, 100, 100))

        #Player Movement:
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and pygame.sprite.collide_rect(thinker, player):
                if not thinker.isTalking:
                    thinker.isTalking = True
                    textItems = ["hello I am a frog", "hello!!!!", "blah blah blah", "i'm teleporting you now"]
                    if len(textItems) == 0:
                        thinker.isTalking = False
                else:
                    textItems = textItems[1:]
                    if len(textItems) == 0:
                        thinker.isTalking = False
                # currentScene = nextScene()
            if event.key == pygame.K_w:
                north = True
            if event.key == pygame.K_s:
                south = True
            if event.key == pygame.K_a:
                west = True
            if event.key == pygame.K_d:
                east = True
            if event.key == pygame.K_SPACE:
                textItems = textItems[1:]
                print(textItems)
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
    if north and currentScene.y < 0:
        currentScene.y += velocity
        player.image = player.northImages[animating // 15]
    if south and currentScene.y > -(background_height - SCREEN_HEIGHT):  # prevent scrolling past the bottom edge
        currentScene.y -= velocity
        player.image = player.southImages[animating // 15]
    if east and currentScene.x > -(background_width - SCREEN_WIDTH):
        currentScene.x -= velocity
        player.image = player.eastImages[animating // 15]
    if west and currentScene.x < 0:
        currentScene.x += velocity
        player.image = player.westImages[animating // 15]

    # update the display
    pygame.display.flip()
    clock.tick(60)
    animating = animating + 1

    #Update entity positions
    for entity in entityList.sprites():
        if isinstance(entity, Thinker):
            x, y = entity.getPosition()
            entity.rect.center = (currentScene.x+x, currentScene.y+y)

pygame.quit()