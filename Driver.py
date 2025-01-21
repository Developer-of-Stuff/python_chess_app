import sys

from PyQt6.QtWidgets import QApplication
from GUI import ChessGUI

def main():
    chessApp = QApplication([])
    chessWindow = ChessGUI()
    chessWindow.show()
    sys.exit(chessApp.exec())

if __name__ == "__main__":
    main()