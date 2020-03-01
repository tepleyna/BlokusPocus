class Piece:

    def __init__(self, shape):
        self.shape = shape

    def pretty_print(self):
        for line in self.shape:
            out = ""
            for c in line:
                out += "x" if c == "x" else "_"
            print(out)
