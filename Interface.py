"""
Terminal interface for the game

Interface file
(Interface.py)

:author Dallin Guisti
:version 1.0 - 30 Dec 2020
:python 3.9.0

"""

import time
from random import choice

def display(text, end="\n", duration=0.05, waittime=0.1, delta=0.01):
    special = ["|","<", ">"]
    span = duration
    for index, character in enumerate(text):
        if span < 0:
            span = 0
        if character == "\\" and text[index + 1] in special:
            continue
        elif character == "|" and text[index-1] != "\\":
            time.sleep(waittime)
        elif character == "<" and text[index-1] != "\\" and text[index+1] == ">":
            span = duration
        elif character == "<" and text[index-1] != "\\":
            span += delta
        elif character == ">" and text[index-1] != "\\":
            span -= delta
        else:
            print(character,end="",flush=True)
            time.sleep(span)
    print("",end=end)
def displayError(player=None,mistake=None,kind=False):
    if player and mistake:
        if mistake == "typing":
            secondspassed = player.getIdiocy("typing")[1]
            minutecooldown = 10
            if secondspassed:
                for group in range(secondspassed//(minutecooldown*60)):
                    player.updateIdiocy("last idiotic event",-minutecooldown*60,event=False)
                    player.updateIdiocy("typing",-1,event=False)
            anger = player.getIdiocy("typing")[0] - secondspassed//30
            if anger < 5 or kind:
                options = [
                    "Uh oh, |it seems like you might have mistyped something. ||Please enter a valid input.",
                    "Uh oh|.|.|.||it looks like you have a typo. ||Please try again.",
                    "That just won't quite work. ||Please enter a valid option.",
                    "Your input seems just a bit off. ||Try inputting something else.",
                    "Input error. ||Next time, |try inputting one of the suggested options.",
                    "Whoops! ||It seems you've inputted something invalid. ||Try again.",
                    "The input you have written is invalid. ||Please try again.",
                    "Oh no! ||It looks like the value you inputted is not an available option. ||Write something else.",
                    "The above input is not an available command. ||Please input a different, valid command.",
                    "Your input value does not match the list of commands. Try using a different command."
                ]
            elif anger < 10 :
                options = [
                    "Man, |you are kinda bad at this. ||Try entering something valid this time.",
                    "Your inputs have consistently been invalid. ||Are you <<<trying>>> to get this wrong?",
                    "Can't you just choose a valid input? ||There's a list of valid options, |yet you've managed to ignore all of them.",
                    "Come <<on>>. ||It's not that hard to pick one of the commands listed. ||Just do it already.",
                    "Did you see that list of available commands? ||Try typing one of those instead of <this> nonsense.",
                    "Really? <How> many <<<times>>> do I need to say it? |Just choose a valid input already!",
                    "Seriously, |I'm disappointed. ||How hard is it to type something you can already see?",
                    "If you are really struggling, |you could select the command you want, ||press CTRL+C, ||go back to the input line, ||and press CTRL+V.",
                    "Do you need to go back to typing class?",
                    "If you'd like to improve your typing abilites, |try using this website: ||https://www.keybr.com/"
                ]
            elif anger < 20:
                options = [
                    "THAT'S ENOUGH! ||I mean come on. ||<<<COME ON>>>! |||||One time? |Okay. ||Five times? |Sure. ||Ten? ||Ehhh.... |||\nBUT TWENTY?! |||<<<<<<<TWENTY>>>>>>>???!!! ||For the LAST time, |please input something <<<VALID>>>."
                ]
            else:
                options = [
                    "I hate you.",
                    "I've had enough of this nonsense. I didn't make this program for you to just "
                ]
        display(choice(options) + " ||",duration=0.04)
        return
def getInput(prompt):
    display(prompt + " ",end="")
    return input("")
