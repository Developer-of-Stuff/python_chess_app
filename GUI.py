from Board import Board
from PyQt6.QtWidgets import (
    QMainWindow,
    QWidget,
    QToolBar,
    QVBoxLayout,
    QGridLayout,
    QPushButton
)

BUTTON_SIZE = 100

class ChessGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Chess")
        self.generalLayout = QVBoxLayout()
        self.board = Board()
        centralWidget = QWidget(self)
        centralWidget.setLayout(self.generalLayout)
        self.setCentralWidget(centralWidget)
        self._createToolBar()
        self._createButtons()

    def _createToolBar(self):
        tools = QToolBar()
        tools.addAction("New Game")
        tools.addAction("Export PGN")
        self.addToolBar(tools)

    def _createButtons(self):
        self.buttonMap = {}
        buttonsLayout = QGridLayout()
        buttonsLayout.setHorizontalSpacing(0)
        buttonsLayout.setVerticalSpacing(0)
        for row, keys in enumerate(self.board.board):
            for col, key in enumerate(keys):
                self.buttonMap[key] = QPushButton(key.pgn_value)
                self.buttonMap[key].setFixedSize(BUTTON_SIZE, BUTTON_SIZE)
                if key.color == "dark":
                    self.buttonMap[key].setStyleSheet(
                        "background-color: #5e423b; border: none"
                    )
                else:
                    self.buttonMap[key].setStyleSheet(
                        "background-color: #B88E72; border: none"
                    )
                buttonsLayout.addWidget(self.buttonMap[key], row, col)

        self.generalLayout.addLayout(buttonsLayout)
