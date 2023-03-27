class Environment:
    def __init__(self, rooms: list):
        self.rooms = rooms

    def is_dirty(self, pos: int):
        return self.rooms[pos]

    def is_there_dirt(self):
        return self.rooms.count(True) > 0
    
    def print_rooms(self, pos:int):
        top_and_bottom = ""
        mid = "|"
        for i in range(len(self.rooms)):
            top_and_bottom = top_and_bottom + "----"
            if (i==pos): mid = mid + " X |"
            else: mid = mid + "   |"
        top_and_bottom = top_and_bottom + "-"
        print(top_and_bottom)
        print(mid)
        print(top_and_bottom)


class Vacuum:
    FIRST_POSSIBLE_POS = 1

    def __init__(self, position: int):
        self.position = position

    def clean(self, env: Environment):
        if env.rooms[self.position]:
            env.rooms[self.position] = False
        else:
            print("Room already clean")

    def move_left(self):
        self.position = self.position - 1

    def move_right(self):
        self.position = self.position + 1


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
        env.print_rooms(vac.position)
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
                if vac.position < len(env.rooms):
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
                print("not implemented")
                break
            case 'omniscient':
                print("not implemented")
                break

    rerun = input("Rerun? (Y/N)")

    if rerun.upper() == "Y":
        __main__()


__main__()
