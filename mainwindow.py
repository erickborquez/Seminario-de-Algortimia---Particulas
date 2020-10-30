from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox
from PySide2.QtCore import Slot
from ui_window import Ui_MainWindow
from Particulas.particula import Particula
from Particulas.particulas import Particulas


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.particulas = Particulas()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.add_start_pushButton.clicked.connect(self.click_add_start)
        self.ui.add_end_pushButton.clicked.connect(self.click_add_end)
        self.ui.print_pushButton.clicked.connect(self.click_show)
        self.ui.actionAbrir.triggered.connect(self.action_abrir_archivo)
        self.ui.actionGuardar.triggered.connect(self.action_guardar_archivo)

    def click_show(self):
        # self.libreria.mostrar()
        self.ui.plainTextEdit.clear()
        self.ui.plainTextEdit.insertPlainText(str(self.particulas))
        self.particulas.mostrar()

    @Slot()
    def action_abrir_archivo(self):
        ubicacion = QFileDialog.getOpenFileName(
            self,
            'Abrir Archivo',
            '.',
            'JSON (*.json)'
        )[0]

        if self.particulas.abrir(ubicacion):
            QMessageBox.information(
                self, "Éxito", "Se pudo crear el archivo " + ubicacion)
        else:
            QMessageBox.critical(
                self, "Error", "No se puedo crear el archivo " + ubicacion)

    @Slot()
    def action_guardar_archivo(self):
        ubicacion = QFileDialog.getSaveFileName(
            self,
            'Guardar Archivo',
            '.',
            "JSON (*.json)"
        )[0]
        if self.particulas.guardar(ubicacion):
            QMessageBox.information(
                self, "Éxito", "Se pudo crear el archivo " + ubicacion)
        else:
            QMessageBox.critical(
                self, "Error", "No se puedo crear el archivo " + ubicacion)

    @Slot()
    def getParticula(self):
        id = self.ui.id_lineEdit.text()
        origin_x = int(self.ui.origin_x_lineEdit.text())
        origin_y = int(self.ui.origin_y_lineEdit.text())
        dest_x = int(self.ui.dest_x_lineEdit.text())
        dest_y = int(self.ui.dest_y_lineEdit.text())
        velocity = int(self.ui.velocity_lineEdit.text())
        red = int(self.ui.red_lineEdit.text())
        green = int(self.ui.green_lineEdit.text())
        blue = int(self.ui.blue_lineEdit.text())
        return Particula(id, origin_x, origin_y, dest_x,
                         dest_y, velocity, red, green, blue)

    @ Slot()
    def click_add_start(self):
        self.particulas.agregar_inicio(self.getParticula())

    @ Slot()
    def click_add_end(self):
        self.particulas.agregar_final(self.getParticula())
