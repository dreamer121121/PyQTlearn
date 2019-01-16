from PyQt5.QtWidgets import QMainWindow, QApplication
from UI_MainWindow import Ui_main_MainWindow
import sys


class Main_Window(QMainWindow, Ui_main_MainWindow):

    def __init__(self):
        super(Main_Window, self).__init__()  # 通过这句话就可以调用其父类的属性和方法
        self.setupUi(self)
        print('进入Main_Window')

    # def showLable(self):
    #     msg = 'success'
    #     self.label_2.setText(msg)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = Main_Window()
    sys.exit(app.exec_())
