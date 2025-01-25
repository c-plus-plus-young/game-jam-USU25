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


map_data_blue = { "mapData" : (0,0,255)}
mapChangeBlue = pygame.event.Event(MAP_EVENT, **map_data_blue)


map_data_green = { "mapData" : (0,255,0)}
mapChangeGreen = pygame.event.Event(MAP_EVENT, **map_data_green)

map_data_yellow = { "mapData" : (255,255,0)}
mapChangeYellow = pygame.event.Event(MAP_EVENT, **map_data_yellow)

map_data_black = { "mapData" : (0,0,0)}
mapChangeBlack = pygame.event.Event(MAP_EVENT, **map_data_black)

#map data:
gameMap = (0, 0, 0)

# loop
run = True

while run:


    screen.fill(gameMap)

    player.draw(screen)



    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        elif event.type == pygame.USEREVENT:
            screen.fill((100, 100, 100))



        #Player Movement:
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                pygame.event.post(mapChangeRed)
                north = True
            if event.key == pygame.K_s:
                pygame.event.post(mapChangeGreen)
                south = True
            if event.key == pygame.K_a:
                pygame.event.post(mapChangeBlue)
                west = True
            if event.key == pygame.K_d:
                pygame.event.post(mapChangeYellow)
                east = True
        elif event.type == pygame.KEYUP:
            pygame.event.post(mapChangeBlack)
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


    #This is for player movement            
    if north:
        player.move(0, -velocity)    
    if south:
        player.move(0, velocity)        
    if east:
        player.move(velocity, 0)        
    if west:
        player.move(-velocity, 0)        

    

    


    # must update in order for changes to appear
    pygame.display.update()

pygame.quit()

