import os
os.system("python -m pip install wget -q")
import wget
print("Downloading dependencies...")
try:
    wget.download("https://raw.githubusercontent.com/dguis/TextAdventure/master/requirements.txt",bar=None)
except:
    print("Error. Failed to resolve dependency file. Please try again later.")
    quit()
os.system("python -m pip install -r requirements.txt -q")
print("Dependencies installed.")
import wget
import urllib.request

def checkConnection(self):
    try:
        urllib.request.urlopen("https://github.com") #Python 3.x
        return True
    except:
        return False

if not checkConnection():
    print("Error. Internet connection failed. Please try again later.")
    quit()
dir = os.getcwd()
if os.path.exists(dir+"/Update.py"):
    os.remove(dir+"/Update.py")
print("Downloading update engine...")
try:
    wget.download("https://raw.githubusercontent.com/dguis/TextAdventure/master/Update.py",bar=None)
except:
    print("Error downloading upload engine. PLease try again later.")
    quit()
print("Update engine downloaded succesfully. Update engine starting...")
os.system(f"python {dir}/Update.py")