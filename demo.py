import time

import pygame
from music import playMusic, playSound
from scene import Scene
from Thinker import Thinker
from Player import Player
import random
from effects import ThoughtBubble
pygame.init()

# font init
pygame.font.init()
font = pygame.font.Font("fonts/Modak-Regular.ttf", 25)
textItems = []
isTalking = False

# window dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Background setup
background = pygame.image.load('images/hubBG.png').convert()
background_width, background_height = background.get_size()
currentScene = Scene(background=background)
backgrounds = ['images/hubBG.png', 'images/bedroomBG.png','images/kitchenBG.png','images/gardenBG.png']

player = Player(SCREEN_WIDTH, SCREEN_HEIGHT)

entityList = pygame.sprite.Group()
entityList.add(player)

effectsList = pygame.sprite.Group()

#scenes set up
scenes = []
def saveScene():
    scene = Scene(currentScene.x, currentScene.y, currentScene.background)
    scenes.append(scene)

def fade_effect(fade_out=True):
    fade_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    fade_surface.fill((0, 0, 0))  # Black overlay

    for alpha in range(0, 255, 10) if fade_out else range(255, -1, -10):
        fade_surface.set_alpha(alpha)
        screen.blit(currentScene.background, (currentScene.x, currentScene.y))  # Draw current background
        entityList.update()
        entityList.draw(screen)
        if len(effectsList) > 0:
            effectsList.draw(screen)
        screen.blit(fade_surface, (0, 0))
        pygame.display.update()
        pygame.time.delay(30)


def nextScene(currentWorld):
    fade_effect(fade_out=True)
    pygame.mixer_music.stop()
    playMusic("music4.mp3")

    saveScene()
    background = pygame.image.load(backgrounds[futureWorld]).convert()
    scene = Scene(background=background)
    effectsList.empty()
    entityList.empty()

    if currentWorld == 1:
        entityList.add(Thinker(0, "duckie", background_width, background_height))
        entityList.add(Thinker(0, "ball", background_width, background_height))
        entityList.add(Thinker(0, "car", background_width, background_height))
        entityList.add(Thinker(0, "rubix", background_width, background_height))
    elif currentWorld == 2:
        entityList.add(Thinker(0, "soap", background_width, background_height))
        entityList.add(Thinker(0, "knife", background_width, background_height))
        entityList.add(Thinker(0, "pan", background_width, background_height))
        entityList.add(Thinker(0, "flour", background_width, background_height))
    elif currentWorld == 3:
        entityList.add(Thinker(0, "pail", background_width, background_height))
        entityList.add(Thinker(0, "shovel", background_width, background_height))
        entityList.add(Thinker(0, "rake", background_width, background_height))
        entityList.add(Thinker(0, "worm", background_width, background_height))

    entityList.add(player)
    if futureWorld == 0:
        playMusic("music5.mp3")
        for i in range(3):
            entityList.add(Thinker((i + 1), thinkerList[i], background_width, background_height))
    return scene

def backScene(currentScene):
    fade_effect(fade_out=True)
    entityList.empty()
    if len(scenes) > 0:
        if len(scenes) == 1:
            playMusic("music5.mp3")
        currentScene = scenes.pop()
    background_width, background_height = currentScene.background.get_size()
    for i in range(3):
        entityList.add(Thinker((i + 1), thinkerList[i], background_width, background_height))
    entityList.add(player)
    return currentScene


clock = pygame.time.Clock()


#player movement
velocity = 5
north = south = east = west = False
animating = 0

#play music
playMusic("music5.mp3")


#map data:
gameMap = (0, 0, 0)




#create the hub thinkers
thinkerList = ["frog", "rat", "plant"]
for i in range(3):
    entityList.add(Thinker((i + 1), thinkerList[i], background_width, background_height))

bubbleCounter = -60
timerLength = 900
timer = timerLength
futureWorld = -1
currentWorld = -1

collectedPail = False
collectedSoap = False
collectedDuckie = False
winTimer = -60

# Main loop=======================================================
run = True

while run:

    screen.fill(gameMap)

    # background
    screen.blit(currentScene.background, (currentScene.x, currentScene.y))

    # sprites
    entityList.update()
    entityList.draw(screen)

    if winTimer <= 0 and winTimer >= -30:
        run = False

    if collectedDuckie and collectedPail and collectedSoap:
        screen.blit(pygame.image.load("images/textContainer.jpeg").convert(), (15, 510))
        text3 = font.render("GAME WON", True, (0, 0, 0))
        screen.blit(text3, (40, 514))
        winTimer == 10



    timer -= 1
    if currentWorld > 0:
        screen.blit(pygame.image.load("images/timer.jpg").convert(), (15, 10))
        currTime = font.render(str(timer / 60)[0:4], True, (0, 0, 0))
        screen.blit(currTime, (50, 15))
        if timer < 0 and timer > -60:
            currentWorld = -1
            currentScene = backScene(currentScene)
            timer = timerLength
            playSound("bubblepop.mp3")

    bubbleCounter -= 1
    if bubbleCounter == 0:
        currentScene = nextScene(futureWorld)
        background_width, background_height = currentScene.background.get_size()
        currentWorld = futureWorld
        timer = timerLength

    if len(effectsList) > 0:
        effectsList.draw(screen)
    effectsList.update()
    if (len(textItems) > 0):
        screen.blit(pygame.image.load("images/textContainer.jpeg").convert(), (15, 510))
        # pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(15, 510, 770, 80))
        text1 = font.render(textItems[0], True, (0, 0, 0))
        screen.blit(text1, (40, 514))
    if (len(textItems) > 1):
        text2 = font.render(textItems[1], True, (0, 0, 0))
        screen.blit(text2, (40, 540))


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
                                entity.isThinking = True
                                isTalking = True
                                entity1 = entity
                                # x,y = entity.getPosition()
                                # effectsList.add(ThoughtBubble(x,y))
                                futureWorld = entity.backgroundNum
                                textItems = entity.dialogue
                else:
                    textItems = textItems[1:]
                    if len(textItems) == 0:
                        if entity1.type == "rat" or entity1.type == "frog" or entity1.type == "plant":
                            x, y = entity1.getPosition()
                            effectsList.add(ThoughtBubble(x, y))
                            playSound("flowbubble.wav")
                            bubbleCounter = 120
                        entity.isThinking = False
                        for entity in entityList.sprites():
                            entity.isTalking = False
                            # if entity != player:
                            #     if entity.type == ("plant" or "rat" or "frog"):
                                    # if entity.isThinking:
                                    #     x, y = entity.getPosition()
                                    #     effectsList.add(ThoughtBubble(x, y))
                                    #     entity.isThinking = False
                            if entity != player:
                                if entity.type == "pail":
                                    collectedPail = True
                                    playSound("bubblepop.mp3")
                                    bubbleCounter = 40
                                elif entity.type == "soap":
                                    collectedSoap = True
                                    bubbleCounter = 40
                                    playSound("bubblepop.mp3")
                                elif entity.type == "duckie":
                                    collectedDuckie = True
                                    playSound("bubblepop.mp3")
                                    bubbleCounter = 40
                        isTalking = False
                        # pygame.time.delay(10000)

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
                currentWorld = -1
                timer = timerLength
                currentWorld = -1
                currentScene = backScene(currentScene)
                playSound("bubblepop.mp3")
            if event.key == pygame.K_n:
                currentScene = nextScene()


    # background scrolling logic
    if north and currentScene.y < 150:
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

    for entity in effectsList.sprites():
        x, y = entity.getPosition()
        x = x - entity.rect.width/2
        y = y - entity.rect.height/2
        entity.rect.center = (currentScene.x+x, currentScene.y+y)

pygame.quit()