
import pyaudio
import time
import struct

import pvporcupine




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
hotword()            

