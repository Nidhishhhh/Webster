import sqlite3
import webbrowser
from playsound import playsound
import eel
import os
from Engine.command import speak
from Engine.config import Assistant_Name
import pywhatkit as kit
import re


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
    
def extract_yt_term(command):
    pattern = r'play\s+(.*?)\s+on\s+youtube'  #here play is a constant term, (.+?) is a dynamic term and on youtube is again a constant term.
    match = re.search(pattern, command, re.IGNORECASE) #here we have imported re(REGULAR EXPRESSION) module to pass the qury. re.IGNORECASE is used to ignore the capital and small letters.
    return match.group(1) if match else None #match.group is used to search the dynamic term in the query. If no match is found, it returns None.