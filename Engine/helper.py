from email.mime import base
import os
import re
import shutil
import sys
import threading
import markdown2

from bs4 import BeautifulSoup


def extract_yt_term(command):
    pattern = r'play\s+(.*?)\s+on\s+youtube'  #here play is a constant term, (.+?) is a dynamic term and on youtube is again a constant term.
    match = re.search(pattern, command, re.IGNORECASE) #here we have imported re(REGULAR EXPRESSION) module to pass the qury. re.IGNORECASE is used to ignore the capital and small letters.
    return match.group(1) if match else None #match.group is used to search the dynamic term in the query. If no match is found, it returns None.



def markdown_to_text(md):
    html = markdown2.markdown(md)
    soup = BeautifulSoup(html, "html.parser")
    return soup.get_text().strip()


def recource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    if hasattr(sys,"_MEIPASS_"):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


DB_NAME = "webster.db"
_lock = threading.Lock()
_connection = None

def get_db_path():
    base_dir = os.path.join(
        os.path.expanduser("~"),
        "Documents",
        "WebsterAssistant"
    )
    os.makedirs
    
    db_path = os.path.join(base_dir, DB_NAME)
    
    if not os.path.exists(db_path):
        with _lock:
            if not os.path.exists(db_path):
                if hasattr(sys, "_MEIPASS"):
                    source_db_path = os.path.join(sys._MEIPASS, DB_NAME)
                else:
                    source_db_path = os.path.join(os.path.abspath("."), DB_NAME)
                    
                if not os.path.exists(source_db_path):
                    raise FileNotFoundError(f"Source database not found at {source_db_path}")
                
                shutil.copy2(source_db_path, db_path)
                
    return db_path

def fix_porcuppine__dll_path():
    if hasattr(sys, "_MEIPASS"):
        dll_path = os.path.join(sys._MEIPASS, "pvporcupine", "lib", "windows", "x86_64", "pv_porcupine.dll", "amd64") 
        os.environ["PATH"] += os.pathsep + dll_path
        print("Porcupine DLL path added to PATH environment variable:", dll_path)
