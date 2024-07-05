import sys
import warnings

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QLabel

from MainWindow import MainUseWindow

warnings.filterwarnings("ignore", category=DeprecationWarning)


class QLoginWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, QLoginWidget):
        QLoginWidget.setObjectName("QLoginWidget")
        QLoginWidget.setMinimumSize(QtCore.QSize(1800, 1000))
        QLoginWidget.setMaximumSize(QtCore.QSize(1800, 1000))
        font = QtGui.QFont()
        font.setPointSize(5)
        QLoginWidget.setFont(font)
        QLoginWidget.setStyleSheet("background-color: white;")
        # 使用QLabel设置背景图
        label = QLabel(self)
        pixmap = QPixmap("../pictures/login_ground.jpg")  # 替换为你的图片路径
        pixmap = pixmap.scaled(self.width(), self.height())  # 缩放图片以适应窗口大小
        label.setPixmap(pixmap)
        label.setGeometry(0, 0, self.width(), self.height())

        self.label = QtWidgets.QLabel(QLoginWidget)
        self.label.setText("内蒙古智能车辆识别系统")
        self.label.setObjectName("欢迎")
        # 设置标签位置和大小
        self.label.setGeometry(390, 300, 1000, 200)
        self.label.setStyleSheet("QLabel "
                                 "{ background-color: transparent;"
                                 "color:white; "
                                 "font-family: '华文行楷'; "
                                 "font-size: 90px;"
                                 "}")

        # 进入系统按钮
        self.pushButton = QtWidgets.QPushButton(QLoginWidget)
        self.pushButton.setGeometry(QtCore.QRect(670, 640, 400, 150))
        self.pushButton.setStyleSheet(
            "QPushButton { background-color:#314C70; color: white; font-size: 40px; "
            "font-weight: bold;border-radius: 50%;}")
        font = QtGui.QFont()
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        # 创建
        self.retranslateUi(QLoginWidget)
        QtCore.QMetaObject.connectSlotsByName(QLoginWidget)

    def retranslateUi(self, QLoginWidget):
        _translate = QtCore.QCoreApplication.translate
        QLoginWidget.setWindowTitle(_translate("QLoginWidget", "登录"))
        self.pushButton.setText(_translate("QLoginWidget", "进入系统"))
        # 连接信号到槽
        self.pushButton.clicked.connect(self.login)
        self.setAcceptDrops(True)  # 允许窗口接受拖拽

    def login(self):
       self.child=MainUseWindow()
       self.child.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QLoginWidget()
    mainWindow.show()
    sys.exit(app.exec_())
