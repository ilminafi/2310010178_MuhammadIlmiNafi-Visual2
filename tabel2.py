import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
from PyQt5.uic import loadUi

data = []
data.append(('Andi', 'Teknik Informatika'))
data.append(('Nor Asmah', 'Teknik Informatika'))
data.append(('Joko Andi', 'Sistem Informasi'))

class HalloPython(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        loadUi('tablewid.ui', self)
        self.setWindowTitle('PYTHON GUI TABLEWIDGET')
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(4)

        row = 0
        for tup in data:
            col = 0
            for item in tup:
                cellinfo = QTableWidgetItem(item)
                self.tableWidget.setItem(row, col, cellinfo)
                col += 1
            row += 1

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = HalloPython()
    form.show()
    sys.exit(app.exec_())