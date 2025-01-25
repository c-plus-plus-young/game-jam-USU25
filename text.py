import pygame, time

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
black = (0, 0, 0)
pygame.font.init()
font = pygame.font.Font("fonts/Modak-Regular.ttf", 30)
"""
prints text to screen
length is time you want message visible
y_pos is, you guessed it, y position of text
"""

def printText(message, y_pos, screen):
    text = font.render(message, True, black)
    screen.blit(text, (25, y_pos))
    disp = True;
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
    newMessage = messages.pop(0)
    printText(newMessage, 515, screen)
    # if len(messages) >= 1:
    #     newMessage = messages.pop(0)
    #     printText(newMessage, 550, screen)
#                 if event.key == pygame.K_k:
#                 advanceableText(["WORDS", "More words", "MMMMM MMMMM MMMMM MMMMM MMMMM MMMMM MMM"], screen)



if __name__ == '__main__':
    print('Welcome to Earth')
    time.sleep(1)