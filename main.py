import array


class Environment:
    def __init__(self, rooms, dirt):
        self.rooms: int = int(rooms)
        self.dirt: array = dirt

    def is_dirty(self, pos):
        if pos in self.dirt:
            return True
        return False

    def is_there_dirt(self):
        if len(self.dirt) > 0:
            return True
        return False


class Vacuum:
    FIRST_POSSIBLE_POS = 1

    def __init__(self, position):
        self.position: int = int(position)

    def clean(self, env):
        if self.position in env.dirt:
            env.dirt.remove(self.position)
        else:
            print("Room already clean")

    def move_left(self):
        self.position = int(self.position) - 1

    def move_right(self):
        self.position = int(self.position) + 1


def create_environment():
    rooms = input("Enter number of rooms")
    x = input("Enter amount of dirty rooms")
    dirt = []
    for i in range(int(x)):
        pos = int(input("Enter position of dirt"))
        dirt.append(pos)
    env = Environment(rooms, dirt)
    return env


def manual(env: Environment):
    vacuum_pos = input("Choose where the vacuum will start")
    vac = Vacuum(vacuum_pos)
    while env.is_there_dirt():
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
                if vac.position < env.rooms:
                    vac.move_right()
                    print("Currently at position" + str(vac.position))
                else:
                    print("Already at last room")
            case 'd':
                if env.is_dirty(vac.position):
                    print("Room is dirty")
                else:
                    print("Room is not dirty")
            case 'e':
                exit()

    print("All rooms are clean")


def __main__():
    env = create_environment()

    while env.is_there_dirt():
        mode = input("Pick the mode: manual/base/omniscient")
        match mode:
            case 'manual':
                manual(env)
            case 'base':
                print("not implemented")
                break
            case 'omniscient':
                print("not implemented")
                break

    rerun = input("Rerun? (Y/N)")

    if rerun.upper() == "Y":
        __main__()


__main__()
