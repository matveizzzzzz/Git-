import sys
import random
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6 import uic
from PyQt6.QtGui import QPainter, QColor


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.draw)
        self.f = False

    def draw(self):
        self.f = True
        self.update()

    def paintEvent(self, event):
        if self.f:
            paint = QPainter(self)
            paint.setPen(QColor(255, 255, 0))
            paint.setBrush(QColor(255, 255, 0))
            d = random.randint(20, 100)
            x = random.randint(d, self.width() - d)
            y = random.randint(d, self.height() - d)
            paint.drawEllipse(x - d // 2, y - d // 2, d, d)
            self.f = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
