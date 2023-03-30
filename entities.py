class Environment:
    def __init__(self, rooms: list):
        self.rooms = rooms

    def is_dirty(self, pos: int):
        return self.rooms[pos]

    def is_there_dirt(self):
        return self.rooms.count(True) > 0
    
    def print_env(self, pos:int):
        mold = "-----------------"
        top= "| ROOM\t\t|"
        mid = "| VACUUM\t|"
        bottom = "| DIRT\t\t|"
        for i in range(len(self.rooms)):
            mold = mold + "-----"
            if i<10: top = top + "  "+str(i)+" |"
            else: top = top + " "+str(i)+" |"
            if (self.rooms[i]): bottom = bottom + "  X |"
            else: bottom = bottom + "    |"
            if (i==pos): mid = mid + "  X |"
            else: mid = mid + "    |"
        print(mold)
        print(top)
        print(mid)
        print(bottom)
        print(mold)
        print("\n")

class Vacuum:
    FIRST_POSSIBLE_POS = 0

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