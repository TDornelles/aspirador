class Environment:
    def __init__(self, rooms, dirt):
        self.rooms = rooms
        self.dirt = dirt

    def is_dirty(self, pos):
        if pos in self.dirt:
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

