#used for multithreading 

#to run Webster
def startWebster():
        print ("Process 1 is running.")
        from main import start
        start() #function to run webster GUI
    

#to run hotword detection
def listenHowtword():
        print ("Process 2 is running.")
        from Engine.features import hotword
        hotword() #function to run hotword detection
        
        
        
if __name__ == '__main__':
        from multiprocessing import Process
        p1 = Process(target=startWebster)
        p2 = Process(target=listenHowtword)
        p1.start()
        p2.start()
        p1.join()
        
        if p2 is not None:
            p2.terminate()
            p2.join()
            
        print(*"System Shutting Down...")
        
    