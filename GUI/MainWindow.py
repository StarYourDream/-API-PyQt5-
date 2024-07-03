from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QPushButton, QWidget
from FileUploda import  QFileWidget
from main import API

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setGeometry(500,500,1500,1100)
        MainWindow.setStyleSheet("background-color: white;")
        # 设置 centralwidget
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # 展示图片的标签
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../pictures/111.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        # 设置标签位置和大小
        self.label.setGeometry(100, 60, 700,650)


        # 展示识别结果的标签
        # 创建标签 label_2 并设置位置和大小
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.label_2.setGeometry(880, 60, 500, 1000)

        # 设置标签的背景颜色和文字大小
        self.label_2.setStyleSheet("background-color: #AB9B93; color: white; font-size: 26px;")
        MainWindow.setCentralWidget(self.centralwidget)


        # 上传按钮
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        # 设置按钮位置和大小
        self.pushButton.setGeometry(150, 840, 200, 160)
        self.pushButton.setStyleSheet(
            "QPushButton { background-color:#0D98BA; color: white; font-size: 40px; "
            "font-weight: bold;border-radius: 50%;font-family: '微软雅黑';}")

        # 识别按钮
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        # 设置按钮位置和大小
        self.pushButton_2.setGeometry(490, 840, 200, 160)
        self.pushButton_2.setStyleSheet(
            "QPushButton { background-color:#0D98BA; color: white; font-size: 40px; "
            "font-weight: bold;border-radius: 50%;font-family: '微软雅黑';}")


        # 其他
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, MainWindow.width(), 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "上传"))
        self.pushButton_2.setText(_translate("MainWindow", "识别"))
        self.label_2.setText(_translate("MainWindow",""))



class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.open_child_window)
        self.ui.pushButton_2.clicked.connect(self.APIGet)
        self.uploaded_file_path = None  # 类变量来存储文件路径

    def open_child_window(self):
        self.child1 = QFileWidget()
        self.child1.show()
        # 连接信号到槽函数
        self.child1.image_uploaded.connect(self.handle_image_uploaded)

    def APIGet(self):
        if self.uploaded_file_path:  # 确保文件路径已设置
            formatted_json = API(self.uploaded_file_path)
            self.ui.label_2.setText(formatted_json)


    def handle_image_uploaded(self, file_path):
        self.uploaded_file_path = file_path  # 存储文件路径
        pixmap = QtGui.QPixmap(file_path)
        self.ui.label.setPixmap(pixmap.scaled(self.ui.label.size(), QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))

    def handle_answer_show(self,file_path):
        formatted_json = API(file_path)
        self.ui.label_2.setText(formatted_json)




if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())