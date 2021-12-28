from PyQt5 import QtCore, QtGui, QtWidgets
from  PyQt5.QtCore import Qt
from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES
import Main

class Ui_Dialog(object):
    def goback(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.add = Main.Ui_MainWindow()
        self.add.setupUi(self.MainWindow)
        self.MainWindow.show()

    def pad(self, text):
        while len(text) % 32 != 0:
            text += b' '
        return text

    def encryptAES(self):
        key = self.keyPlain.toPlainText().encode('utf-8')
        plaintext = self.plainText.toPlainText()
        if (plaintext== ""):
            self.showCipheredText.setText("All fields are required!")
        elif (len(key) != 16):
            self.showCipheredText.setText("Key length must be 16 bytes!")
            self.keyPlain.setPlainText("")
        else:
            plaintext = plaintext.encode('utf-8')
            padded_plaintext = self.pad(plaintext)
            cipher = AES.new(key, AES.MODE_ECB)
            msg = cipher.encrypt(padded_plaintext)
            print(msg.hex())
            self.showCipheredText.setText(msg.hex())

    def decryptAES(self):
        key = self.cipheredKey.toPlainText().encode('utf-8')
        ciphertext = self.cipheredTextField.toPlainText()
        if(ciphertext==""):
            self.decryptResult.setText("All fields are required!")
        elif (len(key) != 16):
            self.decryptResult.setText("Key length must be 16 bytes!")
            self.cipheredKey.setPlainText("")
        else:
            ciphertext = bytes.fromhex(ciphertext)
            cipher = AES.new(key,AES.MODE_ECB)
            msg = cipher.decrypt(ciphertext)
            msg = msg.decode('ASCII')
            self.decryptResult.setText(str(msg))

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1000, 800)
        Dialog.setMinimumSize(QtCore.QSize(1000, 800))
        Dialog.setMaximumSize(QtCore.QSize(1000, 800))
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(450, 60, 111, 41))
        self.label.setStyleSheet("font: 20pt \"Agency FB\";")
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1001, 51))
        self.frame.setStyleSheet("\n"
"background-color: rgb(34, 51, 99);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(450, 0, 211, 51))
        self.label_2.setStyleSheet("font: 20pt \"Agency FB\";\n"
"color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.goBack = QtWidgets.QPushButton(self.frame)
        self.goBack.setGeometry(QtCore.QRect(920, 10, 71, 31))
        self.goBack.setStyleSheet("image: url(:/newPrefix/turnBack.png);\n"
"\n"
"border-radius: 3px;\n"
"")
        self.goBack.setText("")
        self.goBack.setObjectName("goBack")
        self.goBack.clicked.connect(self.goback)
        self.goBack.clicked.connect(self.goback)
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(20, 0, 111, 51))
        self.label_3.setStyleSheet("border-image: url(:/Logo/LogoMakr-2b8XDd.png);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(50, 120, 71, 41))
        self.label_4.setStyleSheet("font: 15pt \"Agency FB\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(80, 200, 31, 41))
        self.label_5.setStyleSheet("font: 15pt \"Agency FB\";")
        self.label_5.setObjectName("label_5")
        self.encrypt = QtWidgets.QPushButton(Dialog)
        self.encrypt.setGeometry(QtCore.QRect(440, 260, 131, 31))
        self.encrypt.setStyleSheet("\n"
"image: url(:/newPrefix/encryptlogo.png);\n"
"background-color: rgb(34, 51, 99);\n"
"border-radius: 7px;\n"
"padding:3px;")
        self.encrypt.setText("")
        self.encrypt.setObjectName("encrypt")
        self.encrypt.clicked.connect(self.encryptAES)
        self.plainText = QtWidgets.QPlainTextEdit(Dialog)
        self.plainText.setGeometry(QtCore.QRect(140, 120, 711, 61))
        self.plainText.setObjectName("plainText")
        self.keyPlain = QtWidgets.QPlainTextEdit(Dialog)
        self.keyPlain.setGeometry(QtCore.QRect(140, 190, 711, 61))
        self.keyPlain.setObjectName("keyPlain")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(40, 330, 81, 41))
        self.label_6.setStyleSheet("font: 15pt \"Agency FB\";")
        self.label_6.setObjectName("label_6")
        self.showCipheredText = QtWidgets.QLabel(Dialog)
        self.showCipheredText.setGeometry(QtCore.QRect(140, 310, 721, 91))
        self.showCipheredText.setStyleSheet("font: 15pt \"Agency FB\";\n"
"\n"
"background-color: rgb(255, 255, 255);")
        self.showCipheredText.setText("")
        self.showCipheredText.setObjectName("showCipheredText")
        self.showCipheredText.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.cipheredTextField = QtWidgets.QPlainTextEdit(Dialog)
        self.cipheredTextField.setGeometry(QtCore.QRect(140, 480, 721, 61))
        self.cipheredTextField.setObjectName("cipheredTextField")
        self.cipheredKey = QtWidgets.QPlainTextEdit(Dialog)
        self.cipheredKey.setGeometry(QtCore.QRect(140, 550, 721, 61))
        self.cipheredKey.setObjectName("cipheredKey")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(450, 410, 121, 41))
        self.label_8.setStyleSheet("font: 20pt \"Agency FB\";")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(40, 490, 81, 41))
        self.label_9.setStyleSheet("font: 15pt \"Agency FB\";")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(70, 550, 61, 41))
        self.label_10.setStyleSheet("font: 15pt \"Agency FB\";")
        self.label_10.setObjectName("label_10")
        self.decrypt = QtWidgets.QPushButton(Dialog)
        self.decrypt.setGeometry(QtCore.QRect(450, 630, 131, 31))
        self.decrypt.setStyleSheet("background-color: rgb(34, 51, 99);\n"
"border-image: url(:/newPrefix/decryptLogo.png);\n"
"border-radius: 7px;\n"
"padding:10px;")
        self.decrypt.setText("")
        self.decrypt.setObjectName("decrypt")
        self.decrypt.clicked.connect(self.decryptAES)
        self.decryptResult = QtWidgets.QLabel(Dialog)
        self.decryptResult.setGeometry(QtCore.QRect(140, 680, 721, 91))
        self.decryptResult.setStyleSheet("font: 15pt \"Agency FB\";\n"
"background-color: rgb(255, 255, 255);")
        self.decryptResult.setText("")
        self.decryptResult.setObjectName("decryptResult")
        self.decryptResult.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.label_12 = QtWidgets.QLabel(Dialog)
        self.label_12.setGeometry(QtCore.QRect(50, 710, 71, 41))
        self.label_12.setStyleSheet("font: 15pt \"Agency FB\";")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(Dialog)
        self.label_13.setGeometry(QtCore.QRect(860, 120, 111, 121))
        self.label_13.setStyleSheet("border-image: url(:/newPrefix/lock (2).png);")
        self.label_13.setText("")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(Dialog)
        self.label_14.setGeometry(QtCore.QRect(870, 480, 81, 131))
        self.label_14.setStyleSheet("border-image: url(:/newPrefix/key (2).png);")
        self.label_14.setText("")
        self.label_14.setObjectName("label_14")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Encryption"))
        self.label_2.setText(_translate("Dialog", "AES Cipher"))
        self.label_4.setText(_translate("Dialog", "Plaintext"))
        self.label_5.setText(_translate("Dialog", "Key"))
        self.label_6.setText(_translate("Dialog", "Ciphertext"))
        self.label_8.setText(_translate("Dialog", "Decryption"))
        self.label_9.setText(_translate("Dialog", "Ciphertext"))
        self.label_10.setText(_translate("Dialog", "Key"))
        self.label_12.setText(_translate("Dialog", "Plaintext"))
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
