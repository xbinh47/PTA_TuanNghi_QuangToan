# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'register.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 554)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 301, 561))
        self.label.setPixmap(QPixmap(u"../../../../Desktop/costume1.svg"))
        self.label.setScaledContents(True)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(180, 0, 741, 561))
        self.label_2.setStyleSheet(u"border_radius: 20px")
        self.label_2.setPixmap(QPixmap(u"../../../../Desktop/costume2.svg"))
        self.label_2.setScaledContents(True)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(390, 0, 331, 91))
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        self.label_3.setPalette(palette)
        font = QFont()
        font.setFamilies([u"Fredoka One"])
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(0, 170, 291, 31))
        self.textEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 0px solid;\n"
"border-radius: 10px;")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(0, 130, 221, 31))
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        self.label_4.setPalette(palette1)
        font1 = QFont()
        font1.setFamilies([u"Fredoka One"])
        font1.setPointSize(18)
        self.label_4.setFont(font1)
        self.textEdit_2 = QTextEdit(self.centralwidget)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setGeometry(QRect(0, 270, 291, 31))
        self.textEdit_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 0px solid;\n"
"border-radius: 10px;")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(0, 230, 221, 31))
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        self.label_5.setPalette(palette2)
        self.label_5.setFont(font1)
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(0, 320, 221, 31))
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        self.label_6.setPalette(palette3)
        self.label_6.setFont(font1)
        self.textEdit_3 = QTextEdit(self.centralwidget)
        self.textEdit_3.setObjectName(u"textEdit_3")
        self.textEdit_3.setGeometry(QRect(0, 360, 291, 31))
        self.textEdit_3.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 0px solid;\n"
"border-radius: 10px;")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(60, 450, 151, 51))
        palette4 = QPalette()
        brush1 = QBrush(QColor(255, 255, 127, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette4.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette4.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        self.pushButton.setPalette(palette4)
        self.pushButton.setFont(font)
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 20, 101, 91))
        self.label_7.setPixmap(QPixmap(u"../../../../Downloads/costume1.svg"))
        self.label_7.setScaledContents(True)
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(130, 40, 131, 31))
        palette5 = QPalette()
        palette5.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        self.label_8.setPalette(palette5)
        self.label_8.setFont(font1)
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(130, 70, 131, 31))
        palette6 = QPalette()
        palette6.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        self.label_9.setPalette(palette6)
        self.label_9.setFont(font1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.label_2.raise_()
        self.label.raise_()
        self.label_3.raise_()
        self.textEdit.raise_()
        self.label_4.raise_()
        self.textEdit_2.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.textEdit_3.raise_()
        self.pushButton.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.label_9.raise_()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Create your account", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Name:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Password:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Email:", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Create", None))
        self.label_7.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Forecast", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Pro", None))
    # retranslateUi

