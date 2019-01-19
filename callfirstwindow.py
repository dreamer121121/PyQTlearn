from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from UI_Login import Ui_Login_MainWindow
from UI_MainWindow import Ui_main_MainWindow
from aip import  AipOcr
import sys

APP_ID = '14660084'
API_KEY = 'liGXaa0wfIrlzTB1x5bT8Afc'
SECRET_KEY = 'GHLpfGKOx54mRWHXKFruBSLtoWCT6yYB'
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)


class Main_Window(QMainWindow, Ui_main_MainWindow):

    def __init__(self):
        super(Main_Window, self).__init__()  # 通过这句话就可以调用其父类的属性和方法
        self.setupUi(self)

    def get_file_content(self):
        with open(self.file_path, 'rb') as fp:
            print('finish get image')
            return fp.read()

    def choose(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "选择发票", r"C:\Users\jack xia\Desktop\test")
        self.file_path = file_path
        img = QImage()
        img.load(file_path)  # 载入图片
        self.img = img
        self.img = img.scaled(self.graphicsView.width(), self.graphicsView.height())
        self.graphicsView.scene = QGraphicsScene()  # 创建一个图片元素的对象
        self.graphicsView.scene.addPixmap(QPixmap().fromImage(self.img))  # 将加载后的图片传递给scene对象
        self.graphicsView.setScene(self.graphicsView.scene)
        self.img = self.get_file_content()

    def recognition(self):
        print('---开始识别---')
        data = client.vatInvoice(self.img)
        print('----data----', data)


class Login_Window(QMainWindow, Ui_Login_MainWindow):

    def __init__(self):
        super(Login_Window, self).__init__()  # 通过这句话就可以调用其父类的属性和方法
        self.setupUi(self)

    def slot1(self):
        if self.lineEdit_4.text() == '' and self.lineEdit_3.text() == '':
            self.hide()
            self.main = Main_Window()
            self.main.show()
        else:
            QMessageBox.critical(self, "Login Error！", "用户名为：meixi,密码为：521")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_window = Login_Window()  # 初始化
    login_window.show()
    sys.exit(app.exec_())
