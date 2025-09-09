from playsound import playsound


#playing assistant sound function on startup
def playAssistantSound():
    music_dir = "www\\assets\\audio\\startup_sound.mp3"
    playsound(music_dir)