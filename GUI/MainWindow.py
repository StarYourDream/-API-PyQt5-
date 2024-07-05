from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QLabel

from FileUploda import QFileWidget
from main import process_image
import sys
from ByeBye import SupriseWindow

class MainUseWindow(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setObjectName("MainWindow")
        self.setGeometry(200, 200, 2600, 1400)
        self.setStyleSheet("background-color: white;")

        # 使用QLabel设置背景图
        label = QLabel(self)
        pixmap = QPixmap("../pictures/main_ground.jpg")  # 替换为你的图片路径
        pixmap = pixmap.scaled(self.width(), self.height())  # 缩放图片以适应窗口大小
        label.setPixmap(pixmap)
        label.setGeometry(0, 0, self.width(), self.height())

        self.label = QtWidgets.QLabel(self)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../pictures/example.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        # 设置标签位置和大小
        self.label.setGeometry(100, 60, 1400, 1200)

        # 展示识别结果的标签
        # 创建 QTableWidget
        # 创建 QTableWidget 实例
        self.tableWidget = QtWidgets.QTableWidget(self)

        # 设置表头的样式
        # 这行代码设置了表头背景色为绿色，文字颜色为白色
        self.tableWidget.horizontalHeader().setStyleSheet(
            "QHeaderView::section { background-color: #6A9276; color: white; }")

        # 设置 QTableWidget 的位置和大小
        self.tableWidget.setGeometry(1600, 90, 860, 850)

        # 设置垂直滚动条策略
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)

        # 设置水平滚动条策略
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)

        # 设置列数
        self.tableWidget.setColumnCount(4)

        # 设置表头标签
        self.tableWidget.setHorizontalHeaderLabels(['类型', '车牌', '品牌名', '年份'])

        # 设置样式
        self.tableWidget.setStyleSheet("background-color: white; color: black; font-size: 26px;")

        #彩蛋按钮
        self.arrow_button = QtWidgets.QPushButton(self)
        self.arrow_button.setObjectName("pushButton")
        # 设置按钮位置和大小
        self.arrow_button.setGeometry(2400, 1250, 120, 110)
        self.arrow_button.setIcon(QIcon('../pictures/LogosInternetComputerIcon.svg'))
        self.arrow_button.setIconSize(QSize(120, 120))  # 可选，设置图标大小
        self.arrow_button.setStyleSheet("QPushButton { background-color: transparent; border: none; }")
        self.arrow_button.clicked.connect(self.surprise)

        # 上传按钮
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setObjectName("pushButton")
        # 设置按钮位置和大小
        self.pushButton.setGeometry(1700, 1000, 250, 210)
        self.pushButton.setStyleSheet("""
                   QPushButton {
                       background-color: #0D98BA;
                       color: white;
                       font-size: 40px;
                       font-weight: bold;
                       border-radius: 50%;
                       font-family: '微软雅黑';
                       border: 9px solid white; /* 设置边缘线 */
                   }
                  
               """)

        # 识别按钮
        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setObjectName("pushButton_2")
        # 设置按钮位置和大小
        self.pushButton_2.setGeometry(2120, 1000, 250, 210)
        self.pushButton_2.setStyleSheet("""
                   QPushButton {
                       background-color: #0D98BA;
                       color: white;
                       font-size: 40px;
                       font-weight: bold;
                       border-radius: 50%;
                       font-family: '微软雅黑';
                       border: 9px solid white; /* 设置边缘线 */
                       box-shadow: 0px 0px 20px rgba(255, 255, 255, 0.5); /* 设置发光效果 */
                   }
                   QPushButton:hover {
                       box-shadow: 0px 0px 30px rgba(255, 255, 255, 0.7); /* 鼠标悬停时的发光效果增强 */
                   }
               """)

        self.pushButton.clicked.connect(self.open_child_window)
        self.pushButton_2.clicked.connect(self.recognize)
        self.uploaded_file_path = None  # 类变量来存储文件路径

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "上传"))
        self.pushButton_2.setText(_translate("MainWindow", "识别"))
        # self.label_2.setText(_translate("MainWindow", ""))

    def fill_table(self, data):
        # 判断data是否是单个列表
        if isinstance(data, list) and not all(isinstance(item, list) for item in data):
            # 将单个列表转化为包含单个列表的列表
            data = [data]
        # 清除现有行
        self.tableWidget.setRowCount(0)
        # 添加行和数据
        for row_data in data:
            row = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row)
            for col, item in enumerate(row_data):
                self.tableWidget.setItem(row, col, QtWidgets.QTableWidgetItem(str(item)))

    def open_child_window(self):
        self.child = QFileWidget()
        self.child.show()
        # 连接信号到槽函数
        self.child.image_uploaded.connect(self.handle_image_uploaded)

    def surprise(self):
        self.child = SupriseWindow()
        self.child.show()

    def recognize(self):
        if self.uploaded_file_path:  # 确保文件路径已设置
            # formatted_json = show_pictures(self.uploaded_file_path)
            data = process_image(self.uploaded_file_path)
            self.fill_table(data)
            self.handle_image_uploaded('../pictures/processed_image.jpg')
            # self.handle_image_uploaded(process_image(self.uploaded_file_path))

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
