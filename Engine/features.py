import sqlite3
import webbrowser
from playsound import playsound
import eel
import os
from Engine.command import speak
from Engine.config import Assistant_Name
import pywhatkit as kit
import re
import pvporcupine
import pyaudio
import struct
import time

from Engine.helper import extract_yt_term


conn = sqlite3.connect("webster.db")
cursor = conn.cursor()

#playing assistant sound function on startup
@eel.expose
def playAssistantSound():
    music_dir = "www\\assets\\audio\\startup_sound.mp3"
    playsound(music_dir)
    
    
    
def openCommand(query):
    query = query.replace(Assistant_Name, "")
    query = query.replace("open", "")
    query.lower()

    app_name = query.strip() #used to remove the extra spaces in the query.

    if app_name != "":  #checking if the app_name is not empty.

        try:
            cursor.execute(
                'SELECT path FROM sys_command WHERE name IN (?)', (app_name,))
            results = cursor.fetchall()

            if len(results) != 0:
                speak("Opening "+query)
                os.startfile(results[0][0])

            elif len(results) == 0: 
                cursor.execute(
                'SELECT url FROM web_command WHERE name IN (?)', (app_name,))
                results = cursor.fetchall()
                
                if len(results) != 0:
                    speak("Opening "+query)
                    webbrowser.open(results[0][0])

                else:
                    speak("Opening "+query)
                    try:
                        os.system('start '+query)
                    except:
                        speak("not found")
        except:
            speak("some thing went wrong")
            
def PlayYoutube(query):
    search_term = extract_yt_term(query)
    speak("Playing "+search_term+" on YouTube")
    kit.playonyt(search_term)
    

def hotword():
    porcupine=None
    paud=None
    audio_stream=None

    try:
        access_key="paste your access key here" #to create access key signup to https://console.picovoice.ai/ 
    #new version of pvporcupine has a limitation--> you can use only in upto 3 devices in free version. 
    #you can install older version of pvporcupine --> pip install pvporcupine==1.9.5 , which does not require any access key
    #if you are using older version of pvporcupine, replace the below line with--> porcupine=pvporcupine.create(keywords=["jarvis","alexa"])
        porcupine=pvporcupine.create(keywords=["computer","jarvis","alexa"]) #pvporcupine.KEYWORDS for all keywords
        paud=pyaudio.PyAudio()
        audio_stream=paud.open(rate=porcupine.sample_rate,channels=1,format=pyaudio.paInt16,input=True,frames_per_buffer=porcupine.frame_length)
        while True:
            keyword=audio_stream.read(porcupine.frame_length)
            keyword=struct.unpack_from("h"*porcupine.frame_length,keyword)
            keyword_index=porcupine.process(keyword)
            if keyword_index>=0:
                print("hotword detected")
                
                import pyautogui as autogui
                autogui.keyDown("win")
                autogui.press("j")
                time.sleep(2)
                autogui.keyUp("win")

    finally:
        if porcupine is not None:
            porcupine.delete()
        if audio_stream is not None:
            audio_stream.close()
        if paud is not None:
            paud.terminate()          


           