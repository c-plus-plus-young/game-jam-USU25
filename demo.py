import pygame

pygame.init()
pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
print(joysticks)

# window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# must create character outside of loop
class Player(pygame.sprite.Sprite):
    def __init__(self):
        self.player = pygame.Rect((200, 250, 50, 50))
        self.color = "white"

    def move(self, x_speed, y_speed):
        self.player.move_ip((x_speed, y_speed))

    def change_color(self, color):
        self.color = color

    def draw(self, game_screen):
        pygame.draw.rect(game_screen, self.color, self.player)

clock = pygame.time.Clock()
player = Player()
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

    player.draw(screen)



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
        player.move(0, -yVelocity)    
    if south:
        player.move(0, yVelocity)        
    if east:
        player.move(xVelocity, 0)        
    if west:
        player.move(-xVelocity, 0)        

    

    


    # must update in order for changes to appear
    pygame.display.update()

pygame.quit()

