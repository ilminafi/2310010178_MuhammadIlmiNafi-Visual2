import sys
import mysql.connector as mc
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from MuhammadIlmiNafi_0178 import Ui_MainWindow  

class AppData(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.tambahdata)
        self.ui.pushButton_2.clicked.connect(self.editdata)
        self.ui.pushButton_3.clicked.connect(self.hapusdata)
        self.ui.pushButton_4.clicked.connect(self.batal)
        self.ui.pushButton_5.clicked.connect(self.hapus)
        self.ui.pushButton_6.clicked.connect(self.loadSql)
        self.ui.tableWidget.cellClicked.connect(self.loadByid)
        

    def tambahdata(self):
        try:
            npm = self.ui.lineEdit.text()
            nama_l = self.ui.lineEdit_2.text()
            nama_p = self.ui.lineEdit_3.text()
            no_hp = self.ui.lineEdit_4.text()
            email = self.ui.lineEdit_5.text()
            kelas = self.ui.lineEdit_6.text()
            matkul = self.ui.lineEdit_7.text()
            prodi = self.ui.lineEdit_8.text()
            lokasi = self.ui.lineEdit_9.text()

            mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="db_mhs"
            )
            mycursor = mydb.cursor()
            sql = """
                INSERT INTO mhs (npm, nama_l, nama_p, no_hp, email, kelas, matkul, prodi, lokasi)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            val = (npm, nama_l, nama_p, no_hp, email, kelas, matkul, prodi, lokasi)
            mycursor.execute(sql, val)
            mydb.commit()

            self.ui.label_11.setText("Data berhasil ditambahkan")
            self.loadSql()  
        except mc.Error as err:
            self.ui.label_11.setText(f" Error: {err}")

    def editdata(self):
        try:
            npm = self.ui.lineEdit.text()
            nama_l = self.ui.lineEdit_2.text()
            nama_p = self.ui.lineEdit_3.text()
            no_hp = self.ui.lineEdit_4.text()
            email = self.ui.lineEdit_5.text()
            kelas = self.ui.lineEdit_6.text()
            matkul = self.ui.lineEdit_7.text()
            prodi = self.ui.lineEdit_8.text()
            lokasi = self.ui.lineEdit_9.text()

            mydb = mc.connect(
                host ="localhost",
                user ="root",
                password ="",
                database ="db_mhs"
            )
            mycursor = mydb.cursor()

            sql = """UPDATE mhs SET
                nama_l = %s, nama_p = %s,
                no_hp = %s, email = %s,
                kelas = %s, matkul = %s,
                prodi = %s, lokasi = %s
            WHERE npm = %s """
            val = (nama_l, nama_p, no_hp, email, kelas, matkul, prodi, lokasi, npm)
            mycursor.execute(sql, val)
            mydb.commit()
            
            self.ui.label_11.setText("Data berhasil diUpdate")
            self.ui.lineEdit.setText("")
            self.ui.lineEdit_2.setText("")
            self.ui.lineEdit_3.setText("")
            self.ui.lineEdit_4.setText("")
            self.ui.lineEdit_5.setText("")
            self.ui.lineEdit_6.setText("")
            self.ui.lineEdit_7.setText("")
            self.ui.lineEdit_8.setText("")
            self.ui.lineEdit_9.setText("")
            self.loadSql()
        except mc.Error as err:
            self.ui.label_11.setText("Data Gagal DiUpdate")

    def hapusdata(self):
        try:
            selected_row = self.ui.tableWidget.currentRow()
            if selected_row < 0:
                self.ui.label_11.setText("Pilih data yang ingin dihapus terlebih dahulu")
                return

            item_npm = self.ui.tableWidget.item(selected_row, 0)
            if item_npm is None:
                self.ui.label_11.setText("Data tidak valid atau kosong")
                return
            
            npm = item_npm.text()
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="db_mhs"
            )
            cursor = mydb.cursor()
            sql = "DELETE FROM mhs WHERE npm = %s"
            val = (npm,)
            cursor.execute(sql, val)
            mydb.commit()

            self.ui.label_11.setText("Data berhasil dihapus")
            self.loadSql()

        except mc.Error as err:
            self.ui.label_11.setText(f"Error: {err}")

    def batal(self):
            self.ui.lineEdit.clear()
            self.ui.lineEdit_2.clear()
            self.ui.lineEdit_3.clear()
            self.ui.lineEdit_4.clear()
            self.ui.lineEdit_5.clear()
            self.ui.lineEdit_6.clear()
            self.ui.lineEdit_7.clear()
            self.ui.lineEdit_8.clear()
            self.ui.lineEdit_9.clear()
            self.ui.label_11.setText("Input dibersihkan")

    def hapus(self):
        self.ui.tableWidget.clearContents()          
        self.ui.tableWidget.setRowCount(0)           
        self.ui.label_11.setText("Data berhasil dihapus dari tampilan")


    def loadByid(self, row):
        try:
            rownpm = self.ui.tableWidget.item(row,0)
            rownama = self.ui.tableWidget.item(row,1)
            rownamap = self.ui.tableWidget.item(row,2)
            rownohp = self.ui.tableWidget.item(row,3)
            rowemail = self.ui.tableWidget.item(row,4)
            rowkelas = self.ui.tableWidget.item(row,5)
            rowmatkul = self.ui.tableWidget.item(row,6)
            rowprodi = self.ui.tableWidget.item(row,7)
            rowlokasi = self.ui.tableWidget.item(row,8)

            if rownpm :
                npm = rownpm.text()
                nama_l = rownama.text()
                nama_p = rownamap.text()
                no_hp = rownohp.text()
                email = rowemail.text()
                kelas = rowkelas.text()
                matkul = rowmatkul.text()
                prodi = rowprodi.text()
                lokasi = rowlokasi.text()

                self.ui.lineEdit.setText(npm)
                self.ui.lineEdit_2.setText(nama_l)
                self.ui.lineEdit_3.setText(nama_p)
                self.ui.lineEdit_4.setText(no_hp)
                self.ui.lineEdit_5.setText(email)
                self.ui.lineEdit_6.setText(kelas)
                self.ui.lineEdit_7.setText(matkul)
                self.ui.lineEdit_8.setText(prodi)
                self.ui.lineEdit_9.setText(lokasi)

            self.ui.label_11.setText("Data Berhasil ditampilkan")
        except mc.Error as err:
            self.ui.label_11.setText("Data Gagal ditampilkan")
            
        
    def loadSql(self):
        try:
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="db_mhs"
            )
            mycursor = mydb.cursor()
            mycursor.execute("SELECT * FROM mhs ORDER BY npm ASC")
            result = mycursor.fetchall()
            self.ui.tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(result):
                self.ui.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.ui.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))
            self.ui.label_11.setText("Data berhasil ditampilkan")
        except mc.Error as err:
            self.ui.label_11.setText("Data Gagal ditampilkan")

app = QApplication(sys.argv)
window = AppData()
window.show()
sys.exit(app.exec_())
