class Environment:
    def __init__(self, rooms, dirt):
        self.rooms = rooms
        self.dirt = dirt

    def is_dirty(self, pos):
        if pos in self.dirt:
            return True
        return False

    def is_there_dirt(self):
        if len(self.dirt) > 0:
            return True
        return False


class Vacuum:
    def __init__(self, position, orientation):
        self.position = position

    def clean(self, env):
        if self.position in env.dirt:
            env.dirt.remove(self.position)
        else:
            print("Room already clean")

    def move_left(self):
        self.position -= 1

    def move_right(self):
        self.position += 1


def create_environment():
    rooms = input("Enter number of rooms")
    x = input("Enter amount of dirty rooms")
    dirt = []
    for i in x:
        pos = input("Enter position of dirt")
        dirt.append(pos)
    env = Environment(rooms, dirt)
    return env


def manual():
    user_choice = input("Choose the action for the vacuum\n"
                        "c -> Clean\n"
                        "l -> go left\n"
                        "r -> go right\n"
                        "d -> detect if room is clean\n"
                        "e -> exit program")


def __main__():
    env = create_environment()

    while env.is_there_dirt():
        mode = input("Pick the mode: manual/base/omniscient")
        match mode:
            case 'manual':
                manual()
            case 'base':
                print("not implemented")
                break
            case 'omniscient':
                print("not implemented")
                break

    rerun = input("Rerun? (Y/N)")

    if rerun:
        __main__()