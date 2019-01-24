from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QRect, Qt
from PyQt5.QtWidgets import *
from MainWindow import Ui_MainWindow
from Children import Ui_ChildrenForm
from Children02 import Ui_Form
import sys


class Main_window(QMainWindow, Ui_MainWindow):

    """多继承"""

    def __init__(self):
        super(Main_window, self).__init__()  # 通过这句话就可以调用其父类的属性和方法
        self.setupUi(self)
        self.actiondakai.triggered.connect(self.open)  # 把动作按钮链接到动作函数
        self.child = ChildrenForm()
        self.child02 = Children02()

    def open(self):
        file, _ = QFileDialog.getOpenFileName(self, "打开", r"C:\Users\dreamer\Desktop\Market")
        self.statusbar.showMessage(file)

    def showchildren(self):
        self.gridLayout.addWidget(self.child)
        self.child.show()

    def slot1(self):
        self.child.hide()
        self.child02.show()



class ChildrenForm(QMainWindow, Ui_ChildrenForm):
    def __init__(self):
        super(ChildrenForm, self).__init__()
        self.setupUi(self)


class Children02(QMainWindow, Ui_Form):
    def __init__(self):
        super(Children02, self).__init__()
        self.setupUi(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    Main = Main_window()  # 初始化
    Main.show()
    sys.exit(app.exec_())
