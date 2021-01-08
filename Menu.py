"""
Simple text-based menu for the game

Menu file
(Menu.py)

:author Dallin Guisti
:version 1.0 - 24 Dec 2020
:python 3.9.0

"""

import time
import os
import urllib.request
import wget
from Interface import display, getInput
from Game import Game
from Player import Player
from random import Random


class Menu:
    def __init__(self):
        self.player = Player()
        self.seed = 0
        self.r = Random(self.seed)
        print("\t\t\t\t╔═════════════╗")
        print("\t\t\t\t║  ＶＩＤＡＳ ║")
        print("\t\t\t\t╚═════════════╝")

        display(
            "Please enter a command, or type help to see a list of available commands...")
        self.commands = {
            "help": [self.help, "Help", "Lists available commands"],
            "start": [self.start, "Start", "Starts the game"],
            "quit": [self.quit, "Quit", "Quits the game"],
            "login": [self.login, "Login (Not implemented)", "Login to preexisting account"],
            "signup": [self.signup, "Signup (Not implemented)", "Signup for a TextAdventure account"],
            "settings": [self.settings, "Settings (not implemented)", "View game settings menu"],
            "update": [self.update, "Update", "Update the game (internet connection required)"]
        }
        while True:
            cmd = getInput(self.player, self.commands.keys(), r=self.r)
            self.procCommand(cmd)

    def procCommand(self, cmd):
        if cmd in self.commands:
            exec("self." + self.commands[cmd][0].__name__ + "()")
        else:
            display("Please input a valid command.")

    def help(self):
        display("Currently available commands:")
        for command, command_name, command_desc in self.commands.values():
            display(f"   ► {command_name} - {command_desc}",duration=0.03)

    def start(self):
        Game(self.player, self.r)

    def quit(self):
        display("Thanks for playing!")
        quit()

    def login(self):
        display("Sorry, the account feature is still in progress!")

    def signup(self):
        display("Sorry, the account feature is still in progress!")

    def settings(self):
        pass

    def update(self):
        if not self.checkConnection():
            display("Error. Internet connection failed. Please try again later.")
            return
        dir = os.getcwd()
        if os.path.exists(dir+"/Update.py"):
            os.remove(dir+"/Update.py")
        print("Downloading update engine...")
        try:
            wget.download(
                "https://raw.githubusercontent.com/dguis/TextAdventure/master/Update.py", bar=None)
        except:
            print("Error downloading upload engine. PLease try again later.")
            return
        print("Update engine downloaded succesfully. Update engine starting...")
        os.system(f"python {dir}/Update.py")
        quit()

    def checkConnection(self):
        try:
            urllib.request.urlopen("https://github.com")  # Python 3.x
            return True
        except:
            return False


def main():
    myMenu = Menu()


if __name__ == "__main__":
    main()
