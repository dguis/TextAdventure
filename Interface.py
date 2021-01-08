"""
Terminal interface for the game

Interface file
(Interface.py)

:author Dallin Guisti
:version 1.0 - 30 Dec 2020
:python 3.9.0

"""

import time
from random import choice, Random


def display(text, end="\n", duration=0.05, waittime=0.1, delta=0.01):
    special = ["|", "<", ">"]
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
            time.sleep(span)
            print(character, end="", flush=True)
    print("", end=end)

def displayError(player=None, mistake=None, kind=False, r=None):
    if player and mistake:
        if mistake == "typing":
            secondspassed = player.getIdiocy("typing")[1]
            minutecooldown = 10
            if secondspassed:
                for group in range(int(secondspassed//(minutecooldown*60))):
                    player.updateIdiocy(
                        "last idiotic event", -minutecooldown*60, event=False)
                    player.updateIdiocy("typing", -1, event=False)
                anger = player.getIdiocy("typing")[0] - secondspassed//30
            else:
                anger = 0
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
            elif anger < 10:
                options = [
                    "Man, |you are kinda bad at this. ||Try entering something valid this time.",
                    "Your inputs have consistently been invalid. ||Are you <<<trying>>> to get this wrong?",
                    "Can't you just choose a valid input? ||There's a list of valid options, |yet you've managed to ignore all of them.",
                    "Come <<<<<<<<on<>. ||It's not that hard to pick one of the commands listed. ||Just do it already.",
                    "Did you see that list of available commands? ||Try typing one of those instead of <this> nonsense.",
                    "Really? <How> many <<<times>>> do I need to say it? |Just choose a valid input already!",
                    "Seriously, |I'm disappointed. ||How hard is it to type something you can already see?",
                    "If you are really struggling, |you could select the command you want, ||press CTRL+C, ||go back to the input line, ||and press CTRL+V.",
                    "Do you need to go back to typing class?",
                    "If you'd like to improve your typing abilites, |try using this website: ||https://www.keybr.com/"
                ]
            elif anger < 20:
                options = [
                    "Input more angry error messages here.",
                    "You"
                ]
            else:
                options = [
                    "THAT'S ENOUGH! ||I mean come on. ||<<<COME ON>>>! |||||One time? |Okay. ||Five times? |Sure. ||Ten? ||Ehhh.... |||\nBUT TWENTY?! |||<<<<<<<TWENTY>>>>>>>???!!! ||For the LAST time, |please input something <<<VALID>>>."
                    "<<<<<<<<<<<<<<I hate you.",
                    "I've had enough of this <<nonsense>>. ||I didn't make this program for you to just input whatever you want. ||Just pick an option already.",
                    "<<<<<<<<<<<<<<<<<<<<STOP",
                    "<<<<<Just stop already.",
                    "<<<<<<Goodbye."
                ]
        if r:
            optionPicked = r.choice(options)
        else:
            optionPicked = choice(options)

        display(optionPicked + " ||", duration=0.035)
        if optionPicked == "<<<<<<Goodbye.":
            quit()
        return

    display("The input you have written is invalid. ||Please try again. ||")


def getInput(player, valid, kind=False, r=None):
    while True:
        display("▷ ", end="")
        start = input("")
        loweredValid = [y.lower() for y in valid]
        if start.lower() in loweredValid:
            return valid[loweredValid.index(start)]
        else:
            try:
                if int(start) <= len(valid) and int(start) > 0:
                    return valid[int(start)-1]
            except:
                pass
        displayError(player=player, mistake="typing", kind=kind, r=r)
        if player:
            player.updateIdiocy("typing", 1)
