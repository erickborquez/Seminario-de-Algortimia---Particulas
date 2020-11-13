# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'particulas.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(859, 577)
        self.actionAbrir = QAction(MainWindow)
        self.actionAbrir.setObjectName(u"actionAbrir")
        self.actionGuardar = QAction(MainWindow)
        self.actionGuardar.setObjectName(u"actionGuardar")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout = QGridLayout(self.tab)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.id_lineEdit = QLineEdit(self.groupBox)
        self.id_lineEdit.setObjectName(u"id_lineEdit")

        self.gridLayout_2.addWidget(self.id_lineEdit, 0, 1, 1, 1)

        self.plainTextEdit = QPlainTextEdit(self.groupBox)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

        self.gridLayout_2.addWidget(self.plainTextEdit, 0, 2, 11, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)

        self.origin_x_lineEdit = QLineEdit(self.groupBox)
        self.origin_x_lineEdit.setObjectName(u"origin_x_lineEdit")

        self.gridLayout_2.addWidget(self.origin_x_lineEdit, 1, 1, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)

        self.origin_y_lineEdit = QLineEdit(self.groupBox)
        self.origin_y_lineEdit.setObjectName(u"origin_y_lineEdit")

        self.gridLayout_2.addWidget(self.origin_y_lineEdit, 2, 1, 1, 1)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 3, 0, 1, 1)

        self.dest_x_lineEdit = QLineEdit(self.groupBox)
        self.dest_x_lineEdit.setObjectName(u"dest_x_lineEdit")

        self.gridLayout_2.addWidget(self.dest_x_lineEdit, 3, 1, 1, 1)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 4, 0, 1, 1)

        self.dest_y_lineEdit = QLineEdit(self.groupBox)
        self.dest_y_lineEdit.setObjectName(u"dest_y_lineEdit")

        self.gridLayout_2.addWidget(self.dest_y_lineEdit, 4, 1, 1, 1)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 5, 0, 1, 1)

        self.velocity_lineEdit = QLineEdit(self.groupBox)
        self.velocity_lineEdit.setObjectName(u"velocity_lineEdit")

        self.gridLayout_2.addWidget(self.velocity_lineEdit, 5, 1, 1, 1)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_2.addWidget(self.label_7, 6, 0, 1, 1)

        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_2.addWidget(self.label_8, 7, 0, 1, 1)

        self.red_lineEdit = QLineEdit(self.groupBox)
        self.red_lineEdit.setObjectName(u"red_lineEdit")

        self.gridLayout_2.addWidget(self.red_lineEdit, 7, 1, 1, 1)

        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_2.addWidget(self.label_9, 8, 0, 1, 1)

        self.green_lineEdit = QLineEdit(self.groupBox)
        self.green_lineEdit.setObjectName(u"green_lineEdit")

        self.gridLayout_2.addWidget(self.green_lineEdit, 8, 1, 1, 1)

        self.label_10 = QLabel(self.groupBox)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_2.addWidget(self.label_10, 9, 0, 1, 1)

        self.blue_lineEdit = QLineEdit(self.groupBox)
        self.blue_lineEdit.setObjectName(u"blue_lineEdit")

        self.gridLayout_2.addWidget(self.blue_lineEdit, 9, 1, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.add_start_pushButton = QPushButton(self.groupBox)
        self.add_start_pushButton.setObjectName(u"add_start_pushButton")

        self.verticalLayout.addWidget(self.add_start_pushButton)

        self.add_end_pushButton = QPushButton(self.groupBox)
        self.add_end_pushButton.setObjectName(u"add_end_pushButton")

        self.verticalLayout.addWidget(self.add_end_pushButton)

        self.print_pushButton = QPushButton(self.groupBox)
        self.print_pushButton.setObjectName(u"print_pushButton")

        self.verticalLayout.addWidget(self.print_pushButton)


        self.gridLayout_2.addLayout(self.verticalLayout, 10, 0, 1, 2)


        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_4 = QGridLayout(self.tab_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.search_line = QLineEdit(self.tab_2)
        self.search_line.setObjectName(u"search_line")

        self.gridLayout_4.addWidget(self.search_line, 1, 0, 1, 1)

        self.search_button = QPushButton(self.tab_2)
        self.search_button.setObjectName(u"search_button")

        self.gridLayout_4.addWidget(self.search_button, 1, 1, 1, 1)

        self.show_button = QPushButton(self.tab_2)
        self.show_button.setObjectName(u"show_button")

        self.gridLayout_4.addWidget(self.show_button, 1, 2, 1, 1)

        self.table = QTableWidget(self.tab_2)
        self.table.setObjectName(u"table")

        self.gridLayout_4.addWidget(self.table, 0, 0, 1, 3)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_5 = QGridLayout(self.tab_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.graphicsView = QGraphicsView(self.tab_3)
        self.graphicsView.setObjectName(u"graphicsView")

        self.gridLayout_5.addWidget(self.graphicsView, 0, 0, 1, 1)

        self.draw_button = QPushButton(self.tab_3)
        self.draw_button.setObjectName(u"draw_button")

        self.gridLayout_5.addWidget(self.draw_button, 1, 0, 1, 1)

        self.tabWidget.addTab(self.tab_3, "")

        self.gridLayout_3.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 859, 22))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menuArchivo.addAction(self.actionAbrir)
        self.menuArchivo.addAction(self.actionGuardar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionAbrir.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
#if QT_CONFIG(shortcut)
        self.actionAbrir.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionGuardar.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
#if QT_CONFIG(shortcut)
        self.actionGuardar.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Particulas", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Id", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Origen X", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Origen Y", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Destino X", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Destino Y", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Velocidad", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Color RGB", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Rojo", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Verde", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Azul", None))
        self.blue_lineEdit.setText("")
        self.add_start_pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar al inicio", None))
        self.add_end_pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar al final", None))
        self.print_pushButton.setText(QCoreApplication.translate("MainWindow", u"Imprimir", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.search_line.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Id de la particula", None))
        self.search_button.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.show_button.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tabla", None))
        self.draw_button.setText(QCoreApplication.translate("MainWindow", u"Dibujar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Dibujar", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
    # retranslateUi

