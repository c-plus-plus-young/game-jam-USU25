import pygame, time

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
black = (0, 0, 0)
pygame.font.init()
font = pygame.font.Font("fonts/Modak-Regular.ttf", 30)
remove_text = []
"""
prints text to screen
length is time you want message visible
y_pos is, you guessed it, y position of text
"""

def printText(message, y_pos, screen):
    text = font.render(message, True, black)
    screen.blit(text, (25, y_pos))
    disp = True
    while disp:
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    disp = False

"""
Gonna use for most text in the game
as name implies, draws two lines at a time
"""
def printTwoLines(message1, message2, screen):
    pygame.draw.rect(screen, green, pygame.Rect(15, 510, 770, 80))
    text1 = font.render(message1, True, black)
    screen.blit(text1, (25, 515))
    text2 = font.render(message2, True, black)
    screen.blit(text2, (25, 550))
    pygame.display.flip()
    disp = True
    while disp:
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    disp = False


"""
Text that can be advanced by placing spacebar
message for this should be a list, with each line
being a separate string in said list (approximately 
39 characters including spaces), though exact size
will depend upon specific characters used
"""
def advanceableText(messages, screen):
    # may cause issues if character is moving when text starts
    # (character will glide when text finishes)
    size = len(messages)
    pygame.draw.rect(screen, green, pygame.Rect(15, 510, 770, 80))
    newMessage = messages.pop(0)
    printText(newMessage, 515, screen)
    while len(messages) >= 1:
        oldMessage = newMessage
        newMessage = messages.pop(0)
        printTwoLines(oldMessage, newMessage, screen)
    # necessary as screen prints again if only one message
    if (size > 1):
        pygame.draw.rect(screen, green, pygame.Rect(15, 510, 770, 80))
        printText(newMessage, 515, screen)


if __name__ == '__main__':
    print('Welcome to Earth')
    time.sleep(1)