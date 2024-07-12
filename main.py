from PyQt6 import QtCore, QtGui, QtWidgets
import sys

from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QTextEdit,
    QPushButton,
    QVBoxLayout,
    QFileDialog
)

from Project import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())