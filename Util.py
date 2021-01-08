"""
Utility class

Util file
(Util.py)

:author Dallin Guisti
:version 1.0 - 31 Dec 2020
:python 3.9.0

"""

def insert(dict, key, value, position):
    vallist = list(dict.values())
    keylist = list(dict.keys())

    vallist.insert(position, value)
    keylist.insert(position, key)

    #result = {}
    dict.clear()
    for k, v in zip(keylist,vallist):
        dict[k] = v

    #return result

if __name__ == "__main__":
    thing = {"1":1,"3":3}
    print(thing)
    thing = insert(thing,"2",2,-1)
    print(thing)