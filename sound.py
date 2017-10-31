from pygame import *

mixer.init()
mixer.music.load('sound.ogg')
mixer.music.play()

while mixer.music.get_busy():
    time.Clock().tick(10)
