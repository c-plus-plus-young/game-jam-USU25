from pygame import mixer

mixer.init()

"""
Function to play a song. Just use song name, not relative location
(assuming file in music folder)
"""


def playMusic(songName):
    mixer.music.load("music/" + str(songName))

    mixer.music.set_volume(0.5)

    mixer.music.play()


def playSound(soundName):
    my_sound = mixer.Sound("sound/" + soundName)

    my_sound.play()

    my_sound.set_volume(1)


if __name__ == '__main__':
    playMusic("music4.mp3")
