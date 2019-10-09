from PyQt5 import QtWidgets
from calc import Ui_MainWindow  
import sys


class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_3.clicked.connect(self.modifipole)

    def modifipole(self):
        self.ui.MainPole.setText("New")


app = QtWidgets.QApplication([])
application = mywindow()
application.show()
sys.exit(app.exec())