from PyQt5 import QtCore, QtGui, QtWidgets
import Caeser
import Polybius
import ROT13
import Affine
import Null
import Atbash
import Vigenere
import Stream
import Hill
import Playfair
import TwoSquarec
import FourSquare
import Bifid
import ADFGX
import ADFGVX
import  ReverseOrder
import Geometric
import RailFence
import Columnar
import AES
import DES

class Ui_MainWindow(object):

    def gotoDES(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.add = DES.Ui_Dialog()
        self.add.setupUi(self.MainWindow)
        self.MainWindow.show()

    def gotoAES(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.add = AES.Ui_Dialog()
        self.add.setupUi(self.MainWindow)
        self.MainWindow.show()

    def gotoColumnar(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.add = Columnar.Ui_Dialog()
        self.add.setupUi(self.MainWindow)
        self.MainWindow.show()
    def gotoRailFence(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.add = RailFence.Ui_Dialog()
        self.add.setupUi(self.MainWindow)
        self.MainWindow.show()
    def gotoReverseOrder(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.add = ReverseOrder.Ui_Dialog()
        self.add.setupUi(self.MainWindow)
        self.MainWindow.show()
    def gotoGeometric(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.add = Geometric.Ui_Dialog()
        self.add.setupUi(self.MainWindow)
        self.MainWindow.show()
    def gotoADFGVX(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.add = ADFGVX.Ui_Dialog()
        self.add.setupUi(self.MainWindow)
        self.MainWindow.show()
    def gotoADFGX(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.add = ADFGX.Ui_Dialog()
        self.add.setupUi(self.MainWindow)
        self.MainWindow.show()

    def gotoBifid(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.add = Bifid.Ui_Dialog()
        self.add.setupUi(self.MainWindow)
        self.MainWindow.show()

    def gotoFourSquare(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.add = FourSquare.Ui_Dialog()
        self.add.setupUi(self.MainWindow)
        self.MainWindow.show()
    def gotoTwoSquare(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.add = TwoSquarec.Ui_Dialog()
        self.add.setupUi(self.MainWindow)
        self.MainWindow.show()

    def gotoPlayfair(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.add = Playfair.Ui_Dialog()
        self.add.setupUi(self.MainWindow)
        self.MainWindow.show()

    def gotoVigenere(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.add = Vigenere.Ui_Dialog()
        self.add.setupUi(self.MainWindow)
        self.MainWindow.show()

    def gotoHill(self):
            self.MainWindow = QtWidgets.QMainWindow()
            self.add = Hill.Ui_Dialog()
            self.add.setupUi(self.MainWindow)
            self.MainWindow.show()

    def gotoStream(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.add = Stream.Ui_Dialog()
        self.add.setupUi(self.MainWindow)
        self.MainWindow.show()

    def gotoAtbash(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.add = Atbash.Ui_Dialog()
        self.add.setupUi(self.MainWindow)
        self.MainWindow.show()

    def gotoAffine(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.add = Affine.Ui_Dialog()
        self.add.setupUi(self.MainWindow)
        self.MainWindow.show()
    def gotoNull(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.add = Null.Ui_Dialog()
        self.add.setupUi(self.MainWindow)
        self.MainWindow.show()
    def gotoROT(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.add = ROT13.Ui_Dialog()
        self.add.setupUi(self.MainWindow)
        self.MainWindow.show()

    def gotopolybius(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.add = Polybius.Ui_Dialog()
        self.add.setupUi(self.MainWindow)
        self.MainWindow.show()

    def gotocaesar(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.add = Caeser.Ui_Dialog()
        self.add.setupUi(self.MainWindow)
        self.MainWindow.show()


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1171, 735)
        MainWindow.setMinimumSize(QtCore.QSize(1171, 735))
        MainWindow.setMaximumSize(QtCore.QSize(1171, 735))
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1171, 71))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        self.frame.setFont(font)
        self.frame.setStyleSheet("QFrame{\n"
"\n"
"    background-color: rgb(34, 51, 99);\n"
"    border-bottom: 2px solid #000;\n"
"}\n"
"\n"
"\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(0, 10, 171, 61))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        self.label.setFont(font)
        self.label.setStyleSheet("image: url(:/Logo/LogoMakr-2b8XDd.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(410, 10, 641, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: white;\n"
"border-bottom:none;")
        self.label_2.setObjectName("label_2")
        self.left_nav = QtWidgets.QFrame(self.centralwidget)
        self.left_nav.setGeometry(QtCore.QRect(0, 70, 121, 671))
        self.left_nav.setAutoFillBackground(False)
        self.left_nav.setStyleSheet("\n"
"background-color: rgb(34, 51, 99);\n"
"\n"
"")
        self.left_nav.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.left_nav.setFrameShadow(QtWidgets.QFrame.Raised)
        self.left_nav.setObjectName("left_nav")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.left_nav)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame_2 = QtWidgets.QFrame(self.left_nav)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_4.setMaximumSize(QtCore.QSize(80, 85))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("QPushButton#pushButton_4{\n"
"    border-image: url(:/icons/About.png);\n"
"padding:5px 10px;\n"
"border: none;\n"
"border-radius: 10px;\n"
"background-color: 223363;\n"
"color:white\n"
"}\n"
"\n"
"\n"
"QPushButton#pushButton_4:hover{\n"
"    background-color: rgb(170, 170, 255);\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 3, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_2.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton#pushButton_2{\n"
"    border-image: url(:/icons/LogoMakr-7LUqSV.png);\n"
"padding:5px 10px;\n"
"border: none;\n"
"border-radius: 10px;\n"
"background-color: 223363;\n"
"color:white\n"
"}\n"
"\n"
"\n"
"QPushButton#pushButton_2:hover{\n"
"    background-color: rgb(170, 170, 255);\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 1, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_3.setMaximumSize(QtCore.QSize(80, 85))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton#pushButton_3{\n"
"    border-image: url(:/icons/Block.png);\n"
"padding:5px 10px;\n"
"border: none;\n"
"border-radius: 10px;\n"
"background-color: 223363;\n"
"color:white\n"
"}\n"
"\n"
"\n"
"QPushButton#pushButton_3:hover{\n"
"    background-color: rgb(170, 170, 255);\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 2, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(True)
        self.pushButton.setFont(font)
        self.pushButton.setTabletTracking(False)
        self.pushButton.setStyleSheet("QPushButton#pushButton{\n"
"    border-image: url(:/icons/LogoMakr-96e2nm.png);\n"
"padding:5px 10px;\n"
"border: none;\n"
"border-radius: 10px;\n"
"background-color: #223363;\n"
"color:white\n"
"    \n"
"}\n"
"    \n"
"\n"
"QPushButton#pushButton:hover{\n"
"    \n"
"    background-color: rgb(170, 170, 255);\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame_2, 0, 0, 1, 1)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(129, 79, 1041, 661))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_3)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 1041, 651))
        self.stackedWidget.setStyleSheet("")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.label_13 = QtWidgets.QLabel(self.page)
        self.label_13.setGeometry(QtCore.QRect(380, 100, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("color: #223363;\n"
"border-bottom:none;")
        self.label_13.setObjectName("label_13")
        self.pushButton_7 = QtWidgets.QPushButton(self.page)
        self.pushButton_7.setGeometry(QtCore.QRect(600, 200, 261, 241))
        self.pushButton_7.setStyleSheet("QPushButton#pushButton_7{\n"
"    border-image: url(:/newPrefix/poly.png);\n"
"padding:5px 10px;\n"
"border: none;\n"
"border-radius: 20px;\n"
"color:white\n"
"    \n"
"}\n"
"    \n"
"\n"
"QPushButton#pushButton_7:hover{\n"
"    \n"
"    background-color: rgb(170, 170, 255);\n"
"\n"
"}\n"
"")
        self.pushButton_7.setText("")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_5 = QtWidgets.QPushButton(self.page)
        self.pushButton_5.setGeometry(QtCore.QRect(150, 200, 231, 261))
        self.pushButton_5.setStyleSheet("QPushButton#pushButton_5{\n"
"    border-image: url(:/newPrefix/mono.png);\n"
"padding:5px 10px;\n"
"border: none;\n"
"border-radius: 20px;\n"
"color:white\n"
"    \n"
"}\n"
"    \n"
"\n"
"QPushButton#pushButton_5:hover{\n"
"    \n"
"    background-color: rgb(170, 170, 255);\n"
"\n"
"}\n"
"")
        self.pushButton_5.setText("")
        self.pushButton_5.setObjectName("pushButton_5")
        self.stackedWidget.addWidget(self.page)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.pushButton_6 = QtWidgets.QPushButton(self.page_3)
        self.pushButton_6.setGeometry(QtCore.QRect(100, 120, 201, 201))
        self.pushButton_6.setStyleSheet("QPushButton#pushButton_6{\n"
"    border-image: url(:/newPrefix/caesar.png);\n"
"    border-image: url(:/newPrefix/Caesar.png);\n"
"padding:5px 10px;\n"
"border: none;\n"
"border-radius: 20px;\n"
"color:white\n"
"    \n"
"}\n"
"    \n"
"\n"
"QPushButton#pushButton_6:hover{\n"
"    \n"
"    background-color: rgb(170, 170, 255);\n"
"\n"
"}\n"
"")
        self.pushButton_6.setText("")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(self.gotocaesar)
        self.label_14 = QtWidgets.QLabel(self.page_3)
        self.label_14.setGeometry(QtCore.QRect(360, 40, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("color: #223363;\n"
"border-bottom:none;")
        self.label_14.setObjectName("label_14")
        self.pushButton_21 = QtWidgets.QPushButton(self.page_3)
        self.pushButton_21.setGeometry(QtCore.QRect(400, 120, 201, 201))
        self.pushButton_21.setStyleSheet("QPushButton#pushButton_21{\n"
"    border-image: url(:/newPrefix/ROT13.png);\n"
"padding:5px 10px;\n"
"border: none;\n"
"border-radius: 20px;\n"
"color:white\n"
"    \n"
"}\n"
"    \n"
"\n"
"QPushButton#pushButton_21:hover{\n"
"    \n"
"    background-color: rgb(170, 170, 255);\n"
"\n"
"}\n"
"")
        self.pushButton_21.setText("")
        self.pushButton_21.setObjectName("pushButton_21")
        self.pushButton_21.clicked.connect(self.gotoROT)
        self.pushButton_22 = QtWidgets.QPushButton(self.page_3)
        self.pushButton_22.setGeometry(QtCore.QRect(100, 370, 201, 201))
        self.pushButton_22.setStyleSheet("QPushButton#pushButton_22{\n"
"    border-image: url(:/newPrefix/polybius.png);\n"
"padding:5px 10px;\n"
"border: none;\n"
"border-radius: 20px;\n"
"color:white\n"
"    \n"
"}\n"
"    \n"
"\n"
"QPushButton#pushButton_22:hover{\n"
"    \n"
"    background-color: rgb(170, 170, 255);\n"
"\n"
"}\n"
"")
        self.pushButton_22.setText("")
        self.pushButton_22.setObjectName("pushButton_22")
        self.pushButton_22.clicked.connect(self.gotopolybius)
        self.pushButton_25 = QtWidgets.QPushButton(self.page_3)
        self.pushButton_25.setGeometry(QtCore.QRect(400, 360, 201, 201))
        self.pushButton_25.setStyleSheet("QPushButton#pushButton_25{\n"
"    border-image: url(:/newPrefix/null.png);\n"
"padding:5px 10px;\n"
"border: none;\n"
"border-radius: 20px;\n"
"color:white\n"
"    \n"
"}\n"
"    \n"
"\n"
"QPushButton#pushButton_25:hover{\n"
"    \n"
"    background-color: rgb(170, 170, 255);\n"
"\n"
"}\n"
"")
        self.pushButton_25.setText("")
        self.pushButton_25.setObjectName("pushButton_25")
        self.pushButton_25.clicked.connect(self.gotoNull)
        self.pushButton_27 = QtWidgets.QPushButton(self.page_3)
        self.pushButton_27.setGeometry(QtCore.QRect(700, 340, 201, 201))
        self.pushButton_27.setStyleSheet("QPushButton#pushButton_27{\n"
"    border-image: url(:/newPrefix/affine.png);\n"
"padding:5px 10px;\n"
"border: none;\n"
"border-radius: 20px;\n"
"color:white\n"
"    \n"
"}\n"
"    \n"
"\n"
"QPushButton#pushButton_27:hover{\n"
"    \n"
"    background-color: rgb(170, 170, 255);\n"
"\n"
"}\n"
"")
        self.pushButton_27.setText("")
        self.pushButton_27.setObjectName("pushButton_27")
        self.pushButton_27.clicked.connect(self.gotoAffine)
        self.pushButton_28 = QtWidgets.QPushButton(self.page_3)
        self.pushButton_28.setGeometry(QtCore.QRect(700, 100, 201, 201))
        self.pushButton_28.setStyleSheet("QPushButton#pushButton_28{\n"
"    border-image: url(:/newPrefix/atbash.png);\n"
"padding:5px 10px;\n"
"border: none;\n"
"border-radius: 20px;\n"
"color:white\n"
"    \n"
"}\n"
"    \n"
"\n"
"QPushButton#pushButton_28:hover{\n"
"    \n"
"    background-color: rgb(170, 170, 255);\n"
"\n"
"}\n"
"")
        self.pushButton_28.setText("")
        self.pushButton_28.setObjectName("pushButton_28")
        self.pushButton_28.clicked.connect(self.gotoAtbash)
        self.pushButton_36 = QtWidgets.QPushButton(self.page_3)
        self.pushButton_36.setGeometry(QtCore.QRect(40, 20, 51, 51))
        self.pushButton_36.setStyleSheet("QPushButton#pushButton_36{\n"
"    border-image: url(:/newPrefix/back.png);\n"
"padding:5px 10px;\n"
"border: none;\n"
"border-radius: 20px;\n"
"color:white\n"
"    \n"
"}\n"
"    \n"
"\n"
"QPushButton#pushButton_36:hover{\n"
"    \n"
"    background-color: rgb(170, 170, 255);\n"
"\n"
"}\n"
"")
        self.pushButton_36.setText("")
        self.pushButton_36.setObjectName("pushButton_36")
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.label_25 = QtWidgets.QLabel(self.page_4)
        self.label_25.setGeometry(QtCore.QRect(370, 0, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        self.label_25.setFont(font)
        self.label_25.setStyleSheet("color: #223363;\n"
"border-bottom:none;")
        self.label_25.setObjectName("label_25")
        self.pushButton_26 = QtWidgets.QPushButton(self.page_4)
        self.pushButton_26.setGeometry(QtCore.QRect(150, 60, 161, 171))
        self.pushButton_26.setStyleSheet("QPushButton#pushButton_26{\n"
"    border-image: url(:/newPrefix/vigenere.png);\n"
"padding:5px 10px;\n"
"border: none;\n"
"border-radius: 20px;\n"
"color:white\n"
"    \n"
"}\n"
"    \n"
"\n"
"QPushButton#pushButton_26:hover{\n"
"    \n"
"    background-color: rgb(170, 170, 255);\n"
"\n"
"}\n"
"")
        self.pushButton_26.setText("")
        self.pushButton_26.setObjectName("pushButton_26")
        self.pushButton_26.clicked.connect(self.gotoVigenere)
        self.pushButton_29 = QtWidgets.QPushButton(self.page_4)
        self.pushButton_29.setGeometry(QtCore.QRect(150, 260, 161, 171))
        self.pushButton_29.setStyleSheet("QPushButton#pushButton_29{\n"
"border-image: url(:/newPrefix/playfair.png);\n"
"padding:5px 10px;\n"
"border: none;\n"
"border-radius: 20px;\n"
"color:white\n"
"    \n"
"}\n"
"    \n"
"\n"
"QPushButton#pushButton_29:hover{\n"
"    \n"
"    background-color: rgb(170, 170, 255);\n"
"\n"
"}\n"
"")
        self.pushButton_29.setText("")
        self.pushButton_29.setObjectName("pushButton_29")
        self.pushButton_29.clicked.connect(self.gotoPlayfair)
        self.pushButton_30 = QtWidgets.QPushButton(self.page_4)
        self.pushButton_30.setGeometry(QtCore.QRect(420, 60, 161, 171))
        self.pushButton_30.setStyleSheet("QPushButton#pushButton_30{\n"
"    border-image: url(:/newPrefix/doublesquare.png);\n"
"padding:5px 10px;\n"
"border: none;\n"
"border-radius: 20px;\n"
"color:white\n"
"    \n"
"}\n"
"    \n"
"\n"
"QPushButton#pushButton_30:hover{\n"
"    \n"
"    background-color: rgb(170, 170, 255);\n"
"\n"
"}\n"
"")
        self.pushButton_30.setText("")
        self.pushButton_30.setObjectName("pushButton_30")
        self.pushButton_30.clicked.connect(self.gotoTwoSquare)
        self.pushButton_31 = QtWidgets.QPushButton(self.page_4)
        self.pushButton_31.setGeometry(QtCore.QRect(410, 260, 161, 171))
        self.pushButton_31.setStyleSheet("QPushButton#pushButton_31{\n"
"    border-image: url(:/newPrefix/foursquare.png);\n"
"padding:5px 10px;\n"
"border: none;\n"
"border-radius: 20px;\n"
"color:white\n"
"    \n"
"}\n"
"    \n"
"\n"
"QPushButton#pushButton_31:hover{\n"
"    \n"
"    background-color: rgb(170, 170, 255);\n"
"\n"
"}\n"
"")
        self.pushButton_31.setText("")
        self.pushButton_31.setObjectName("pushButton_31")
        self.pushButton_31.clicked.connect(self.gotoFourSquare)

        self.pushButton_32 = QtWidgets.QPushButton(self.page_4)
        self.pushButton_32.setGeometry(QtCore.QRect(690, 50, 161, 171))
        self.pushButton_32.setStyleSheet("QPushButton#pushButton_32{\n"
"    border-image: url(:/newPrefix/hill.png);\n"
"padding:5px 10px;\n"
"border: none;\n"
"border-radius: 20px;\n"
"color:white\n"
"    \n"
"}\n"
"    \n"
"\n"
"QPushButton#pushButton_32:hover{\n"
"    \n"
"    background-color: rgb(170, 170, 255);\n"
"\n"
"}\n"
"")
        self.pushButton_32.setText("")
        self.pushButton_32.setObjectName("pushButton_32")
        self.pushButton_32.clicked.connect(self.gotoHill)
        self.pushButton_33 = QtWidgets.QPushButton(self.page_4)
        self.pushButton_33.setGeometry(QtCore.QRect(700, 260, 161, 171))
        self.pushButton_33.setStyleSheet("QPushButton#pushButton_33{\n"
"    border-image: url(:/newPrefix/ADFGX.png);\n"
"padding:5px 10px;\n"
"border: none;\n"
"border-radius: 20px;\n"
"color:white\n"
"    \n"
"}\n"
"    \n"
"\n"
"QPushButton#pushButton_33:hover{\n"
"    \n"
"    background-color: rgb(170, 170, 255);\n"
"\n"
"}\n"
"")
        self.pushButton_33.setText("")
        self.pushButton_33.setObjectName("pushButton_33")
        self.pushButton_33.clicked.connect(self.gotoADFGX)
        self.pushButton_34 = QtWidgets.QPushButton(self.page_4)
        self.pushButton_34.setGeometry(QtCore.QRect(150, 450, 161, 171))
        self.pushButton_34.setStyleSheet("QPushButton#pushButton_34{\n"
"    border-image: url(:/newPrefix/stream.png);\n"
"padding:5px 10px;\n"
"border: none;\n"
"border-radius: 20px;\n"
"color:white\n"
"    \n"
"}\n"
"    \n"
"\n"
"QPushButton#pushButton_34:hover{\n"
"    \n"
"    background-color: rgb(170, 170, 255);\n"
"\n"
"}\n"
"")
        self.pushButton_34.setText("")
        self.pushButton_34.setObjectName("pushButton_34")
        self.pushButton_34.clicked.connect(self.gotoStream)
        self.pushButton_35 = QtWidgets.QPushButton(self.page_4)
        self.pushButton_35.setGeometry(QtCore.QRect(420, 450, 161, 171))
        self.pushButton_35.setStyleSheet("QPushButton#pushButton_35{\n"
"    border-image: url(:/newPrefix/ADFGVX.png);\n"
"padding:5px 10px;\n"
"border: none;\n"
"border-radius: 20px;\n"
"color:white\n"
"    \n"
"}\n"
"    \n"
"\n"
"QPushButton#pushButton_35:hover{\n"
"    \n"
"    background-color: rgb(170, 170, 255);\n"
"\n"
"}\n"
"")
        self.pushButton_35.setText("")
        self.pushButton_35.setObjectName("pushButton_35")
        self.pushButton_35.clicked.connect(self.gotoADFGVX)
        self.pushButton_37 = QtWidgets.QPushButton(self.page_4)
        self.pushButton_37.setGeometry(QtCore.QRect(30, 20, 51, 51))
        self.pushButton_37.setStyleSheet("QPushButton#pushButton_37{\n"
"    border-image: url(:/newPrefix/back.png);\n"
"padding:5px 10px;\n"
"border: none;\n"
"border-radius: 20px;\n"
"color:white\n"
"    \n"
"}\n"
"    \n"
"\n"
"QPushButton#pushButton_37:hover{\n"
"    \n"
"    background-color: rgb(170, 170, 255);\n"
"\n"
"}\n"
"")
        self.pushButton_37.setText("")
        self.pushButton_37.setObjectName("pushButton_37")
        self.pushButton_38 = QtWidgets.QPushButton(self.page_4)
        self.pushButton_38.setGeometry(QtCore.QRect(710, 450, 161, 171))
        self.pushButton_38.setStyleSheet("QPushButton#pushButton_38{\n"
"    border-image: url(:/newPrefix/bifid.png);\n"
"padding:5px 10px;\n"
"border: none;\n"
"border-radius: 20px;\n"
"color:white\n"
"    \n"
"}\n"
"    \n"
"\n"
"QPushButton#pushButton_38:hover{\n"
"    \n"
"    background-color: rgb(170, 170, 255);\n"
"\n"
"}\n"
"")
        self.pushButton_38.setText("")
        self.pushButton_38.setObjectName("pushButton_38")
        self.pushButton_38.clicked.connect(self.gotoBifid)
        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.label_17 = QtWidgets.QLabel(self.page_5)
        self.label_17.setGeometry(QtCore.QRect(390, 20, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("color: #223363;\n"
"border-bottom:none;")
        self.label_17.setObjectName("label_17")
        self.pushButton_11 = QtWidgets.QPushButton(self.page_5)
        self.pushButton_11.setGeometry(QtCore.QRect(140, 90, 241, 241))
        self.pushButton_11.setStyleSheet("QPushButton#pushButton_11{\n"
"    border-image: url(:/newPrefix/reverseOrder.png);\n"
"padding:5px 10px;\n"
"border: none;\n"
"border-radius: 20px;\n"
"color:white\n"
"    \n"
"}\n"
"    \n"
"\n"
"QPushButton#pushButton_11:hover{\n"
"    \n"
"    background-color: rgb(170, 170, 255);\n"
"\n"
"}\n"
"")
        self.pushButton_11.setText("")
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_11.clicked.connect(self.gotoReverseOrder)
        self.pushButton_14 = QtWidgets.QPushButton(self.page_5)
        self.pushButton_14.setGeometry(QtCore.QRect(610, 90, 241, 241))
        self.pushButton_14.setStyleSheet("QPushButton#pushButton_14{\n"
"    border-image: url(:/newPrefix/geometric.png);\n"
"padding:5px 10px;\n"
"border: none;\n"
"border-radius: 20px;\n"
"color:white\n"
"    \n"
"}\n"
"    \n"
"\n"
"QPushButton#pushButton_14:hover{\n"
"    \n"
"    background-color: rgb(170, 170, 255);\n"
"\n"
"}\n"
"")
        self.pushButton_14.setText("")
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_14.clicked.connect(self.gotoGeometric)
        self.pushButton_15 = QtWidgets.QPushButton(self.page_5)
        self.pushButton_15.setGeometry(QtCore.QRect(140, 370, 241, 241))
        self.pushButton_15.setStyleSheet("QPushButton#pushButton_15{\n"
"    border-image: url(:/newPrefix/RailFence.png);\n"
"padding:5px 10px;\n"
"border: none;\n"
"border-radius: 20px;\n"
"color:white\n"
"    \n"
"}\n"
"    \n"
"\n"
"QPushButton#pushButton_15:hover{\n"
"    \n"
"    background-color: rgb(170, 170, 255);\n"
"\n"
"}\n"
"")
        self.pushButton_15.setText("")
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_15.clicked.connect(self.gotoRailFence)
        self.pushButton_23 = QtWidgets.QPushButton(self.page_5)
        self.pushButton_23.setGeometry(QtCore.QRect(610, 370, 241, 241))
        self.pushButton_23.setStyleSheet("QPushButton#pushButton_23{\n"
"    border-image: url(:/newPrefix/columnar.png);\n"
"padding:5px 10px;\n"
"border: none;\n"
"border-radius: 20px;\n"
"color:white\n"
"    \n"
"}\n"
"    \n"
"\n"
"QPushButton#pushButton_23:hover{\n"
"    \n"
"    background-color: rgb(170, 170, 255);\n"
"\n"
"}\n"
"")
        self.pushButton_23.setText("")
        self.pushButton_23.setObjectName("pushButton_23")
        self.pushButton_23.clicked.connect(self.gotoColumnar)
        self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.label_3 = QtWidgets.QLabel(self.page_6)
        self.label_3.setGeometry(QtCore.QRect(370, 100, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: #223363;\n"
"border-bottom:none;")
        self.label_3.setObjectName("label_3")
        self.pushButton_8 = QtWidgets.QPushButton(self.page_6)
        self.pushButton_8.setGeometry(QtCore.QRect(150, 200, 231, 241))
        self.pushButton_8.setStyleSheet("QPushButton#pushButton_8{\n"
"    border-image: url(:/newPrefix/DES.png);\n"
"padding:5px 10px;\n"
"border: none;\n"
"border-radius: 20px;\n"
"color:white\n"
"    \n"
"}\n"
"    \n"
"\n"
"QPushButton#pushButton_8:hover{\n"
"    \n"
"    background-color: rgb(170, 170, 255);\n"
"\n"
"}\n"
"")
        self.pushButton_8.setText("")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_8.clicked.connect(self.gotoDES)
        self.pushButton_12 = QtWidgets.QPushButton(self.page_6)
        self.pushButton_12.setGeometry(QtCore.QRect(620, 190, 231, 241))
        self.pushButton_12.setStyleSheet("QPushButton#pushButton_12{\n"
"    border-image: url(:/newPrefix/AES.png);\n"
"padding:5px 10px;\n"
"border: none;\n"
"border-radius: 20px;\n"
"color:white\n"
"    \n"
"}\n"
"    \n"
"\n"
"QPushButton#pushButton_12:hover{\n"
"    \n"
"    background-color: rgb(170, 170, 255);\n"
"\n"
"}\n"
"")
        self.pushButton_12.setText("")
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_12.clicked.connect(self.gotoAES)
        self.stackedWidget.addWidget(self.page_6)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.label_20 = QtWidgets.QLabel(self.page_2)
        self.label_20.setGeometry(QtCore.QRect(420, 70, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(22)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("color: #223363;\n"
"border-bottom:none;")
        self.label_20.setObjectName("label_20")
        self.label_4 = QtWidgets.QLabel(self.page_2)
        self.label_4.setGeometry(QtCore.QRect(80, 140, 751, 431))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("\n"
"color: rgb(132, 132, 132);\n"
"color: rgb(122, 122, 122);")
        self.label_4.setObjectName("label_4")
        self.label_15 = QtWidgets.QLabel(self.page_2)
        self.label_15.setGeometry(QtCore.QRect(860, 130, 101, 131))
        self.label_15.setStyleSheet("border-image: url(:/newPrefix/Lock.png);")
        self.label_15.setText("")
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.page_2)
        self.label_16.setGeometry(QtCore.QRect(860, 360, 101, 141))
        self.label_16.setStyleSheet("border-image: url(:/newPrefix/LogoMakr-4WWQ6m (1).png);")
        self.label_16.setText("")
        self.label_16.setObjectName("label_16")
        self.stackedWidget.addWidget(self.page_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.stackedWidget.setCurrentIndex(0)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page))
        self.pushButton_5.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_3))
        self.pushButton_7.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_4))
        self.pushButton_2.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_5))
        self.pushButton_3.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_6))
        self.pushButton_4.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_2))
        self.pushButton_36.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page))
        self.pushButton_37.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page))
        
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Symmetric Ciphers Encryption & Decryption"))
        self.label_13.setText(_translate("MainWindow", "Substitution Ciphers"))
        self.label_14.setText(_translate("MainWindow", "Mono-Alphabetic Ciphers"))
        self.label_25.setText(_translate("MainWindow", "Poly-Alphabetic Ciphers"))
        self.label_17.setText(_translate("MainWindow", "Transposition Ciphers"))
        self.label_3.setText(_translate("MainWindow", "Block Cipher Categories"))
        self.label_20.setText(_translate("MainWindow", "About"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"justify\"><span style=\" font-size:12pt;\">Symmetric encryption is a type of encryption where only one key (a secret key) is</span></p><p align=\"justify\"><span style=\" font-size:12pt;\">used to both encrypt and decrypt electronic information. This app is designed to</span></p><p align=\"justify\"><span style=\" font-size:12pt;\">encrypt and decrypt data using different symmetric cipher algorithms such as </span></p><p align=\"justify\"><span style=\" font-size:12pt;\">substitution, transposition, and block ciphers. The types of each category of the</span></p><p align=\"justify\"><span style=\" font-size:12pt;\">symmetric class are accessible in sub-menus. Substitution is an encryption algorithm</span></p><p align=\"justify\"><span style=\" font-size:12pt;\">in which letters of plaintext are replaced by letters of ciphertext. This cipher is further</span></p><p align=\"justify\"><span style=\" font-size:12pt;\">divided into two categories: mono-alphabetic and poly-alphabetic. This app helps you</span></p><p align=\"justify\"><span style=\" font-size:12pt;\">encrypt and decrypt using many mono-alphabetic and polyalphabetic ciphers.</span></p><p align=\"justify\"><span style=\" font-size:12pt;\">Furthermore, it uses transposition cipher in which letters of the plaintext are re-</span></p><p align=\"justify\"><span style=\" font-size:12pt;\">arranged to achieve the ciphertext. Also, it provides the opportunity to encrypt and</span></p><p align=\"justify\"><span style=\" font-size:12pt;\">decrypt using two famous and complex block ciphers: the DES (Data Encryption</span></p><p align=\"justify\"><span style=\" font-size:12pt;\">Standard and AES (Advanced Encryption Standard).</span></p><p align=\"justify\"><span style=\" font-size:12pt;\"><br/></span></p></body></html>"))
import Logo
import icons
import images


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
