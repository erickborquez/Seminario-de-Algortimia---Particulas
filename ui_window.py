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
        MainWindow.resize(470, 479)
        self.actionAbrir = QAction(MainWindow)
        self.actionAbrir.setObjectName(u"actionAbrir")
        self.actionGuardar = QAction(MainWindow)
        self.actionGuardar.setObjectName(u"actionGuardar")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(0, 0, 491, 441))
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 30, 67, 17))
        self.id_lineEdit = QLineEdit(self.groupBox)
        self.id_lineEdit.setObjectName(u"id_lineEdit")
        self.id_lineEdit.setGeometry(QRect(90, 30, 113, 25))
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 60, 67, 17))
        self.origin_x_lineEdit = QLineEdit(self.groupBox)
        self.origin_x_lineEdit.setObjectName(u"origin_x_lineEdit")
        self.origin_x_lineEdit.setGeometry(QRect(90, 60, 113, 25))
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 90, 67, 17))
        self.origin_y_lineEdit = QLineEdit(self.groupBox)
        self.origin_y_lineEdit.setObjectName(u"origin_y_lineEdit")
        self.origin_y_lineEdit.setGeometry(QRect(90, 90, 113, 25))
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 120, 67, 17))
        self.dest_x_lineEdit = QLineEdit(self.groupBox)
        self.dest_x_lineEdit.setObjectName(u"dest_x_lineEdit")
        self.dest_x_lineEdit.setGeometry(QRect(90, 120, 113, 25))
        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 150, 67, 17))
        self.dest_y_lineEdit = QLineEdit(self.groupBox)
        self.dest_y_lineEdit.setObjectName(u"dest_y_lineEdit")
        self.dest_y_lineEdit.setGeometry(QRect(90, 150, 113, 25))
        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 180, 67, 17))
        self.velocity_lineEdit = QLineEdit(self.groupBox)
        self.velocity_lineEdit.setObjectName(u"velocity_lineEdit")
        self.velocity_lineEdit.setGeometry(QRect(90, 180, 113, 25))
        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(20, 210, 67, 17))
        self.green_lineEdit = QLineEdit(self.groupBox)
        self.green_lineEdit.setObjectName(u"green_lineEdit")
        self.green_lineEdit.setGeometry(QRect(90, 270, 113, 25))
        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(20, 240, 67, 17))
        self.red_lineEdit = QLineEdit(self.groupBox)
        self.red_lineEdit.setObjectName(u"red_lineEdit")
        self.red_lineEdit.setGeometry(QRect(90, 240, 113, 25))
        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(20, 270, 67, 17))
        self.blue_lineEdit = QLineEdit(self.groupBox)
        self.blue_lineEdit.setObjectName(u"blue_lineEdit")
        self.blue_lineEdit.setGeometry(QRect(90, 300, 113, 25))
        self.label_10 = QLabel(self.groupBox)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(20, 300, 67, 17))
        self.plainTextEdit = QPlainTextEdit(self.groupBox)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(210, 30, 251, 401))
        self.layoutWidget = QWidget(self.groupBox)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 340, 181, 89))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.add_start_pushButton = QPushButton(self.layoutWidget)
        self.add_start_pushButton.setObjectName(u"add_start_pushButton")

        self.verticalLayout.addWidget(self.add_start_pushButton)

        self.add_end_pushButton = QPushButton(self.layoutWidget)
        self.add_end_pushButton.setObjectName(u"add_end_pushButton")

        self.verticalLayout.addWidget(self.add_end_pushButton)

        self.print_pushButton = QPushButton(self.layoutWidget)
        self.print_pushButton.setObjectName(u"print_pushButton")

        self.verticalLayout.addWidget(self.print_pushButton)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 470, 22))
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
        self.blue_lineEdit.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Azul", None))
        self.add_start_pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar al inicio", None))
        self.add_end_pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar al final", None))
        self.print_pushButton.setText(QCoreApplication.translate("MainWindow", u"Imprimir", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
    # retranslateUi

