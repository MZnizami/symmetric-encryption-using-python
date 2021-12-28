from  PyQt5.QtCore import Qt

from PyQt5 import QtCore, QtGui, QtWidgets
import Main

class Ui_Dialog(object):
    def goback(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.add = Main.Ui_MainWindow()
        self.add.setupUi(self.MainWindow)
        self.MainWindow.show()

    def encryptROT(self):
        numbers = "1234567890"
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        plaintext = self.plainText.toPlainText().lower()
        plaintext = ''.join(plaintext.split())
        key =  13
        ciphertext = ""
        if(plaintext==""):
            self.showCipheredText.setText("All fields are required!")
            self.plainText.setPlainText("")
        elif(plaintext in numbers):
            self.showCipheredText.setText("You can't enter numeric data!")
            self.plainText.setPlainText("")
        else:
            for i in range(len(plaintext)):
                letter = plaintext[i]
                location = alphabet.find(letter)
                location = (location + key) % 26
                ciphertext = ciphertext + alphabet[location]
            self.showCipheredText.setText(ciphertext)

    def decryptROT(self):
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        numbers = "1234567890"
        ciphertext = self.cipheredTextField.toPlainText().lower()
        ciphertext = ''.join(ciphertext.split())
        key = 13
        plaintext = ''
        if(ciphertext==""):
            self.decryptResult.setText("All fields are required!")
            self.cipheredTextField.setPlainText("")
        elif(ciphertext in numbers):
            self.decryptResult.setText("You can't enter numeric data!")
            self.cipheredTextField.setPlainText("")
        else:
            for i in range(len(ciphertext)):
                letter = ciphertext[i]
                location = alphabet.find(letter)
                location = (location - key) % 26
                plaintext = plaintext + alphabet[location]
            self.decryptResult.setText(plaintext)
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(600, 620)
        Dialog.setMinimumSize(QtCore.QSize(600, 620))
        Dialog.setMaximumSize(QtCore.QSize(600, 620))
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
        self.label_2.setGeometry(QtCore.QRect(200, 10, 171, 31))
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
        self.label_4.setGeometry(QtCore.QRect(60, 120, 71, 41))
        self.label_4.setStyleSheet("font: 15pt \"Agency FB\";")
        self.label_4.setObjectName("label_4")
        self.encrypt = QtWidgets.QPushButton(Dialog)
        self.encrypt.setGeometry(QtCore.QRect(230, 200, 101, 31))
        self.encrypt.setStyleSheet("\n"
"image: url(:/newPrefix/encryptlogo.png);\n"
"background-color: rgb(34, 51, 99);\n"
"border-radius: 7px;\n"
"padding:3px;")
        self.encrypt.setText("")
        self.encrypt.setObjectName("encrypt")
        self.encrypt.clicked.connect(self.encryptROT)
        self.plainText = QtWidgets.QPlainTextEdit(Dialog)
        self.plainText.setGeometry(QtCore.QRect(150, 120, 251, 51))
        self.plainText.setObjectName("plainText")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(50, 260, 81, 41))
        self.label_6.setStyleSheet("font: 15pt \"Agency FB\";")
        self.label_6.setObjectName("label_6")
        self.showCipheredText = QtWidgets.QLabel(Dialog)
        self.showCipheredText.setGeometry(QtCore.QRect(150, 250, 251, 61))
        self.showCipheredText.setStyleSheet("font: 15pt \"Agency FB\";\n"
"\n"
"background-color: rgb(255, 255, 255);")
        self.showCipheredText.setText("")
        self.showCipheredText.setObjectName("showCipheredText")
        self.showCipheredText.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.cipheredTextField = QtWidgets.QPlainTextEdit(Dialog)
        self.cipheredTextField.setGeometry(QtCore.QRect(160, 390, 251, 51))
        self.cipheredTextField.setObjectName("cipheredTextField")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(230, 340, 121, 41))
        self.label_8.setStyleSheet("font: 20pt \"Agency FB\";")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(60, 400, 81, 41))
        self.label_9.setStyleSheet("font: 15pt \"Agency FB\";")
        self.label_9.setObjectName("label_9")
        self.decrypt = QtWidgets.QPushButton(Dialog)
        self.decrypt.setGeometry(QtCore.QRect(230, 470, 111, 31))
        self.decrypt.setStyleSheet("background-color: rgb(34, 51, 99);\n"
"border-image: url(:/newPrefix/decryptLogo.png);\n"
"border-radius: 7px;\n"
"padding:10px;")
        self.decrypt.setText("")
        self.decrypt.setObjectName("decrypt")
        self.decrypt.clicked.connect(self.decryptROT)
        self.decryptResult = QtWidgets.QLabel(Dialog)
        self.decryptResult.setGeometry(QtCore.QRect(160, 520, 251, 61))
        self.decryptResult.setStyleSheet("font: 15pt \"Agency FB\";\n"
"background-color: rgb(255, 255, 255);")
        self.decryptResult.setText("")
        self.decryptResult.setObjectName("decryptResult")
        self.decryptResult.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.label_12 = QtWidgets.QLabel(Dialog)
        self.label_12.setGeometry(QtCore.QRect(70, 530, 71, 41))
        self.label_12.setStyleSheet("font: 15pt \"Agency FB\";")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(Dialog)
        self.label_13.setGeometry(QtCore.QRect(440, 120, 111, 121))
        self.label_13.setStyleSheet("border-image: url(:/newPrefix/lock (2).png);")
        self.label_13.setText("")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(Dialog)
        self.label_14.setGeometry(QtCore.QRect(460, 380, 81, 131))
        self.label_14.setStyleSheet("border-image: url(:/newPrefix/key (2).png);")
        self.label_14.setText("")
        self.label_14.setObjectName("label_14")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Encryption"))
        self.label_2.setText(_translate("Dialog", "ROT 13 Cipher"))
        self.label_4.setText(_translate("Dialog", "Plaintext"))
        self.label_6.setText(_translate("Dialog", "Ciphertext"))
        self.label_8.setText(_translate("Dialog", "Decryption"))
        self.label_9.setText(_translate("Dialog", "Ciphertext"))
        self.label_12.setText(_translate("Dialog", "PlainText"))
import decr
import encrypt
import keyLogo
import lockLogo
import returnBack


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
