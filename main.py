from entities import Environment as Environment
from entities import Vacuum as Vacuum
from random import randint
import base
import manual
import omniscient


def create_environment(mode):
    numberOfRooms = int(input("Enter number of rooms: "))
    rooms = [False] * numberOfRooms
    x = int(input("Enter amount of dirty rooms: "))
    
    dirtyPos = []
    for i in range(int(x)):
        newDirtyPos = randint(0,numberOfRooms-1)
        while (dirtyPos.count(newDirtyPos)): newDirtyPos = randint(0,numberOfRooms-1)
        rooms[newDirtyPos] = True
        dirtyPos.append(newDirtyPos)

    env = Environment(rooms, dirtyPos)
    return env



def __main__():
    mode = input("Pick the mode: manual/base/omniscient ")
    env = create_environment(mode)

    while env.is_there_dirt():
        match mode:
            case 'manual':
                manual.manual(env)
            case 'base':
                base.base(env)
            case 'omniscient':
                omniscient.exec(env)
                break

    rerun = input("Rerun? (Y/N)")

    if rerun.upper() == "Y":
        __main__()


__main__()
