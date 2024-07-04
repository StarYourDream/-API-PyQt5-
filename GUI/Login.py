import sys
import warnings

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication

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

        # 进入系统按钮
        self.pushButton = QtWidgets.QPushButton(QLoginWidget)
        self.pushButton.setGeometry(QtCore.QRect(670, 640, 400, 150))
        self.pushButton.setStyleSheet(
            "QPushButton { background-color:#89CFF0; color: white; font-size: 40px; "
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
