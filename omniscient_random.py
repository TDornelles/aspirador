from entities import Environment as Environment
from entities import Vacuum as Vacuum
from random import randint


def find_nearest(pos,env:Environment):
    nearest = 100
    i = 0
    for room in env.rooms:
        if room and abs(pos-i)<abs(pos-nearest): nearest = i
        i = i+1
    
    return nearest

def exec(env: Environment):
    initPos = randint(0,len(env.rooms)-1)
    vac = Vacuum(initPos)

    # PRINT INITIAL STATE
    env.print_env(initPos, "")
    while(env.is_there_dirt()):
        if env.is_dirty(vac.position):
            vac.clean(env)
            print("*Cleaned room "+str(vac.position)+"*")
            env.print_env(vac.position, "")
        else:
            nearest = find_nearest(vac.position, env)
            vac.move_left() if nearest < vac.position else vac.move_right()
            env.print_env(vac.position,"")
            # CALCULATE CHANCE TO SPAWN DIRT
            roll = randint(0,9)
            if roll<4:
                randDirt = randint(0,len(env.rooms)-1)

                while env.rooms[randDirt] == True:
                    randDirt = randint(0,len(env.rooms)-1)
                env.rooms[randDirt] = True
                print("** ANOTHER DIRT HAS APPEARED!! **")
        
