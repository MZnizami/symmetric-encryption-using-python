from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets
import Main

class Ui_Dialog(object):
    def decryptNull(self):

        plaintext = self.cipheredTextField.toPlainText().lower()
        if(plaintext==""):
            self.decryptResult.setText("Field is required!")
            self.cipheredTextField.setPlainText("")
        else:
            result = ''.join([lett[0] for lett in plaintext.split()])
            self.decryptResult.setText(result)

    def goback(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.add = Main.Ui_MainWindow()
        self.add.setupUi(self.MainWindow)
        self.MainWindow.show()
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(550, 400)
        Dialog.setMinimumSize(QtCore.QSize(550, 400))
        Dialog.setMaximumSize(QtCore.QSize(550, 400))
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(0, 0, 601, 51))
        self.frame.setStyleSheet("\n"
"background-color: rgb(34, 51, 99);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(220, 10, 111, 31))
        self.label_2.setStyleSheet("font: 20pt \"Agency FB\";\n"
"color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 111, 41))
        self.label_3.setStyleSheet("image: url(:/Logo/LogoMakr-2b8XDd.png);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.goBack = QtWidgets.QPushButton(self.frame)
        self.goBack.setGeometry(QtCore.QRect(500, 10, 41, 31))
        self.goBack.setStyleSheet("image: url(:/newPrefix/turnBack.png);\n"
"\n"
"border-radius: 3px;\n"
"")
        self.goBack.setText("")
        self.goBack.setObjectName("goBack")
        self.goBack.clicked.connect(self.goback)
        self.cipheredTextField = QtWidgets.QPlainTextEdit(Dialog)
        self.cipheredTextField.setGeometry(QtCore.QRect(140, 140, 251, 51))
        self.cipheredTextField.setObjectName("cipheredTextField")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(210, 90, 121, 41))
        self.label_8.setStyleSheet("font: 20pt \"Agency FB\";")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(40, 150, 81, 41))
        self.label_9.setStyleSheet("font: 15pt \"Agency FB\";")
        self.label_9.setObjectName("label_9")
        self.decrypt = QtWidgets.QPushButton(Dialog)
        self.decrypt.setGeometry(QtCore.QRect(210, 220, 111, 31))
        self.decrypt.setStyleSheet("background-color: rgb(34, 51, 99);\n"
"border-image: url(:/newPrefix/decryptLogo.png);\n"
"border-radius: 7px;\n"
"padding:10px;")
        self.decrypt.setText("")
        self.decrypt.setObjectName("decrypt")
        self.decrypt.clicked.connect(self.decryptNull)
        self.decryptResult = QtWidgets.QLabel(Dialog)
        self.decryptResult.setGeometry(QtCore.QRect(140, 270, 251, 61))
        self.decryptResult.setStyleSheet("font: 15pt \"Agency FB\";\n"
"background-color: rgb(255, 255, 255);")
        self.decryptResult.setText("")
        self.decryptResult.setObjectName("decryptResult")
        self.decryptResult.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.label_12 = QtWidgets.QLabel(Dialog)
        self.label_12.setGeometry(QtCore.QRect(50, 280, 71, 41))
        self.label_12.setStyleSheet("font: 15pt \"Agency FB\";")
        self.label_12.setObjectName("label_12")
        self.label_14 = QtWidgets.QLabel(Dialog)
        self.label_14.setGeometry(QtCore.QRect(440, 130, 81, 131))
        self.label_14.setStyleSheet("border-image: url(:/newPrefix/key (2).png);")
        self.label_14.setText("")
        self.label_14.setObjectName("label_14")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "Null Cipher"))
        self.label_8.setText(_translate("Dialog", "Decryption"))
        self.label_9.setText(_translate("Dialog", "Ciphertext"))
        self.label_12.setText(_translate("Dialog", "PlainText"))
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
