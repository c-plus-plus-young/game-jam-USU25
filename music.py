
from pygame import mixer

mixer.init()

mixer.music.load("music/Abstraction - Fear -2HAC Volume 28- - 01 Triskaidekaphobia.mp3")

mixer.music.set_volume(0.7)

mixer.music.play()

while True:

    print("Press 'p' to pause, 'r' to resume")
    print("Press 'e' to exit the program")
    query = input("  ")

    if query == 'p':

        # Pausing the music
        mixer.music.pause()
    elif query == 'r':

        # Resuming the music
        mixer.music.unpause()
    elif query == 'e':

        # Stop the mixer
        mixer.music.stop()
        break