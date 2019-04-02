import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

class Checkers(QWidget):

    def __init__(self):
        super().__init__()
        self.title = "Checkers"
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        #self.initUI()
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()

    #def initUI(self):
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Checkers()
    sys.exit(app.exec_())
   
