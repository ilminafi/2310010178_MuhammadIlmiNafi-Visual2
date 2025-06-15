import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import loadUi
class HalloPython(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        loadUi('tablewid.ui',self)
        self.setWindowTitle('PYTHON GUI TABLEWIDGET')
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(4)
        self.pushButton_5.clicked.connect(self.hapus)

    def hapus(self):
        self.tableWidget.clear()

if __name__=="__main__":
    app=QApplication(sys.argv)
    form=HalloPython()
    form.show()
    sys.exit(app.exec_())