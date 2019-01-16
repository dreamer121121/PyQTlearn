from PyQt5.QtWidgets import QMainWindow, QApplication
from UI_Login import Ui_Login_MainWindow
from main import *
import sys


class Login_Window(QMainWindow, Ui_Login_MainWindow):
    def __init__(self):
        super(Login_Window, self).__init__()  # 通过这句话就可以调用其父类的属性和方法
        self.setupUi(self)
        self.pushButton.clicked.connect(self.slot1)

    def slot1(self):
        if self.lineEdit.text() == 'xt' and self.lineEdit_2.text() == '123':
            self.close()
            mainwindow.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_window = Login_Window()  # 初始化
    login_window.show()
    mainwindow = Main_Window()
    sys.exit(app.exec_())
