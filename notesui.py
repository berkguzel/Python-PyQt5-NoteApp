# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'berksnotes.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1058, 848)
        MainWindow.setStyleSheet("\n"
"background-color: rgb(58, 58, 58);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lbl_addedToday = QtWidgets.QLabel(self.centralwidget)
        self.lbl_addedToday.setGeometry(QtCore.QRect(170, 0, 231, 31))
        self.lbl_addedToday.setObjectName("lbl_addedToday")
        self.lbl_results = QtWidgets.QLabel(self.centralwidget)
        self.lbl_results.setGeometry(QtCore.QRect(550, 400, 491, 31))
        self.lbl_results.setObjectName("lbl_results")
        self.pb_search = QtWidgets.QPushButton(self.centralwidget)
        self.pb_search.setGeometry(QtCore.QRect(370, 560, 161, 31))
        self.pb_search.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.pb_search.setObjectName("pb_search")
        self.pb_markasRead = QtWidgets.QPushButton(self.centralwidget)
        self.pb_markasRead.setGeometry(QtCore.QRect(370, 250, 231, 31))
        self.pb_markasRead.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.pb_markasRead.setObjectName("pb_markasRead")
        self.pb_delete_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pb_delete_2.setGeometry(QtCore.QRect(10, 250, 151, 31))
        self.pb_delete_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);\n"
"selection-color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.pb_delete_2.setObjectName("pb_delete_2")
        self.pb_add = QtWidgets.QPushButton(self.centralwidget)
        self.pb_add.setGeometry(QtCore.QRect(10, 560, 171, 31))
        self.pb_add.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.pb_add.setObjectName("pb_add")
        self.pb_exit = QtWidgets.QPushButton(self.centralwidget)
        self.pb_exit.setGeometry(QtCore.QRect(60, 680, 211, 31))
        self.pb_exit.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.pb_exit.setObjectName("pb_exit")
        self.lbl_addedToday_4 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_addedToday_4.setGeometry(QtCore.QRect(100, 330, 261, 21))
        self.lbl_addedToday_4.setObjectName("lbl_addedToday_4")
        self.groupBox_adding = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_adding.setGeometry(QtCore.QRect(10, 370, 521, 171))
        self.groupBox_adding.setObjectName("groupBox_adding")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.groupBox_adding)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(200, 20, 211, 141))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.cb_cloudNative_2 = QtWidgets.QCheckBox(self.verticalLayoutWidget_4)
        self.cb_cloudNative_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.cb_cloudNative_2.setObjectName("cb_cloudNative_2")
        self.verticalLayout_4.addWidget(self.cb_cloudNative_2)
        self.cb_programming_2 = QtWidgets.QCheckBox(self.verticalLayoutWidget_4)
        self.cb_programming_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.cb_programming_2.setObjectName("cb_programming_2")
        self.verticalLayout_4.addWidget(self.cb_programming_2)
        self.cb_others_2 = QtWidgets.QCheckBox(self.verticalLayoutWidget_4)
        self.cb_others_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.cb_others_2.setObjectName("cb_others_2")
        self.verticalLayout_4.addWidget(self.cb_others_2)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.groupBox_adding)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 20, 151, 141))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.cb_science_2 = QtWidgets.QCheckBox(self.verticalLayoutWidget_3)
        self.cb_science_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"")
        self.cb_science_2.setObjectName("cb_science_2")
        self.verticalLayout_3.addWidget(self.cb_science_2)
        self.cb_software_2 = QtWidgets.QCheckBox(self.verticalLayoutWidget_3)
        self.cb_software_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.cb_software_2.setObjectName("cb_software_2")
        self.verticalLayout_3.addWidget(self.cb_software_2)
        self.cb_technology_2 = QtWidgets.QCheckBox(self.verticalLayoutWidget_3)
        self.cb_technology_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.cb_technology_2.setObjectName("cb_technology_2")
        self.verticalLayout_3.addWidget(self.cb_technology_2)
        self.list_addedToday = QtWidgets.QListWidget(self.centralwidget)
        self.list_addedToday.setGeometry(QtCore.QRect(15, 40, 541, 192))
        self.list_addedToday.setStyleSheet("color: rgb(255, 255, 255);")
        self.list_addedToday.setObjectName("list_addedToday")
        self.list_results = QtWidgets.QListWidget(self.centralwidget)
        self.list_results.setGeometry(QtCore.QRect(540, 440, 501, 351))
        self.list_results.setStyleSheet("color: rgb(255, 255, 255);")
        self.list_results.setObjectName("list_results")
        self.pb_edit = QtWidgets.QPushButton(self.centralwidget)
        self.pb_edit.setGeometry(QtCore.QRect(190, 250, 151, 31))
        self.pb_edit.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);\n"
"selection-color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.pb_edit.setObjectName("pb_edit")
        self.pb_delete_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pb_delete_3.setGeometry(QtCore.QRect(190, 560, 171, 31))
        self.pb_delete_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);\n"
"selection-color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.pb_delete_3.setObjectName("pb_delete_3")
        self.list_analysis = QtWidgets.QListWidget(self.centralwidget)
        self.list_analysis.setGeometry(QtCore.QRect(630, 40, 411, 291))
        self.list_analysis.setStyleSheet("color: rgb(255, 255, 255);")
        self.list_analysis.setObjectName("list_analysis")
        self.pb_search_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pb_search_2.setGeometry(QtCore.QRect(690, 340, 311, 31))
        self.pb_search_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.pb_search_2.setObjectName("pb_search_2")
        self.lbl_addedToday_3 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_addedToday_3.setGeometry(QtCore.QRect(720, 0, 231, 31))
        self.lbl_addedToday_3.setObjectName("lbl_addedToday_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1058, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lbl_addedToday.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:#00557f;\">ADDED TODAY</span></p></body></html>"))
        self.lbl_results.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:#00557f;\">RESULTS</span></p></body></html>"))
        self.pb_search.setText(_translate("MainWindow", "SEARCH"))
        self.pb_markasRead.setText(_translate("MainWindow", "MARK AS READ"))
        self.pb_delete_2.setText(_translate("MainWindow", "DELETE"))
        self.pb_add.setText(_translate("MainWindow", "ADD"))
        self.pb_exit.setText(_translate("MainWindow", "EXIT"))
        self.lbl_addedToday_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:#00557f;\">PLEASE CHOOSE FROM TAGS</span></p></body></html>"))
        self.groupBox_adding.setTitle(_translate("MainWindow", "Tags"))
        self.cb_cloudNative_2.setText(_translate("MainWindow", "Cloud Native, AWS"))
        self.cb_programming_2.setText(_translate("MainWindow", "Python, ML, Data Science"))
        self.cb_others_2.setText(_translate("MainWindow", "Others"))
        self.cb_science_2.setText(_translate("MainWindow", "Science"))
        self.cb_software_2.setText(_translate("MainWindow", "Software"))
        self.cb_technology_2.setText(_translate("MainWindow", "Technology"))
        self.pb_edit.setText(_translate("MainWindow", "EDIT"))
        self.pb_delete_3.setText(_translate("MainWindow", "DELETE"))
        self.pb_search_2.setText(_translate("MainWindow", "SEE WHAT YOU READ"))
        self.lbl_addedToday_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:#00557f;\">READ ANALYSIS</span></p></body></html>"))
