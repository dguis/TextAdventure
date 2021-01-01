"""
Ground 0: The tutorial

Tutorial file
(Tutorial.py)

:author Dallin Guisti
:version 1.0 - 30 Dec 2020
:python 3.9.0

"""

from Interface import display, getInput, displayError
from time import sleep
from Player import Player

class Tutorial:
    """
    Ground 0: The tutorial
    """
    def __init__(self, player):
        #display("Welcome to Vidas,| the text-based adventure game where YOU determine the story. ||\nThe choices you make throughout the game will affect each and every aspect of the storyline. |||") 
        #display("Your actions have consequences... |||||",duration=0.1)
        #display("\nThis tutorial level will teach you how to play the game. ||\nThe symbol \" ▷ \" is used to show when you can input a decision. ||\nAvailable options will be listed after the symbol \" ► \". ||Please input only available options. |||\n\nWhen you are ready to begin, type |\"start\": ||")
        while True:
            start = getInput("▷ ")
            if start.lower() == "start":
                display("LOL! Write the game yourself you dodo.")
                break
            else:
                displayError(player=player,mistake="typing")
                player.updateIdiocy("typing",1)
def main():
    pl = Player()
    myTutorial = Tutorial(pl)

if __name__ == "__main__":
    main()