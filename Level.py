"""
Template for levels

Level file
(Level.py)

:author Dallin Guisti
:version 1.0 - 25 Dec 2020
:python 3.9.0

"""
from Interface import *


class Level:
    """
    Template for levels
    """

    def __init__(self):
        pass

    def execute(self, command, commands):
        exec("self." + commands[command].__name__ + "(commands)")

    def options(self, options):
        for option in options.keys():
            display(f"► {option} ||", duration=0.035)
        inputText = getInput(self.player, list(options.keys()), seed=self.seed)
        self.player.setKey("Tutorial", "insidePlane", inputText)
        self.execute(inputText, options)


def main():
    myLevel = Level()


if __name__ == "__main__":
    main()
