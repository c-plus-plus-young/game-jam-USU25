import pygame
from text import advanceableText
from music import playMusic
from scene import Scene
from Thinker import Thinker
from Player import Player
import random
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


thinker = Thinker(background_width, background_height)


clock = pygame.time.Clock()
player = Player(SCREEN_WIDTH, SCREEN_HEIGHT)

#player movement
north = False
south = False
east = False
west = False
velocity = 1

#Custom Events
SCENE_CHANGE_EVENT = pygame.USEREVENT + 1
sceneData = { "scene" : nextScene()}
sceneChange = pygame.event.Event(SCENE_CHANGE_EVENT, **sceneData)


#map data:
gameMap = (0, 0, 0)

entityList = pygame.sprite.Group()
entityList.add(player)
entityList.add(thinker)

# Movement
north = south = east = west = False
xVelocity = 10
yVelocity = 10
animating = 0

# Main loop=======================================================
run = True

while run:

    screen.fill(gameMap)

    # background
    screen.blit(currentScene.background, (currentScene.x, currentScene.y))

    # sprites
    entityList.update()
    entityList.draw(screen)

    if animating // 15 >= len(player.northImages):
        animating = 0

    thinker.image = thinker.idleImages[animating // 15]

    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        elif event.type == pygame.USEREVENT:
            screen.fill((100, 100, 100))

        #Player Movement:
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and pygame.sprite.collide_rect(thinker, player):
                thinker.image = thinker.talkingImages[animating // 15]
                frogText = ["hello I am a frog", "blah blah blah", "i'm teleporting you now"]
                advanceableText(frogText, screen)
                currentScene = nextScene()
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

        elif event.type == SCENE_CHANGE_EVENT:
            gameMap = event.mapData

    # background scrolling logic
    if north and currentScene.y < 0:
        currentScene.y += yVelocity
        player.image = player.northImages[animating // 15]
    if south and currentScene.y > -(background_height - SCREEN_HEIGHT):  # prevent scrolling past the bottom edge
        currentScene.y -= yVelocity
        player.image = player.southImages[animating // 15]
    if east and currentScene.x > -(background_width - SCREEN_WIDTH):
        currentScene.x -= xVelocity
        player.image = player.eastImages[animating // 15]
    if west and currentScene.x < 0:
        currentScene.x += xVelocity
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