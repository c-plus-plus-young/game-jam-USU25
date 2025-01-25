import pygame
from text import printText
from music import playMusic

pygame.init()

# window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# must create character outside of loop
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for i in range(4):
            img = pygame.image.load(r'images/image' + str(i) + '.png').convert()
            img = pygame.transform.scale(img, (150,150))
            self.images.append(img)
            self.image = self.images[i]
            self.rect = self.image.get_rect()

        self.player = pygame.Rect((200, 250, 50, 50))
        # self.color = "white"

    def move(self, x_speed, y_speed):
        self.rect.move_ip((x_speed, y_speed))

clock = pygame.time.Clock()
player = Player()
player.rect.x = 0  # go to x
player.rect.y = 0  # go to y
player_list = pygame.sprite.Group()
player_list.add(player)

north = False
south = False
east = False
west = False
xVelocity = 2
yVelocity = 2

# loop
run = True
while run:
    screen.fill((0, 0, 0))

    player_list.draw(screen)
    pygame.display.flip()

    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
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

    if north:
        if player.rect.y > 0:
            player.move(0, -yVelocity)
        player.image = player.images[3]
    if south:
        if player.rect.y < SCREEN_HEIGHT - 150:
            player.move(0, yVelocity)
        player.image = player.images[0]
    if east:
        if player.rect.x < SCREEN_WIDTH - 150:
            player.move(xVelocity, 0)
        player.image = player.images[2]
    if west:
        if player.rect.x > 0:
            player.move(-xVelocity, 0)
        player.image = player.images[1]

    

    


    # must update in order for changes to appear
    pygame.display.update()

pygame.quit()

