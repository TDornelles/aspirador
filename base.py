from entities import Environment as Environment
from entities import Vacuum as Vacuum
from random import randint

class Node:
    def __init__(self, moves, pos):
        self.moves = moves
        self.pos = pos
        self.checked = []

def busca(roomsize, initPos):
    solved = False
    initNode = Node([], initPos)
    initNode.checked.append(initPos)

    ## CHECK WHICH WAY IS OPTIMAL TO START
    if initPos < roomsize/2:
        initNode.moves.append('l')
        initNode.checked.append(initPos-1)
        initNode.pos = initNode.pos-1
    else:
        initNode.moves.append('r')
        initNode.checked.append(initPos+1)
        initNode.pos = initNode.pos+1

    while(not solved):

        ## CHECK IF ALREADY CHECKED ALL ROOMS
        if len(initNode.checked) == roomsize:
            solved = True
        ## IF NOT, CONTINUE MOVING
        else:
            ## CHECK LAST MOVE, TO CONTINUE MOVING IN SAME DIRECTION
            if initNode.moves[len(initNode.moves)-1] == 'l':
            
                if initNode.pos == 0:
                    initNode.moves.append('r')
                    if not initNode.checked.count(initNode.pos+1):
                        initNode.checked.append(initNode.pos+1)
                    initNode.pos = initNode.pos+1
                else:
                    initNode.moves.append('l')
                    if not initNode.checked.count(initNode.pos-1):
                        initNode.checked.append(initNode.pos-1)
                    initNode.pos = initNode.pos-1
            
            else:
                if initNode.pos == roomsize-1:
                    initNode.moves.append('l')
                    if not initNode.checked.count(initNode.pos-1):
                        initNode.checked.append(initNode.pos-1)
                    initNode.pos = initNode.pos-1
                else:
                    initNode.moves.append('r')
                    if not initNode.checked.count(initNode.pos+1):
                        initNode.checked.append(initNode.pos+1)
                    initNode.pos = initNode.pos+1

    return initNode.moves

def base(env:Environment):
    # GET RANDOM INITIAL POSITION
    initPos = randint(0,len(env.rooms)-1)
    vac = Vacuum(initPos)
    # CALCULATE OPTIMAL MOVES TO CHECK ALL ROOMS
    moves = busca(len(env.rooms), initPos)
    # PRINT INITIAL STATE
    env.print_env(initPos, "base")
    # IF INITIAL POSITION IS DIRTY, CLEAN AND PRINT STATE
    if env.is_dirty(vac.position):
        vac.clean(env)
        print("*Cleaned room "+str(vac.position)+"*")
        env.print_env(initPos, "base")
    # ITERATE FOR ALL MOVES CACLCULATED
    for move in moves:
        if move == 'r': vac.move_right()
        else: vac.move_left()
        env.print_env(vac.position, "base")
        if env.is_dirty(vac.position):
            vac.clean(env)
            print("*Cleaned room "+str(vac.position)+"*")
            env.print_env(vac.position, "base")
    # FINAL PRINT
    print("*ALL ROOMS CHECKED*\n")
            



        

