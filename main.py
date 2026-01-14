import os

import eel

from Engine.features import *

from Engine.command import *

def start():
    eel.init('www')


    playAssistantSound()

    os.system('start msedge.exe --app="http://localhost:8000/index.html"')

    eel.start('index.html', mode=None, host='localhost', block=True)


