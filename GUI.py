from PyQt6.QtWidgets import (
    QMainWindow
)

class ChessGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        print("GUI Initialized")