from PyQt5 import QtCore, QtGui, QtWidgets
from FileUploda import QFileWidget
from main import api
from main import process_image
import sys


class MainUseWindow(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setObjectName("MainWindow")
        self.setGeometry(500, 500, 1500, 1100)
        self.setStyleSheet("background-color: white;")

        self.label = QtWidgets.QLabel(self)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../pictures/111.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        # 设置标签位置和大小
        self.label.setGeometry(100, 60, 700, 650)

        # 展示识别结果的标签
        # 创建标签 label_2 并设置位置和大小
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setObjectName("label_2")
        self.label_2.setGeometry(880, 60, 500, 1000)

        # 设置标签的背景颜色和文字大小
        self.label_2.setStyleSheet("background-color: #AB9B93; color: white; font-size: 26px;")

        # 上传按钮
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setObjectName("pushButton")
        # 设置按钮位置和大小
        self.pushButton.setGeometry(150, 840, 200, 160)
        self.pushButton.setStyleSheet(
            "QPushButton { background-color:#0D98BA; color: white; font-size: 40px; "
            "font-weight: bold;border-radius: 50%;font-family: '微软雅黑';}")

        # 识别按钮
        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setObjectName("pushButton_2")
        # 设置按钮位置和大小
        self.pushButton_2.setGeometry(490, 840, 200, 160)
        self.pushButton_2.setStyleSheet(
            "QPushButton { background-color:#0D98BA; color: white; font-size: 40px; "
            "font-weight: bold;border-radius: 50%;font-family: '微软雅黑';}")

        self.pushButton.clicked.connect(self.open_child_window)
        # self.pushButton_2.clicked.connect(self.api_get)
        self.pushButton_2.clicked.connect(self.recognize)
        self.uploaded_file_path = None  # 类变量来存储文件路径

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "上传"))
        self.pushButton_2.setText(_translate("MainWindow", "识别"))
        self.label_2.setText(_translate("MainWindow", ""))

    def open_child_window(self):
        self.child = QFileWidget()
        self.child.show()
        # 连接信号到槽函数
        self.child.image_uploaded.connect(self.handle_image_uploaded)

    def api_get(self):  # 识别
        if self.uploaded_file_path:  # 确保文件路径已设置
            formatted_json = api(self.uploaded_file_path)
            self.label_2.setText(formatted_json)

    def recognize(self):
        if self.uploaded_file_path:  # 确保文件路径已设置
            formatted_json = api(self.uploaded_file_path)
            self.label_2.setText(formatted_json)
            self.handle_image_uploaded(process_image(self.uploaded_file_path))

    def handle_image_uploaded(self, file_path):
        self.uploaded_file_path = file_path  # 存储文件路径
        pixmap = QtGui.QPixmap(file_path)
        self.label.setPixmap(
            pixmap.scaled(self.label.size(), QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainUseWindow()
    mainWindow.show()
    sys.exit(app.exec_())
