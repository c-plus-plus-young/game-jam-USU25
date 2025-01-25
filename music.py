from pygame import mixer

mixer.init()

"""
Function to play a song. Just use song name, not relative location
(assuming file in music folder)
"""
def playMusic(songName):

    mixer.music.load("music/" + str(songName))

    mixer.music.set_volume(0.7)

    mixer.music.play()

if __name__ == '__main__':
    playMusic("music4.mp3")
