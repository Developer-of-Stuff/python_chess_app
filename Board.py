from Square import Square

class Board:
    def __init__(self):
        self.board = self._generateBoardLayout()

    def _generateBoardLayout(self):
        board = []
        files = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        for file in files:
            rank = []
            for i in range(1, 9):
                rank.append(Square(file, i))
            board.append(rank)
        return board
                
