from copy import deepcopy

class Piece:

    def __init__(self, shape, id):
        self._shape = shape
        self._id = id

    def prettyPrint(self):
        print(self.shapeAsText())

    def rotate(self, isClockwise):
        # 1. transpose
        # 2. if clockwise,
        #.    A. flip in the Y
        #.    B. else flip by X
        self._transpose()
        return self.flip(not isClockwise)

    def flip(self, isX):
        if isX:
            self._shape.reverse()
        else:
            for outer_index in range(len(self._shape)):
                self._shape[outer_index].reverse()
        return self.getShape()

    def getShape(self):
        return deepcopy(self._shape)

    def getId(self):
        return self._id

    def getShapeText(self):
        return ("\n").join(
            ( ("").join(line) ) for line in self._shape)

    def _transpose(self):
        self._shape = [[self._shape[x][y] for x in range(len(self._shape))]
         for y in range(len(self._shape[0]))]


def allShapes():
    return ([
    [ ['x'] ] ,     # 1
    [ ['x', 'x']],

    [ ['x','x','x']], # 3
    [ ['x','x'],
        ['x','o']],

    [ ['x','x','x','x']], # 5
    [ ['x','x','x'],
        ['x','o','o']],
    [ ['o','x','o'],
        ['x','x','x']],
    [ ['x','x'],
        ['x','x']],
    [ ['o','x'],
        ['x','x'],
        ['x','o']],

    [ ['x','x','x','x','x']], #10
    [ ['x','x','x'],
        ['x','o','o'],
        ['x','o','o']],
    [ ['x','x','x','x'],
        ['o','o','x','o']],
    [ ['x','x','x','x'],
        ['o','o','o','x']], # 13
    [ ['o','x','x'],
        ['x','x','o'],
        ['x','o','o']],
    [ ['o','x','o'],
        ['x','x','x'],
        ['o','x','o']],
    [ ['x','x','x','o'],
        ['o','o','x','x']],
    [ ['o','x','x'],
        ['o','x','o'],
        ['x','x','o']], #17
    [ ['o','x','x'],
        ['x','x','o'],
        ['o','x','o']],
    [ ['x','x','x'],
        ['o','x','o'],
        ['o','x','o']],
    [ ['o','x','x'],
        ['o','o','x'],
        ['o','x','x']],
    [ ['x','x','x'],
        ['x','x','o']] #21
    ])
