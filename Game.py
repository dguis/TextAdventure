"""
Main game file

Game file
(Game.py)

:author Dallin Guisti
:version 1.0 - 25 Dec 2020
:python 3.9.0

"""

from Tutorial import Tutorial
from Player import Player
from random import randint


class Game:
    """
    Main game class
    """

    def __init__(self, pl, seed):
        Tutorial(pl, seed)


def main():
    seed = 0  # randint(5615646546546,8789465498498496549849684)
    pl = Player()
    myGame = Game(pl, seed)


if __name__ == "__main__":
    main()
