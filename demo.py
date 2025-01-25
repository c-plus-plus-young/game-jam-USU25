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
class Player(object):

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

# loop
run = True
while run:

    screen.fill((0, 0, 0))

    player.draw(screen)

    # key = pygame.key.get_pressed()
    # if key[pygame.K_LEFT] == True:
    #     player.move_ip(-1, 0)
    # elif key[pygame.K_RIGHT] == True:
    #     player.move_ip(1, 0)
    # elif key[pygame.K_UP] == True:
    #     player.move_ip(0, -1)
    # elif key[pygame.K_DOWN] == True:
    #     player.move_ip(0, 1)


    # buttons:
    # x = 0
    # a = 1
    # b = 2
    # y = 3
    # l = 4
    # r = 5
    # SELECT = 8
    # START = 9


    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.JOYBUTTONDOWN:
            if pygame.joystick.Joystick(0).get_button(0):
                player.change_color("blue")
            elif pygame.joystick.Joystick(0).get_button(1):
                player.change_color("red")
            elif pygame.joystick.Joystick(0).get_button(2):
                player.change_color("yellow")
            elif pygame.joystick.Joystick(0).get_button(3):
                player.change_color("green")
        elif event.type == pygame.JOYAXISMOTION:
            print(event)
    x_speed = round(pygame.joystick.Joystick(0).get_axis(0))
    y_speed = round(pygame.joystick.Joystick(0).get_axis(1))
    player.move(x_speed, y_speed)


    # must update in order for changes to appear
    pygame.display.update()

pygame.quit()

