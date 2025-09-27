from playsound import playsound
import eel
import os
from Engine.command import speak
from Engine.config import Assistant_Name
import pywhatkit as kit
import re

#playing assistant sound function on startup
@eel.expose
def playAssistantSound():
    music_dir = "www\\assets\\audio\\startup_sound.mp3"
    playsound(music_dir)
    
    
    
def openCommand(query):
    query = query.replace(Assistant_Name, "")
    query = query.replace("open", "")
    query = query.lower()
    
    if query!="":
        speak(f"Opening {query}")
        os.system('start ' + query)
    else:
        speak("Nothing to open")
        
def PlayYoutube(query):
    search_term = extract_yt_term(query)
    speak("Playing "+search_term+" on YouTube")
    kit.playonyt(search_term)
    
def extract_yt_term(command):
    pattern = r'play\s+(.*?)\s+on\s+youtube'  #here play is a constant term, (.+?) is a dynamic term and on youtube is again a constant term.
    match = re.search(pattern, command, re.IGNORECASE) #here we have imported re(REGULAR EXPRESSION) module to pass the qury. re.IGNORECASE is used to ignore the capital and small letters.
    return match.group(1) if match else None #match.group is used to search the dynamic term in the query. If no match is found, it returns None.