import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
from PyQt5.uic import loadUi
import mysql.connector as mc

class HalloPython(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        loadUi('tablewid.ui', self)
        self.setWindowTitle('PYTHON GUI TABLEWIDGET')
        self.pushButton_5.clicked.connect(self.hapus)
        self.pushButton_6.clicked.connect(self.sqlLoad)
        self.pushButton.clicked.connect(self.insertkategori)
        self.tableWidget.cellClicked.connect(self.loadByid)
        self.pushButton_2.clicked.connect(self.updatekategori)
        self.pushButton_3.clicked.connect(self.deletekategori)
        self.pushButton_4.clicked.connect(self.batal)


    def deletekategori(self):
        try:
            selected_row = self.tableWidget.currentRow()
            if selected_row < 0:
                self.label_3.setText("Pilih data yang ingin dihapus")
                return
            
            nama_item = self.tableWidget.item(selected_row, 0)
            if nama_item is None:
                self.label_3.setText("Data tidak valid")
                return
            nama = nama_item.text()

            mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="db_latihan"
            )
            cursor = mydb.cursor()
            sql = "DELETE FROM mahasiswa WHERE nama = %s"
            val = (nama,)
            cursor.execute(sql, val)
            mydb.commit()


            self.label_3.setText("Data berhasil dihapus")
            self.sqlLoad()

        except mc.Error as err:
            self.label_3.setText(f"Error: {err}")

    def hapus(self):
        self.tableWidget.clearContents()          
        self.tableWidget.setRowCount(0)           
        self.label_3.setText("Data berhasil dihapus dari tampilan")


    def sqlLoad(self):
        try:
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="db_latihan"
            )
            mycursor = mydb.cursor()
            mycursor.execute("SELECT * FROM mahasiswa Order By nama ASC")
            result = mycursor.fetchall()
            self.tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))
            self.label_3.setText("Data berhasil ditampilkan")
        except mc.Error as err:
            self.label_4.setText("Data Gagal ditampilkan")

    def insertkategori(self):
        try:
            mydb = mc.connect(
                host="localhost",
                user ="root",
                password ="",
                database ="db_latihan"
            )
            cursor = mydb.cursor()
            nama = self.lineEdit.text()
            jurusan = self.lineEdit_2.text()

            sql = "Insert into mahasiswa (nama, jurusan) values (%s,%s)"
            val = (nama,jurusan)
            cursor.execute(sql,val)
            mydb.commit()
            self.label_4.setText("Data berhasil disimpan")
            self.lineEdit.setText("")
            self.lineEdit_2.setText("")
            self.sqlLoad()
        except mc.Error as err:
            self.label_4.setText("Data Gagal Disimpan")
    
    def loadByid(self, row):
        try:
            rownama = self.tableWidget.item(row,0)
            rowjur = self.tableWidget.item(row,1)
            if rownama :
                nama = rownama.text()
                jurusan = rowjur.text()
                self.lineEdit.setText(nama)
                self.lineEdit_2.setText(jurusan)
            self.label_3.setText("Data Berhasil ditampilkan")
        except mc.Error as err:
            self.label_3.setText("Data Gagal ditampilkan")

    def updatekategori(self):
        try:
            mydb = mc.connect(
                host ="localhost",
                user ="root",
                password ="",
                database ="db_latihan"
            )
            cursor = mydb.cursor()
            nama = self.lineEdit.text()
            jurusan = self.lineEdit_2.text()

            sql = "update mahasiswa set jurusan = %s where nama = %s"
            val = (jurusan,nama)
            cursor.execute(sql,val)
            mydb.commit()
            
            self.label_3.setText("Data berhasil diUpdate")
            self.lineEdit.setText("")
            self.lineEdit_2.setText("")
            self.sqlLoad()
        except mc.Error as err:
            self.label_3.setText("Data Gagal DiUpdate")

    def batal(self):
            self.lineEdit.clear()
            self.lineEdit_2.clear()
            self.label_3.setText("Input dibersihkan")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = HalloPython()
    form.show()
    sys.exit(app.exec_())