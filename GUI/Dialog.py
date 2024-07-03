from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QDialog, QFileDialog
import os
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)

class Ui_QFileWidget(object):
    def setupUi(self, QFileWidget):
        QFileWidget.setObjectName("QFileWidget")
        QFileWidget.resize(1000, 700)
        QFileWidget.setMinimumSize(QtCore.QSize(1000, 700))
        QFileWidget.setMaximumSize(QtCore.QSize(1000, 700))
        font = QtGui.QFont()
        font.setPointSize(5)
        QFileWidget.setFont(font)
        QFileWidget.setStyleSheet("background-color: white;")

        #地址文本框
        self.textEdit = QtWidgets.QTextEdit(QFileWidget)
        self.textEdit.setGeometry(QtCore.QRect(210, 300, 730, 90))#地址文本框
        self.textEdit.setObjectName("textEdit")
        font = self.textEdit.font()
        font.setPointSize(14)
        self.textEdit.setFont(font)

        #标签
        self.label = QtWidgets.QLabel(QFileWidget)
        self.label.setGeometry(QtCore.QRect(220, 160, 250, 80))#文字"文件上传"
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label.setStyleSheet("QLabel { color:#89CFF0; font-family: '华文行楷'; }")

        #图标
        self.label_2 = QtWidgets.QLabel(QFileWidget)
        self.label_2.setGeometry(QtCore.QRect(500, 120, 180, 140))  # 图标
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_2.setFont(font)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../pictures/cloud.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")

        #选择文件按钮
        self.pushButton = QtWidgets.QPushButton(QFileWidget)
        self.pushButton.setGeometry(QtCore.QRect(70, 300, 130, 90))#按钮：选择文件
        self.pushButton.setStyleSheet(
            "QPushButton { background-color:#89CFF0; color: white; font-size: 40px; "
            "font-weight: bold;border-radius: 50%;}")
        font = QtGui.QFont()
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        #上传文件按钮
        self.pushButton_2 = QtWidgets.QPushButton(QFileWidget)
        self.pushButton_2.setGeometry(QtCore.QRect(370, 500, 210, 90))#按钮：上传文件
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")#上传文件
        self.pushButton_2.setStyleSheet(
            "QPushButton { background-color:#89CFF0; color: white; font-size: 40px; "
            "font-weight: bold;border-radius: 50%;}")
        #创建
        self.retranslateUi(QFileWidget)
        QtCore.QMetaObject.connectSlotsByName(QFileWidget)

    def retranslateUi(self, QFileWidget):
        _translate = QtCore.QCoreApplication.translate
        QFileWidget.setWindowTitle(_translate("QFileWidget", "文件上传"))
        self.label.setText(_translate("QFileWidget", "文件上传"))
        self.pushButton.setText(_translate("QFileWidget", "✚"))
        self.pushButton_2.setText(_translate("QFileWidget", "上传文件"))
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_QFileWidget()
        self.ui.setupUi(self)

        # 连接信号到槽
        self.ui.pushButton.clicked.connect(self.openFileNameQtWidget)
        self.ui.pushButton_2.clicked.connect(self.on_upload_clicked)
        self.setAcceptDrops(True)  # 允许窗口接受拖拽

    def openFileNameQtWidget(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "选择文件", "", "All Files (*);;Python Files (*.py)",
                                                  options=options)
        if fileName:
            self.ui.textEdit.setText(fileName)


    def on_upload_clicked(self):
        content = self.ui.textEdit.toPlainText()
        if not os.path.exists(content):  # 修改这里
            QMessageBox.warning(self, "上传失败", "请上传图片")
        else:
         ext = os.path.splitext(content)[1]
         if ext.lower() in ['.jpg', '.jpeg', '.png', '.bmp']:
             QMessageBox.information(self, "上传成功", "文件上传成功！")
             self.close()
         else:
             QMessageBox.warning(self, "上传失败", "格式错误")

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            event.setDropAction(QtCore.Qt.CopyAction)
            for url in event.mimeData().urls():
                file_path = url.toLocalFile()
                self.ui.textEdit.setText(file_path)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())