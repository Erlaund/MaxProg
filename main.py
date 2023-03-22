# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/sedoy/Desktop/MaxProg/ui/MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import * 

from DataLoad import Ui_LoadDialog

from RegrGraphic import Ui_RegrDialog
from Prediction import Ui_PredictDialog

from BalGraphics import Ui_BalDialog
from BalPredict import Ui_BalPredict

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(770, 568)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 201, 21))
        self.label.setObjectName("label")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 50, 271, 207))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 3, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 2, 1, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout.addWidget(self.lineEdit_5, 4, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 270, 751, 251))
        self.tableWidget.setObjectName("tableWidget")

        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(530, 25, 221, 171))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(520, 230, 241, 32))
        self.pushButton_5.setObjectName("pushButton_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 770, 22))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu.menuAction())
        
        self.pushButton.clicked.connect(self.clicked_button)
        self.pushButton_2.clicked.connect(self.clicked_button2)
        self.pushButton_3.clicked.connect(self.clicked_button3)
        self.pushButton_4.clicked.connect(self.clicked_button4)
        self.pushButton_5.clicked.connect(self.clicked_5)

        self.tableWidget.setColumnCount(9)
        self.tableWidget.setRowCount(8)
        self.tableWidget.setItem(0,0, QTableWidgetItem("Год"))
        self.tableWidget.setItem(0,1, QTableWidgetItem("Количество платных студентов"))
        self.tableWidget.setItem(0,2, QTableWidgetItem("Баллы ЭИС"))
        self.tableWidget.setItem(0,3, QTableWidgetItem("Баллы ЭПИ"))
        self.tableWidget.setItem(0,4, QTableWidgetItem("Количество участников ЕГЭ"))
        self.tableWidget.setItem(0,5, QTableWidgetItem("Средняя зарплата по регионам"))
        self.tableWidget.setItem(0,6, QTableWidgetItem("Рейтинг ВУЗа"))
        self.tableWidget.setItem(0,7, QTableWidgetItem("Работа преподавателя по информированию"))
        self.tableWidget.setItem(0,8, QTableWidgetItem("Возможность подавать копии документов"))

        self.tableWidget.setItem(1,0, QTableWidgetItem("2016"))
        self.tableWidget.setItem(2,0, QTableWidgetItem("2017"))
        self.tableWidget.setItem(3,0, QTableWidgetItem("2018"))
        self.tableWidget.setItem(4,0, QTableWidgetItem("2019"))
        self.tableWidget.setItem(5,0, QTableWidgetItem("2020"))

        self.tableWidget.setItem(1,1, QTableWidgetItem("217"))
        self.tableWidget.setItem(2,1, QTableWidgetItem("220"))
        self.tableWidget.setItem(3,1, QTableWidgetItem("224"))
        self.tableWidget.setItem(4,1, QTableWidgetItem("229"))
        self.tableWidget.setItem(5,1, QTableWidgetItem("233"))
    
        self.tableWidget.setItem(1,2, QTableWidgetItem("211"))
        self.tableWidget.setItem(2,2, QTableWidgetItem("215"))
        self.tableWidget.setItem(3,2, QTableWidgetItem("221"))
        self.tableWidget.setItem(4,2, QTableWidgetItem("227"))
        self.tableWidget.setItem(5,2, QTableWidgetItem("232"))

        self.tableWidget.setItem(1,3, QTableWidgetItem("211"))
        self.tableWidget.setItem(2,3, QTableWidgetItem("215"))
        self.tableWidget.setItem(3,3, QTableWidgetItem("221"))
        self.tableWidget.setItem(4,3, QTableWidgetItem("227"))
        self.tableWidget.setItem(5,3, QTableWidgetItem("232"))

        self.tableWidget.setItem(1,4, QTableWidgetItem("26658"))
        self.tableWidget.setItem(2,4, QTableWidgetItem("25489"))
        self.tableWidget.setItem(3,4, QTableWidgetItem("26970"))
        self.tableWidget.setItem(4,4, QTableWidgetItem("28208"))
        self.tableWidget.setItem(5,4, QTableWidgetItem("27519"))

        self.tableWidget.setItem(1,5, QTableWidgetItem("28206"))
        self.tableWidget.setItem(2,5, QTableWidgetItem("30414"))
        self.tableWidget.setItem(3,5, QTableWidgetItem("36610"))
        self.tableWidget.setItem(4,5, QTableWidgetItem("36610"))
        self.tableWidget.setItem(5,5, QTableWidgetItem("39084"))        

        self.tableWidget.setItem(1,6, QTableWidgetItem("10,9"))
        self.tableWidget.setItem(2,6, QTableWidgetItem("11,5"))
        self.tableWidget.setItem(3,6, QTableWidgetItem("11,9"))
        self.tableWidget.setItem(4,6, QTableWidgetItem("12,4"))
        self.tableWidget.setItem(5,6, QTableWidgetItem("11,5"))        

        self.tableWidget.setItem(1,7, QTableWidgetItem("9"))
        self.tableWidget.setItem(2,7, QTableWidgetItem("11"))
        self.tableWidget.setItem(3,7, QTableWidgetItem("9"))
        self.tableWidget.setItem(4,7, QTableWidgetItem("8"))
        self.tableWidget.setItem(5,7, QTableWidgetItem("8"))        

        self.tableWidget.setItem(1,8, QTableWidgetItem("0"))
        self.tableWidget.setItem(2,8, QTableWidgetItem("0"))
        self.tableWidget.setItem(3,8, QTableWidgetItem("0"))
        self.tableWidget.setItem(4,8, QTableWidgetItem("0"))
        self.tableWidget.setItem(5,8, QTableWidgetItem("12"))    

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">Актуальные данные</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "Рейтинг вуза"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p>Количество<br/>участников ЕГЭ</p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p>Средняя зарплата<br/>по регионам</p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p>Оценка работы <br/>преподавателя</p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p>Возможность <br/>подавать копии <br/>документов</p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Спрогнозировать \n"
"количество платных мест"))
        self.pushButton_2.setText(_translate("MainWindow", "Спрогнозировать баллы"))
        self.pushButton_3.setText(_translate("MainWindow", "Построить график \n"
"количества платных мест"))
        self.pushButton_4.setText(_translate("MainWindow", "Построить график баллов"))
        self.pushButton_5.setText(_translate("MainWindow", "Занести новые данные в таблицу"))
        self.menu.setTitle(_translate("MainWindow", "О программе"))
        self.menu_2.setTitle(_translate("MainWindow", "Файл"))

    def clicked_button(self):
        PredictDialog = Ui_PredictDialog()
        PredictDialog.setupUi(PredictDialog)
        PredictDialog.setWindowTitle("")
        PredictDialog.exec()

    def clicked_button2(self):
        BalDialog = Ui_BalPredict()
        BalDialog.setupUi(BalDialog)
        BalDialog.setWindowTitle("")
        BalDialog.exec()

    def clicked_button3(self):
        GraphicDialog = Ui_RegrDialog()
        GraphicDialog.setupUi(GraphicDialog)
        GraphicDialog.setWindowTitle("")
        GraphicDialog.exec()

    def clicked_button4(self):
        GraphicBalDialog = Ui_BalDialog()
        GraphicBalDialog.setupUi(GraphicBalDialog)
        GraphicBalDialog.setWindowTitle("")
        GraphicBalDialog.exec()

    def clicked_5(self):
        LoadDialog = Ui_LoadDialog()
        LoadDialog.setupUi(LoadDialog)
        LoadDialog.setWindowTitle("")
        LoadDialog.exec()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.setWindowTitle("")
    MainWindow.show()
    sys.exit(app.exec_())
