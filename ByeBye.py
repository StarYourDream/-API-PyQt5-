from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QImage, QPixmap
import sys
from Video import Video


class SupriseWindow(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.label222 = None
        self.setupUi()

    def setupUi(self):
        self.setObjectName("MainWindow")
        self.setGeometry(200, 200, 2600, 1400)
        self.setStyleSheet("background-color: white;")

        self.label = QtWidgets.QLabel(self)
        self.label.setText("")
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        # 设置标签位置和大小
        self.label.setGeometry(260, 110, 2000, 1200)


        self.label1 = QtWidgets.QLabel(self)
        self.label1.setText("视频模式敬请期待！")
        self.label1.setScaledContents(True)
        self.label1.setObjectName("label")
        self.label1.setGeometry(360, 180, 2000, 200)
        font = QtGui.QFont()
        font.setPointSize(80)
        self.label1.setFont(font)
        self.label1.setStyleSheet("QLabel"
                                  " { background-color: transparent; "
                                  "color:#FADADD;"
                                  " font-family: '宋体'; }")

        self.th1 = Video(0)
        self.th1.send.connect(self.showimg)
        self.th1.start()

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "彩蛋：视频"))


    def showimg(self, h, w, c, b, th_id):
        image = QImage(b, w, h, w * c, QImage.Format_BGR888)
        pix = QPixmap.fromImage(image)
        if th_id == 0:
            width = self.label.width()
            height = self.label.height()
            scale_pix = pix.scaled(width, height, Qt.KeepAspectRatio)
            self.label.setPixmap(scale_pix)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = SupriseWindow()
    mainWindow.show()
    sys.exit(app.exec_())
