"""
Generates the world

Generator file
(Generator.py)

:author Dallin Guisti
:version 1.0 - 25 Dec 2020
:python 3.9.0

"""

import random

class Generator:
    """
    Generates the world
    """
    def __init__(self, seed):
        random.seed(seed)
        print(random.random())
    
    def random(self):
        return random.random()


def main():
    myGenerator = Generator(1)

if __name__ == "__main__":
    main()