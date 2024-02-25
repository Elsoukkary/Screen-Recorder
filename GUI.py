from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
import sys


class Ui_Win():
    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)

        self.Win = QtWidgets.QWidget()
        self.Win.setObjectName("Win")
        self.Win.setWindowFlag(Qt.FramelessWindowHint)
        self.Win.resize(148, 51)
        self.Win.setStyleSheet("background-color: black;")

        self.rec_state = False
        self.rec = QtWidgets.QPushButton(self.Win)
        self.rec.setGeometry(QtCore.QRect(0, 10, 31, 31))
        self.icon = QtGui.QIcon()
        self.icon.addPixmap(QtGui.QPixmap("Resources/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.rec.setIcon(self.icon)
        self.rec.setIconSize(QtCore.QSize(40, 40))
        self.rec.setStyleSheet("background-color : black;")
        self.rec.setObjectName("rec")
        self.rec.clicked.connect(self.rec_func)

        self.cam_state = False
        self.cam = QtWidgets.QPushButton(self.Win)
        self.cam.setGeometry(QtCore.QRect(60, 10, 41, 31))
        self.icon1 = QtGui.QIcon()
        self.icon1.addPixmap(QtGui.QPixmap("Resources/video-camera.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cam.setIcon(self.icon1)
        self.cam.setIconSize(QtCore.QSize(25, 40))
        self.cam.setStyleSheet("background-color : black;")
        self.cam.setObjectName("cam")
        self.cam.clicked.connect(self.cam_func)

        self.mic_state = False
        self.mic = QtWidgets.QPushButton(self.Win)
        self.mic.setGeometry(QtCore.QRect(30, 10, 31, 31))
        self.icon2 = QtGui.QIcon()
        self.icon2.addPixmap(QtGui.QPixmap("Resources/mic.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mic.setIcon(self.icon2)
        self.mic.setIconSize(QtCore.QSize(40, 25))
        self.mic.setStyleSheet("background-color : black;")
        self.mic.setObjectName("mic")
        self.mic.clicked.connect(self.mic_func)

        self.close = QtWidgets.QPushButton(self.Win)
        self.close.setGeometry(QtCore.QRect(100, 10, 41, 31))
        self.icon3 = QtGui.QIcon()
        self.icon3.addPixmap(QtGui.QPixmap("Resources/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.close.setIcon(self.icon3)
        self.close.setIconSize(QtCore.QSize(30, 30))
        self.close.setStyleSheet("background-color : black;")
        self.close.setObjectName("close")
        self.close.clicked.connect(self.Win.close) 

        self.retranslateUi(self.Win)
        QtCore.QMetaObject.connectSlotsByName(self.Win)

        self.Win.show()
        sys.exit(self.app.exec_())

    def retranslateUi(self, Win):
        _translate = QtCore.QCoreApplication.translate
        self.Win.setWindowTitle(_translate("Win", "Win"))

    def rec_func(self):
        if not self.rec_state:
            self.icon = QtGui.QIcon()
            self.icon.addPixmap(QtGui.QPixmap("Resources/stop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.rec.setIcon(self.icon)
            self.rec.setIconSize(QtCore.QSize(30, 25))
            self.rec_state = True

        else:
            self.icon = QtGui.QIcon()
            self.icon.addPixmap(QtGui.QPixmap("Resources/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.rec.setIcon(self.icon)
            self.rec.setIconSize(QtCore.QSize(40, 40))
            self.rec_state = False

    def cam_func(self):
        if not self.cam_state:
            self.icon1 = QtGui.QIcon()
            self.icon1.addPixmap(QtGui.QPixmap("Resources/no-video.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.cam.setIcon(self.icon1)
            self.cam_state = True

        else:
            self.icon1 = QtGui.QIcon()
            self.icon1.addPixmap(QtGui.QPixmap("Resources/video-camera.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.cam.setIcon(self.icon1)
            self.cam_state = False

    def mic_func(self):
        if not self.mic_state:
            self.icon2 = QtGui.QIcon()
            self.icon2.addPixmap(QtGui.QPixmap("Resources/mute.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.mic.setIcon(self.icon2)
            self.mic_state = True

        else:
            self.icon2 = QtGui.QIcon()
            self.icon2.addPixmap(QtGui.QPixmap("Resources/mic.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.mic.setIcon(self.icon2)
            self.mic_state = False



if __name__ == "__main__":
    ui = Ui_Win()
    
