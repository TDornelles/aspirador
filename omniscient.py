from entities import Environment as Environment
from entities import Vacuum as Vacuum
from random import randint

def move_list_to(start: int, destination: int):
    distance = start - destination

    if(distance < 0):
        return map(lambda a : 'r', range(abs(distance)))
    else:
        return map(lambda a : 'l', range(distance))


def generate_move_list(env: Environment, vac: Vacuum):
    firstDirtyRoom = len(env.rooms) - 1
    lastDirtyRoom = 0

    firstDirtyRoom = min([firstDirtyRoom, *env.dirtyPos])
    lastDirtyRoom = max([lastDirtyRoom, *env.dirtyPos])

    firstDistance = abs(vac.position - firstDirtyRoom)
    lastDistance = abs(vac.position - lastDirtyRoom)

    firstDestination = lastDirtyRoom if firstDistance > lastDistance else firstDirtyRoom

    lastDestination = lastDirtyRoom if firstDestination == firstDirtyRoom else firstDirtyRoom

    moveToFirst = move_list_to(vac.position, firstDestination)
    moveToLast = move_list_to(firstDestination, lastDestination)

    return [*moveToFirst, *moveToLast]


def exec(env: Environment):
    initPos = randint(0,len(env.rooms)-1)
    vac = Vacuum(initPos)
    moves = generate_move_list(env, vac)

    # PRINT INITIAL STATE
    env.print_env(initPos, "")
    # IF INITIAL POSITION IS DIRTY, CLEAN AND PRINT STATE
    if env.is_dirty(vac.position):
        vac.clean(env)
        print("*Cleaned room "+str(vac.position)+"*")
        env.print_env(initPos, "")
    # ITERATE FOR ALL MOVES CALCULATED
    for move in moves:
        if move == 'r': vac.move_right()
        else: vac.move_left()
        env.print_env(vac.position, "")
        if env.is_dirty(vac.position):
            vac.clean(env)
            print("*Cleaned room "+str(vac.position)+"*")
            env.print_env(vac.position, "")