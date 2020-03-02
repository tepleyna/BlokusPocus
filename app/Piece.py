from copy import deepcopy

class Piece:

    def __init__(self, shape, id):
        self._shape = shape
        self._id = id

    def getShape(self):
        return deepcopy(self._shape)

    def getId(self):
        return self._id

    def prettyPrint(self):
        print(self.shapeAsText())

    def getShapeText(self):
        return ("\n").join(
            ( ("").join(line) ) for line in self._shape)


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
