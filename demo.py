import pygame
from text import advanceableText
from music import playMusic

pygame.init()

# window dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Background setup
background = pygame.image.load('images/background1.jpg').convert()
background_width, background_height = background.get_size()
bg_x = 0
bg_y = 0


# Player class
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

#map data:
gameMap = (0, 0, 0)

player_list = pygame.sprite.Group()
player_list.add(player)

# Movement
north = south = east = west = False
xVelocity = 10
yVelocity = 10

# Main loop
run = True

while run:

    screen.fill(gameMap)

    # background
    screen.blit(background, (bg_x, bg_y))

    # player
    player_list.draw(screen)

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
        elif event.type == MAP_EVENT:
            gameMap = event.mapData

    # background scrolling logic
    if north and bg_y < 0:
        bg_y += yVelocity
        player.image = player.images[3]
    if south and bg_y > -(background_height - SCREEN_HEIGHT):  # prevent scrolling past the bottom edge
        bg_y -= yVelocity
        player.image = player.images[0]
    if east and bg_x > -(background_width - SCREEN_WIDTH):
        bg_x -= xVelocity
        player.image = player.images[2]
    if west and bg_x < 0:
        bg_x += xVelocity
        player.image = player.images[1]

    # update the display
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
