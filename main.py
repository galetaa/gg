from PyQt5.QtWidgets import QApplication, QWidget
from PIL.ImageQt import ImageQt
from PyQt5.QtGui import QPixmap
from PIL import Image, ImageDraw
from random import randint
from PyQt5 import QtCore
import sys, PyQt5


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 300)
        self.horizontalLayout = PyQt5.QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = PyQt5.QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = PyQt5.QtWidgets.QLabel(Form)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.pushButton = PyQt5.QtWidgets.QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton)

        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(Form)

        PyQt5.QtCore.QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(PyQt5.QtCore.QCoreApplication.translate("Form", u"Form", None))
        self.label.setText("")
        self.pushButton.setText(PyQt5.QtCore.QCoreApplication.translate("Form", u"run", None))
    # retranslateUi


class MyWidget(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
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
            draw.ellipse(((x, y), (x + d, y + d)), (randint(1, 255), randint(1, 255), randint(1, 255)))
        self.imqt = ImageQt(self.im)
        self.pixmap = QPixmap.fromImage(self.imqt)
        self.label.setPixmap(self.pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
