"""
Game updater

Update file
(Update.py)

:author Dallin Guisti
:version 1.0 - 24 Dec 2020
:python 3.9.0

"""

import os
import wget

class Update:
    def __init__(self):
        print("Update engine started.")
        print("Initializing game update...")
        files = [".env","Database.py","Main.py","Menu.py"]

        dir = os.getcwd()
        for file in files:
            if os.path.exists(dir+"/"+file):
                os.remove(dir+"/"+file)
            try:
                wget.download("https://raw.githubusercontent.com/dguis/TextAdventure/master/" + file, bar=None)
            except:
                print(f"Error downloading file '{file}''. PLease try again later.")
                return

def main():
    myUpdate = Update()

if __name__ == "__main__":
    main()