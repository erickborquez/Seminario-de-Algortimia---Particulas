from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QTableWidgetItem
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

        self.ui.show_button.clicked.connect(self.click_show_table)
        self.ui.search_button.clicked.connect(self.click_search_table)

    @Slot()
    def click_show_table(self):
        self.ui.table.setColumnCount(6)
        headers = ["Id", "Origen X", "Origen Y",
                   "Destino X", "Destino Y", "Distancia"]
        self.ui.table.setHorizontalHeaderLabels(headers)
        self.ui.table.setRowCount(len(self.particulas))

        row = 0
        for particula in self.particulas:
            id_widget = QTableWidgetItem(particula.id)
            origen_x_widget = QTableWidgetItem(str(particula.origen_x))
            origen_y_widget = QTableWidgetItem(str(particula.origen_y))
            destino_x_widget = QTableWidgetItem(str(particula.destino_x))
            destino_y_widget = QTableWidgetItem(str(particula.destino_y))
            distancia_widget = QTableWidgetItem(str(particula.distancia))

            self.ui.table.setItem(row, 0, id_widget)
            self.ui.table.setItem(row, 1, origen_x_widget)
            self.ui.table.setItem(row, 2, origen_y_widget)
            self.ui.table.setItem(row, 3, destino_x_widget)
            self.ui.table.setItem(row, 4, destino_y_widget)
            self.ui.table.setItem(row, 5, distancia_widget)

            row += 1

        print('Mostrar tabla')

    @Slot()
    def click_search_table(self):
        id = self.ui.search_line.text()

        for particula in self.particulas:
            if id == particula.id:
                self.ui.table.clear()
                self.ui.table.setColumnCount(6)
                headers = ["Id", "Origen X", "Origen Y",
                           "Destino X", "Destino Y", "Distancia"]
                self.ui.table.setHorizontalHeaderLabels(headers)
                self.ui.table.setRowCount(1)
                id_widget = QTableWidgetItem(particula.id)

                origen_x_widget = QTableWidgetItem(str(particula.origen_x))
                origen_y_widget = QTableWidgetItem(str(particula.origen_y))
                destino_x_widget = QTableWidgetItem(str(particula.destino_x))
                destino_y_widget = QTableWidgetItem(str(particula.destino_y))
                distancia_widget = QTableWidgetItem(str(particula.distancia))

                self.ui.table.setItem(0, 0, id_widget)
                self.ui.table.setItem(0, 1, origen_x_widget)
                self.ui.table.setItem(0, 2, origen_y_widget)
                self.ui.table.setItem(0, 3, destino_x_widget)
                self.ui.table.setItem(0, 4, destino_y_widget)
                self.ui.table.setItem(0, 5, distancia_widget)

                return

        QMessageBox.warning(
            self, "Atencion", f'La particula con id "{id}" no se ha encontrado')

    @Slot()
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
