class Player:

    def __init__(self, display_name, id, color):
        self._display_name = display_name
        self._id = id
        self._color = color

    def getDisplayName(self):
        return self._display_name

    def getId(self):
        return self._id

    def getColor(self):
        return self._color
