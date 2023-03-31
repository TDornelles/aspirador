from entities import Environment as Environment
from entities import Vacuum as Vacuum

def manual(env: Environment):
    vacuum_pos = int(input("Choose where the vacuum will start "))
    vac = Vacuum(vacuum_pos)
    while env.is_there_dirt():
        env.print_env(vac.position, "manual")
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