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
    porcupine = None
    paud = None
    audio_stream = None
    try:
        
        #here we use pretrained keyword
        porcupine = pvporcupine.create(keywords=["webster", "alexa"], sensitivities=[0.7])
        paud = pyaudio.PyAudio()
        audio_stream = paud.open(
            rate=porcupine.sample_rate,
            channels=1,
            format=pyaudio.paInt16,
            input=True,
            frames_per_buffer=porcupine.frame_length
        )
        
        #listening loop
        while True:
            keyword = audio_stream.read(porcupine.frame_length)
            keyword = struct.unpack_from("h" * porcupine.frame_length, keyword)
            
            #here we will process keyword which comes from the mic
            if keyword_index>=0: # type: ignore
                print("hotword detected")
                
                #here we press a shortcut key that is win +j
                import pyautogui as autogui
                autogui.keyDown("win")
                autogui.press("j")
                time.sleep(2)
                autogui.keyUp("win")
                
    except:
        if porcupine is not None:
            porcupine.delete()
        if audio_stream is not None:
            audio_stream.close()
        if paud is not None:
            paud.terminate()

            