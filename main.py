from random import randint
from base import busca
from entities import Environment as Environment
from entities import Vacuum as Vacuum


def create_environment():
    numberOfRooms = int(input("Enter number of rooms "))
    rooms = [False] * numberOfRooms
    x = int(input("Enter amount of dirty rooms "))
    for i in range(int(x)):
        pos = int(input("Enter position of dirt "))
        rooms[pos] = True
    env = Environment(rooms)
    return env


def manual(env: Environment):
    vacuum_pos = int(input("Choose where the vacuum will start "))
    vac = Vacuum(vacuum_pos)
    while env.is_there_dirt():
        env.print_env(vac.position)
        user_choice = input("Choose the action for the vacuum\n"
                            "c -> Clean\n"
                            "l -> go left\n"
                            "r -> go right\n"
                            "d -> detect if room is clean\n"
                            "e -> exit program")
        match user_choice:
            case 'c':
                vac.clean(env)
            case 'l':
                if vac.position > Vacuum.FIRST_POSSIBLE_POS:
                    vac.move_left()
                    print("Currently at position" + str(vac.position))
                else:
                    print("Already at first room")
            case 'r':
                if vac.position < len(env.rooms)-1:
                    vac.move_right()
                    print("Currently at position" + str(vac.position))
                else:
                    print("Already at last room")
            case 'd':
                if env.is_dirty(vac.position):
                    print("Room is dirty")
                else:
                    print("Room is clean")
            case 'e':
                exit()

    print("All rooms are clean")


def __main__():
    env = create_environment()

    while env.is_there_dirt():
        mode = input("Pick the mode: manual/base/omniscient ")
        match mode:
            case 'manual':
                manual(env)
            case 'base':
                initPos = randint(0,len(env.rooms)-1)
                vac = Vacuum(initPos)
                moves = busca(len(env.rooms), initPos)
                env.print_env(initPos)
                for move in moves:
                    if move == 'r':
                        vac.move_right()
                        if env.is_dirty(vac.position): vac.clean(env)
                        env.print_env(vac.position)
                    else:
                        vac.move_left()
                        if env.is_dirty(vac.position): vac.clean(env)
                        env.print_env(vac.position)
                break
            case 'omniscient':
                print("not implemented")
                break

    rerun = input("Rerun? (Y/N)")

    if rerun.upper() == "Y":
        __main__()


__main__()
