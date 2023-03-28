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



        

