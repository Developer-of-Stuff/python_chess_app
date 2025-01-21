class Square:
    def __init__(self, file, rank, is_occupied=False):
        self.file = file
        self.rank = rank
        self.pgn_value = self.file + str(self.rank)
        self.is_occupied = is_occupied
        self.color = self._getColor()

    def _getColor(self):
        file_legend = {
            'a': 1,
            'b': 2,
            'c': 3,
            'd': 4,
            'e': 5,
            'f': 6,
            'g': 7,
            'h': 8
        }

        if file_legend[self.file] % 2 == 1:
            if self.rank % 2 == 1:
                return "dark"
            else:
                return "light"
        else:
            if self.rank % 2 == 1:
                return "light"
            else:
                return "dark"