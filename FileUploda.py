import cv2
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QFileDialog
import os
import sys
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)

class QFileWidget(QtWidgets.QWidget):
    image_uploaded = QtCore.pyqtSignal(str)
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(1400, 600, 1000, 700)
        self.setWindowTitle("文件上传")
        self.setStyleSheet("background-color: white;")

        # 创建UI组件
        self.textEdit = QtWidgets.QTextEdit(self)
        self.textEdit.setGeometry(QtCore.QRect(210, 300, 730, 90))
        font = self.textEdit.font()
        font.setPointSize(14)
        self.textEdit.setFont(font)

        self.label = QtWidgets.QLabel("文件上传", self)
        self.label.setGeometry(QtCore.QRect(220, 160, 250, 80))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel { color:#89CFF0; font-family: '华文行楷'; }")

        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(500, 120, 180, 140))
        self.label_2.setPixmap(QtGui.QPixmap("../pictures/cloud.png"))
        self.label_2.setScaledContents(True)

        self.pushButton = QtWidgets.QPushButton("✚", self)
        self.pushButton.setGeometry(QtCore.QRect(70, 300, 130, 90))
        self.pushButton.setStyleSheet(
            "QPushButton { background-color:#89CFF0; color: white; font-size: 40px; "
            "font-weight: bold;border-radius: 50%;}")

        self.pushButton_2 = QtWidgets.QPushButton("上传文件", self)
        self.pushButton_2.setGeometry(QtCore.QRect(370, 500, 210, 90))
        self.pushButton_2.setStyleSheet(
            "QPushButton { background-color:#89CFF0; color: white; font-size: 40px; "
            "font-weight: bold;border-radius: 50%;}")

        # 连接信号到槽
        self.pushButton.clicked.connect(self.openFileNameQtWidget)
        self.pushButton_2.clicked.connect(self.on_upload_clicked)
        self.setAcceptDrops(True)

    def openFileNameQtWidget(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, '选择图片', '', '图片文件 (*.png *.jpg *.jpeg);;所有文件 (*)',
                                                   options=options)
        if fileName:
            self.textEdit.setText(fileName)
            self.image_uploaded.emit(fileName)

    def on_upload_clicked(self):
        content = self.textEdit.toPlainText()
        # 复制图片副本用于裁剪
        img = cv2.imread(content)
        output_path = os.path.join('copy2', f'other.jpg')
        cv2.imwrite(output_path, img)
        if not os.path.exists(content):
            QMessageBox.warning(self, "上传失败", "请上传图片")
        else:
             QMessageBox.information(self, "上传成功", "文件上传成功！")
             self.close()

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

            if event.mimeData().hasUrls():
                event.setDropAction(QtCore.Qt.CopyAction)
                for url in event.mimeData().urls():
                    file_path = url.toLocalFile()
                    self.textEdit.setText(file_path)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QFileWidget()
    mainWindow.show()
    sys.exit(app.exec_())
