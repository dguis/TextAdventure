"""
Stores information about a player

Player file
(Player.py)

:author Dallin Guisti
:version 1.0 - 25 Dec 2020
:python 3.9.0

"""
from datetime import datetime


class Player:
    """
    Stores information about a player
    """

    def __init__(self):
        """
        User Information:
        Logged in : boollean
        If logged in, user id : int or None

        """
        self.choices = {}
        self.idiocy = {"typing": 0, "literacy": 0, "intelligence": 0, "life skills": 0,
                       "direction following": 0, "last idiotic event": None, "general": 0}

    def updateIdiocy(self, type, amount, event=True):
        self.idiocy[type] += amount
        self.idiocy["general"] += amount
        if self.idiocy[type] < 0:
            self.idiocy[type] = 0

        if self.idiocy["general"] < 0:
            self.idiocy["general"] = 0

        if event:
            self.idiocy["last idiotic event"] = datetime.now()

    def createLevel(self, name):
        self.choices[name] = {}

    def setKey(self, level, name, value):
        self.choices[level][name] = value

    def getIdiocy(self, category):
        delta = None
        if self.idiocy["last idiotic event"]:
            deltaobject = datetime.now() - self.idiocy["last idiotic event"]
            delta = deltaobject.total_seconds()
        return (self.idiocy[category], delta)


def main():
    myPlayer = Player()


if __name__ == "__main__":
    main()
