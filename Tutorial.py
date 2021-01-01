"""
Ground 0: The tutorial

Tutorial file
(Tutorial.py)

:author Dallin Guisti
:version 1.0 - 30 Dec 2020
:python 3.9.0

"""

from time import sleep

from Interface import display, displayError, getInput
from Level import Level
from Player import Player


class Tutorial(Level):
    """
    Ground 0: The tutorial
    """

    def __init__(self, player, seed):
        self.player = player
        self.player.createLevel("Tutorial")
        self.seed = seed
        display("Welcome to Vidas,| the text-based adventure game where YOU determine the story. ||\nThe choices you make throughout the game will affect each and every aspect of the storyline. |||")
        display("Your actions have consequences<<<<<<<...<> |||||",duration=0.1)
        display("\nThis tutorial level will teach you how to play the game. ||\nThe symbol \" ▷ \" is used to show when you can input a decision. ||\nAvailable options will be listed after the symbol \" ► \". ||Please input only available options. |||\n\nWhen you are ready to begin, type |\"start\": ||")
        getInput(player,["start"], seed=self.seed)
        display("\n\nYou are jostled awake as the seat you are on seemingly falls from beneath you, |before quickly righting back up. ||\n\"Sorry for...|| turbulence...|| humidity...|| bad weather,\" ||shouts the pilot from the front of the plane, |\nbarely audible over the torrential rain and loud motors. ||\n\"Should be arriving... |shortly,\" |you manage to hear as well. ||\nYou wonder what on earth is going on. ||You can’t seem to remember where you are going, |what you are doing, |or even who you are. |||||\nWhat do you want to do? ||")
        insidePlane = {
            "Ask the pilot where you're going": self.say_whereGoing,
            "Ask the pilot what you're doing": self.say_whatDoing,
            "Ask the pilot who you are": self.say_whoSelf,
            "Ask the pilot who he is": self.action_whoPilot,
            "Look around": self.action_lookAround,
            "Wait patiently": self.action_wait,
        }
        while True:
            self.options(insidePlane)
            display("What next? ||")

    def say_whereGoing(self,commands):
        display("You ask the pilot |\"Where are we going?\" ||\nThrough the whipping whirlwind and the patter of the rain on the roof, |he doesn’t seem to understand you very well. ||\nYou manage to make out: |||\n\"Where... ||the Boeing? ||Nah this pretty lady is... ||a Cessna. ||She'll fly ya... ||jungle and back... ||in no time.\" |||||")
        del commands["Ask the pilot where you're going"]
        return
    def say_whatDoing(self, commands):
        display("You ask the pilot “What are we doing?” There’s a sudden break in the downpour, and you for once you can clearly hear his answer. “What are we doing? How could ya forget! You’re journeyin’ to find the Lost Temple of Vidas.”")
    def say_whoSelf(self, commands):
        display("You ask the pilot “Who am I?” Just as you ask, a bolt of lightning cracks across the sky, making your ears ring. You can see the pilot’s lips moving but you can’t make out anything he says…")
    def action_whoPilot(self, commands):
        display("You ask the pilot “Who are you?” He looks back at you quickly, and yells, “Why, I’m Sam.. McGee, the best… pilot in all of… pacific!”")
    def action_lookAround(self, commands):
        display("You attempt to look around. As you begin to unbuckle your seatbelt, you are jerked back by another wave of turbulence. You realize that getting up is probably not the best idea right now…")
    def action_wait(self, commands):
        pass
def main():
    pl = Player()
    myTutorial = Tutorial(pl, 0)


if __name__ == "__main__":
    main()
