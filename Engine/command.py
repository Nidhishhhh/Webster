import pyttsx3
import speech_recognition as sr
import eel
import time

def speak(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 174)
    eel.DisplayMessage(text)
    engine.say(text)
    eel.receiverText(text)
    engine.runAndWait()
    

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        eel.DisplayMessage("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, 10, 6)
        
    try:
        print("Recognizing...")
        eel.DisplayMessage("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        eel.DisplayMessage(query)
        
        
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query.lower()

@eel.expose 
def allCommands(message=1):
    
    
    if message == 1:
        query = takecommand()
        print(query)
        eel.senderText(query)
    else:
        query = message
        eel.senderText(query)
        
    try:  
        if "open" in query:
            from Engine.features import openCommand
            openCommand(query)
    
        elif "on YouTube":
            from Engine.features import PlayYoutube
            PlayYoutube(query)
        else:
            print("No Command Found...")

    except:
        print("error")
        
        
        
    time.sleep(2)
    eel.ShowHood()
    
    


