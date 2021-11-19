from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget
from PIL.ImageQt import ImageQt
from PyQt5.QtGui import QPixmap
from PIL import Image, ImageDraw
from random import randint
import sys


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.label.hide()
        self.pushButton.clicked.connect(self.run)

    def run(self):
        self.label.show()
        self.im = Image.new("RGB", (500, 500), (255, 255, 255))
        draw = ImageDraw.Draw(self.im)
        for i in range(randint(2, 10)):
            d = randint(10, 300)
            x = randint(0, 500)
            y = randint(0, 500)
            draw.ellipse(((x, y), (x + d, y + d)), (255, 211, 0))
        self.imqt = ImageQt(self.im)
        self.pixmap = QPixmap.fromImage(self.imqt)
        self.label.setPixmap(self.pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
