"""
Ground 1: Into the Jungle

Level1 file
(Tutorial1.py)

:author Dallin Guisti
:version 1.0 - 30 Dec 2020
:python 3.9.0

"""

from time import sleep

from random import Random

from Interface import display, displayError, getInput
from Level import Level
from Player import Player

from Util import insert


class Wait(Exception):
    pass

class GetUp(Exception):
    pass

class Ground1(Level):
    """
    Ground 0: The tutorial
    """

    def __init__(self, player, r):
        self.player = player
        self.player.createLevel("Tutorial")
        self.r = r
        #display("Welcome to Vidas, |the text-based adventure game where YOU determine the story. ||\nThe choices you make throughout the game will affect each and every aspect of the storyline. |||")
        #display("Your actions have consequences<<<<<<<<<<<<<<<<<<<<<... <>||||||||||",duration=0.1)
        #display("\nThis tutorial level will teach you how to play the game. ||\nThe symbol \" ▷ \" is used to show when you can input a decision. ||\nAvailable options will be listed after the symbol \" ► \". ||Please input only available options. |||\n\nWhen you are ready to begin, type |\"start\": ||")
        #getInput(player,["start"], seed=self.seed)
        display("\n< » GROUND 0:|| TUTORIAL « |||||")
        #display("\n\nYou are jostled awake as the seat you are on seemingly falls from beneath you, |before quickly righting back up. ||\n\"Sorry for...|| turbulence...|| humidity...|| bad weather,\" ||shouts the pilot from the front of the plane, |\nbarely audible over the torrential rain and loud motors. ||\n\"Should be arriving... |shortly,\" |you manage to hear as well. ||\nYou wonder what on earth is going on. ||You can't seem to remember where you are going, |what you are doing, |or even who you are. |||||\nWhat do you want to do? |||||")
        insidePlane = {
            "Ask the pilot where you're going": self.say_whereGoing,
            "Ask the pilot what you're doing": self.say_whatDoing,
            "Ask the pilot who you are": self.say_whoSelf,
            "Ask the pilot who he is": self.action_whoPilot,
            "Look around": self.action_lookAround,
            "Wait patiently": self.action_wait,
        }
        totalOptions = self.r.randint(2,4)
        ending = "normal"
        for optionCount in range(totalOptions):
            try:
                self.options(insidePlane)
            except Wait:
                break
            except GetUp:
                ending = "unconscious"
                break
            if optionCount < totalOptions: display("\nWhat next? ||")
        if ending == "unconscious":
            display("\n<<You awaken again as you land with a thud onto moss-covered ground. ||>The sounds of birds calling and critters buzzing fill your ears. ||\n\n>As you open your eyes, |you see a lush green landscape filled with countless varieties of flora. ||Dew rests on the leaves of the plants around you. ||\n\nSuddenly, |your attention is drawn to the sound of a rotor whirring to life. ||")
            display("The plane you vaguely remember flying in on starts to drift away from you down a nearby river. ||\nYou try to shout at the pilot, |but the roar of the engine is too loud for you to even hear yourself. ||\nThe plane takes off, |leaving you behind in the jungle... ||||||||||")
        else:
            display("\nA large crack of lighting resonates from the sky, |and the rain seems to pour down even harder. ||\n\"Weather... ||worse... ||need to land... ||a few miles out... ||you'll have to hike... ||get there,\" ||you hear the pilot say. ||\nHe yanks on the controls, |and the plane begins to descend. ||\n\nAs you lower out of the storm clouds, the area below you begins to materialize. ||")
            display("A lush jungle canopy stretches as far as the eye can see. ||The pilot points to a section of a river up ahead, |and starts to descend further. |||||")
            display("You land on the water with a slight jolt, |and the pilot guides the aircraft towards the water's edge. ||He kills the engine and opens the rear door. ||||\n\nAs you step outside, |the sounds of birds calling and critters buzzing fill your ears. ||\nThe lush green landscape you saw from above is just as beautiful on the ground: ||countless varieties of flora make up the dense jungle. ||")
            display("Dew rests on the leaves of the plants around you. ||Suddenly, |you hear a door slam behind you. ||\n\nAs you look back at the seaplane, |you see the rear door has shut, |and the pilot has started the engine back up. ||\nYou try to shout to stop him, |but the roar of the engine is too loud for you to even hear yourself. ||\nYou run towards the plane, |desperate to grab onto something, |but it floats away and takes off before you can reach it, |\n<<leaving you behind in the jungle<<<<<<<<<<<<<<<... ||||||||||")

        display("\n< » GROUND 0:|| TUTORIAL ||— |<<COMPLETE « |||||")

    def say_whereGoing(self,commands):
        display("You ask the pilot |\"Where are we going?\" ||\nThrough the whipping whirlwind and the patter of the rain on the roof, |he doesn't seem to understand you very well. ||\nYou manage to make out: |||\n\"Where... ||the Boeing? ||Nah this pretty lady... ||a Cessna. ||She'll fly ya... ||jungle and back... ||no time.\" |||||")
        del commands["Ask the pilot where you're going"]
        return
    def say_whatDoing(self, commands):
        display("You ask the pilot |\"What are we doing?\" ||There's a sudden break in the downpour, |and for once you can clearly hear his answer. |||\n\"What are we doing? ||How could ya forget! ||You're journeyin' to find the Lost Temple of Vidas of course!\" |||||")
        del commands["Ask the pilot what you're doing"]
        return
    def say_whoSelf(self, commands):
        display("You ask the pilot |\"Who am I?\" ||Just as you ask, |a bolt of lightning cracks across the sky, |making your ears ring. ||\nYou can see the pilot's lips moving, |but you can't make out anything he says... |||||")
        del commands["Ask the pilot who you are"]
        return
    def action_whoPilot(self, commands):
        display("You ask the pilot |\"Who are you?\" |||He looks back at you quickly and yells, ||\n\"Why, |I'm Sam... ||McGee, |the best... ||pilot in all of... ||pacific!\" |||||")
        del commands["Ask the pilot who he is"]
        return
    def action_lookAround(self, commands):
        display("You attempt to look around. ||As you begin to unbuckle your seatbelt, |you are jerked back by another wave of turbulence. ||\nYou realize getting up is probably not the best idea right now... |||||")
        del commands["Look around"]
        insert(commands,"Get up anyway",self.action_getUp,4)
        return
    def action_getUp(self,commands):
        display("You get up anyway. ||You look around for a few moments, |but don't see much of interest. ||The plane is, |for the most part, |empty. ||\nHowever, |one thing stands out: ||you see a gun sitting on the back seat, |a box of bullets next to it. ||\nBefore you can do anything, |the plane bounces again and you get flung backwards. \n||Your head hits the wall|| and you pass out... ||||||||||")
        raise GetUp
    def action_wait(self, commands):
        display("You decide to wait patiently in your seat until you land before doing anything else. ||||||||||")
        raise Wait
def main():
    pl = Player()
    myTutorial = Ground1(pl, Random(0))


if __name__ == "__main__":
    main()
