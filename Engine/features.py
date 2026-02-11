import json
import sqlite3
from sysconfig import get_path
import webbrowser
from playsound import playsound
import eel
import os
from Engine.command import speak
from Engine.config import Assistant_Name, LLM_KEY
import pywhatkit as kit
import re
import pvporcupine
import pyaudio
import struct
import time
from Engine.helper import extract_yt_term, fix_porcuppine__dll_path, get_db_path, markdown_to_text 



con = sqlite3.connect("webster.db")
cursor = con.cursor()

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
        fix_porcuppine__dll_path()  # Ensure the Porcupine DLL path is set correctly
        access_key="paste your access key here"  
        porcupine=pvporcupine.create(keywords_path=["computer","jarvis","alexa"]) 
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
            
 
 
from openai import OpenAI

client = OpenAI(
    api_key=LLM_KEY,
    base_url="https://openrouter.ai/api/v1"
)

def openai_ai(query):
    try:
        # Clean query
        query = query.replace(Assistant_Name, "")
        query = query.replace("search", "")

        response = client.chat.completions.create(
            model="deepseek/deepseek-chat",
            messages=[
                {"role": "system", "content": "You are a helpful voice assistant."},
                {"role": "user", "content": query}
            ]
        )

        answer = response.choices[0].message.content
        filter_text = markdown_to_text(answer)

        speak(filter_text)

        return filter_text  
    except Exception as e:
        print("Error in openai_ai:", e)
        speak("Sorry, I am having trouble right now.")
        return "ERROR"      


            
con = sqlite3.connect("webster.db", check_same_thread=False)
cursor = con.cursor()
con = sqlite3.connect(get_db_path())

# ---------------- ASSISTANT NAME ----------------
Assistant_Name = "My Assistant"

@eel.expose
def assistantName():
    return Assistant_Name


# ---------------- PERSONAL INFO ----------------
@eel.expose
def personalInfo():
    cursor.execute("SELECT * FROM info LIMIT 1")
    result = cursor.fetchone()

    if result:
        eel.getData(json.dumps(result))
        return 1
    else:
        print("No data found")
        return 0


@eel.expose
def updatePersonalInfo(name, designation, mobileno, email, city):
    cursor.execute("SELECT COUNT(*) FROM info")
    count = cursor.fetchone()[0]

    if count == 0:
        cursor.execute(
            "INSERT INTO info VALUES (?,?,?,?,?)",
            (name, designation, mobileno, email, city)
        )
    else:
        cursor.execute(
            "UPDATE info SET name=?, designation=?, mobileno=?, email=?, city=?",
            (name, designation, mobileno, email, city)
        )

    con.commit()
    personalInfo()
    return 1


# ---------------- SYSTEM COMMANDS ----------------
@eel.expose
def displaySysCommands():
    cursor.execute("SELECT * FROM sys_command")
    eel.displaySysCommands(json.dumps(cursor.fetchall()))
    return 1


@eel.expose
def addSysCommand(key, value):
    cursor.execute(
        "INSERT INTO sys_command (name, path) VALUES (?,?)",
        (key, value)
    )
    con.commit()


@eel.expose
def deleteSysCommand(id):
    try:
        print("Deleting sys_command id:", id, type(id))
        cursor.execute("DELETE FROM sys_command WHERE id=?", (int(id),))
        con.commit()
        return 1
    except Exception as e:
        print("Error deleting sys_command:", e)
        return 0


# ---------------- WEB COMMANDS ----------------
@eel.expose
def displayWebCommands():
    cursor.execute("SELECT * FROM web_command")
    eel.displayWebCommands(json.dumps(cursor.fetchall()))
    return 1


@eel.expose
def addWebCommand(key, value):
    cursor.execute(
        "INSERT INTO web_command (name, url) VALUES (?,?)",
        (key, value)
    )
    con.commit()


@eel.expose
def deleteWebCommand(id):
    try:
        print("Deleting web_command id:", id, type(id))
        cursor.execute("DELETE FROM web_command WHERE id=?", (int(id),))
        con.commit()
        return 1
    except Exception as e:
        print("Error deleting web_command:", e)
        return 0

# ---------------- CONTACTS ----------------
@eel.expose
def displayContacts():
    cursor.execute("SELECT * FROM contacts")
    eel.displayContacts(json.dumps(cursor.fetchall()))
    return 1


@eel.expose
def addContact(name, mobile, email, address):
    cursor.execute(
        "INSERT INTO contacts (name, mobile_no, email, address) VALUES (?,?,?,?)",
        (name, mobile, email, address)
    )
    con.commit()


@eel.expose
def deleteContact(id):
    try:
        print("Deleting contact id:", id, type(id))
        cursor.execute("DELETE FROM contacts WHERE id=?", (int(id),))
        con.commit()
        return 1
    except Exception as e:
        print("Error deleting contact:", e)
        return 0



