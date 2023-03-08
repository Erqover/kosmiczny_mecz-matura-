import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui

class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.hello = ["hello", "world", "hello world", "hail world!!"]

        self.button = QtWidgets.QPushButton("click me!")
        self.text = QtWidgets.QLabel("hello world!", alignment=QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)

@QtCore.Slot()
def magic(self):
    self.text.setText(random.choice(self.hello))

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())