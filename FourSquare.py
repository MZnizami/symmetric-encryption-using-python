from PyQt5.QtCore import  Qt
from PyQt5 import QtCore, QtGui, QtWidgets
from idna import unicode
from secretpy import FourSquare
from secretpy import CryptMachine
from secretpy import alphabets
from secretpy.cmdecorators import NoSpaces, UpperCase

import Main

class Ui_Dialog(object):
    def goback(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.add = Main.Ui_MainWindow()
        self.add.setupUi(self.MainWindow)
        self.MainWindow.show()

    def encryptFourSquare(self):
        alphabet = alphabets.ENGLISH_SQUARE_OQ
        key1 = self.keyPlain.toPlainText()
        key2 = self.keyPlain_2.toPlainText()
        p = self.plainText.toPlainText()
        if(p=='' or key1=='' or key2==''):
            self.showCipheredText.setText("All fields are required!")
        else:
            key = (unicode(key1), unicode(key2))
            cm = NoSpaces(UpperCase(CryptMachine(FourSquare())))
            cm.set_alphabet(alphabet)
            cm.set_key(key)
            plaintext = unicode(p)
            enc = cm.encrypt(plaintext)
            self.showCipheredText.setText(enc)
    def decryptFourSquare(self):
        alphabet = alphabets.ENGLISH_SQUARE_OQ
        key1 = self.cipheredKey.toPlainText()
        key2 = self.cipheredKey_2.toPlainText()
        c = self.cipheredTextField.toPlainText()
        if(c == '' or key1 == '' or key2 == ''):
            self.decryptResult.setText("All fields are required!")
        else:
            key = (unicode(key1), unicode(key2))
            cm = NoSpaces(UpperCase(CryptMachine(FourSquare())))
            cm.set_alphabet(alphabet)
            cm.set_key(key)
            ciphertext = unicode(c)
            dec = cm.decrypt(ciphertext)
            self.decryptResult.setText(dec)
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(600, 750)
        Dialog.setMinimumSize(QtCore.QSize(600, 750))
        Dialog.setMaximumSize(QtCore.QSize(600, 750))
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(210, 60, 111, 41))
        self.label.setStyleSheet("font: 20pt \"Agency FB\";")
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(0, 0, 601, 51))
        self.frame.setStyleSheet("\n"
"background-color: rgb(34, 51, 99);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(170, 0, 231, 41))
        self.label_2.setStyleSheet("font: 20pt \"Agency FB\";\n"
"color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 111, 41))
        self.label_3.setStyleSheet("image: url(:/Logo/LogoMakr-2b8XDd.png);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.goBack = QtWidgets.QPushButton(self.frame)
        self.goBack.setGeometry(QtCore.QRect(520, 10, 71, 31))
        self.goBack.setStyleSheet("image: url(:/newPrefix/turnBack.png);\n"
"\n"
"border-radius: 3px;\n"
"")
        self.goBack.setText("")
        self.goBack.setObjectName("goBack")
        self.goBack.clicked.connect(self.goback)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(60, 110, 71, 41))
        self.label_4.setStyleSheet("font: 15pt \"Agency FB\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(90, 160, 31, 41))
        self.label_5.setStyleSheet("font: 15pt \"Agency FB\";")
        self.label_5.setObjectName("label_5")
        self.encrypt = QtWidgets.QPushButton(Dialog)
        self.encrypt.setGeometry(QtCore.QRect(230, 270, 101, 31))
        self.encrypt.setStyleSheet("\n"
"image: url(:/newPrefix/encryptlogo.png);\n"
"background-color: rgb(34, 51, 99);\n"
"border-radius: 7px;\n"
"padding:3px;")
        self.encrypt.setText("")
        self.encrypt.setObjectName("encrypt")
        ########################################
        self.encrypt.clicked.connect(self.encryptFourSquare)
        self.plainText = QtWidgets.QPlainTextEdit(Dialog)
        self.plainText.setGeometry(QtCore.QRect(150, 120, 251, 31))
        self.plainText.setObjectName("plainText")
        self.keyPlain = QtWidgets.QPlainTextEdit(Dialog)
        self.keyPlain.setGeometry(QtCore.QRect(150, 170, 251, 31))
        self.keyPlain.setObjectName("keyPlain")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(50, 330, 81, 41))
        self.label_6.setStyleSheet("font: 15pt \"Agency FB\";")
        self.label_6.setObjectName("label_6")
        self.showCipheredText = QtWidgets.QLabel(Dialog)
        self.showCipheredText.setGeometry(QtCore.QRect(150, 320, 251, 61))
        self.showCipheredText.setStyleSheet("font: 15pt \"Agency FB\";\n"
"\n"
"background-color: rgb(255, 255, 255);")
        self.showCipheredText.setText("")
        self.showCipheredText.setObjectName("showCipheredText")
        self.showCipheredText.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.cipheredTextField = QtWidgets.QPlainTextEdit(Dialog)
        self.cipheredTextField.setGeometry(QtCore.QRect(160, 450, 251, 31))
        self.cipheredTextField.setObjectName("cipheredTextField")
        self.cipheredKey = QtWidgets.QPlainTextEdit(Dialog)
        self.cipheredKey.setGeometry(QtCore.QRect(160, 500, 251, 31))
        self.cipheredKey.setObjectName("cipheredKey")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(230, 400, 121, 41))
        self.label_8.setStyleSheet("font: 20pt \"Agency FB\";")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(60, 440, 81, 41))
        self.label_9.setStyleSheet("font: 15pt \"Agency FB\";")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(90, 500, 61, 41))
        self.label_10.setStyleSheet("font: 15pt \"Agency FB\";")
        self.label_10.setObjectName("label_10")
        self.decrypt = QtWidgets.QPushButton(Dialog)
        self.decrypt.setGeometry(QtCore.QRect(230, 610, 111, 31))
        self.decrypt.setStyleSheet("background-color: rgb(34, 51, 99);\n"
"border-image: url(:/newPrefix/decryptLogo.png);\n"
"border-radius: 7px;\n"
"padding:10px;")
        self.decrypt.setText("")
        self.decrypt.setObjectName("decrypt")
        #############################################
        self.decrypt.clicked.connect(self.decryptFourSquare)
        self.decryptResult = QtWidgets.QLabel(Dialog)
        self.decryptResult.setGeometry(QtCore.QRect(160, 660, 251, 61))
        self.decryptResult.setStyleSheet("font: 15pt \"Agency FB\";\n"
"background-color: rgb(255, 255, 255);")
        self.decryptResult.setText("")
        self.decryptResult.setObjectName("decryptResult")
        self.decryptResult.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.label_12 = QtWidgets.QLabel(Dialog)
        self.label_12.setGeometry(QtCore.QRect(70, 670, 71, 41))
        self.label_12.setStyleSheet("font: 15pt \"Agency FB\";")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(Dialog)
        self.label_13.setGeometry(QtCore.QRect(440, 120, 111, 121))
        self.label_13.setStyleSheet("border-image: url(:/newPrefix/lock (2).png);")
        self.label_13.setText("")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(Dialog)
        self.label_14.setGeometry(QtCore.QRect(460, 440, 81, 131))
        self.label_14.setStyleSheet("border-image: url(:/newPrefix/key (2).png);")
        self.label_14.setText("")
        self.label_14.setObjectName("label_14")
        self.cipheredKey_2 = QtWidgets.QPlainTextEdit(Dialog)
        self.cipheredKey_2.setGeometry(QtCore.QRect(160, 550, 251, 31))
        self.cipheredKey_2.setObjectName("cipheredKey_2")
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(90, 550, 61, 41))
        self.label_11.setStyleSheet("font: 15pt \"Agency FB\";")
        self.label_11.setObjectName("label_11")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(90, 210, 41, 41))
        self.label_7.setStyleSheet("font: 15pt \"Agency FB\";")
        self.label_7.setObjectName("label_7")
        self.keyPlain_2 = QtWidgets.QPlainTextEdit(Dialog)
        self.keyPlain_2.setGeometry(QtCore.QRect(150, 220, 251, 31))
        self.keyPlain_2.setObjectName("keyPlain_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Encryption"))
        self.label_2.setText(_translate("Dialog", "Four-Square Cipher"))
        self.label_4.setText(_translate("Dialog", "Plaintext"))
        self.label_5.setText(_translate("Dialog", "Key"))
        self.label_6.setText(_translate("Dialog", "Ciphertext"))
        self.label_8.setText(_translate("Dialog", "Decryption"))
        self.label_9.setText(_translate("Dialog", "Ciphertext"))
        self.label_10.setText(_translate("Dialog", "Key"))
        self.label_12.setText(_translate("Dialog", "PlainText"))
        self.label_11.setText(_translate("Dialog", "Key2"))
        self.label_7.setText(_translate("Dialog", "Key2"))
import decr
import encrypt
import keyLogo
import lockLogo
import Logo
import returnBack


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
