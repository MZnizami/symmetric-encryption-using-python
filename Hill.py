
from  PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets
import Main

class Ui_Dialog(object):
    def goback(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.add = Main.Ui_MainWindow()
        self.add.setupUi(self.MainWindow)
        self.MainWindow.show()

    def encryptHill(self):
        alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        plaintext = self.plainText.toPlainText().replace(" ", "").upper()
        key1 = self.key11.toPlainText()
        key2 = self.key12.toPlainText()
        key3 = self.key13.toPlainText()
        key4 = self.key14.toPlainText()
        if(plaintext=="" or key1 == "" or key2 == "" or key3 == "" or key4 == ""):
            self.showCipheredText.setText("All fileds are required!")
        else:
            if len(plaintext) % 2 != 0:  # adding a z if not even length plain text
                plaintext += "X"
            plaintext = [plaintext[i:i + 2] for i in
                         range(0, len(plaintext), 2)]  # spliting the plaintext into a list of letter pairs


            matrixKey = [[key1, key2], [key3, key4]]  # forming the key matrix
            cipherText = ""
            for pairs in plaintext:  # finding location of pairs of letters of plaintext in alphabet
                indx1 = alpha.find(pairs[0])
                indx2 = alpha.find(pairs[1])
                matrixPlaintext = [[indx1], [indx2]]  # forming the plainText matrix of each pair
                cipherMatrix = [[0] for i in range(2)]  # creating an empty cipher text matrix
                for i in range(2):  # multiplying key matrix with each pair of plain letters
                    for j in range(1):
                        cipherMatrix[i][j] = 0
                        for x in range(2):
                            cipherMatrix[i][j] += (int(matrixKey[i][x]) *
                                                   matrixPlaintext[x][j])
                        cipherMatrix[i][j] = cipherMatrix[i][j] % 26
                cipherText += alpha[cipherMatrix[0][0]] + alpha[cipherMatrix[1][0]]  # finding the corresponding letters of
                self.showCipheredText.setText(cipherText)

    def gcd(self, a,b):  # To get the greatest common divisor...If gcd is not 1 means determinant and mod 26 are not coprime numbers, therefore no solution
        while b != 0:
            a, b = b, a % b
        return a

    def decryptHill(self):
        alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        cipherText = self.cipheredTextField.toPlainText().upper()
        key1 = self.keyb11.toPlainText()
        key2 = self.keyb12.toPlainText()
        key3 = self.keyb13.toPlainText()
        key4 = self.keyb14.toPlainText()
        if (cipherText == "" or key1 == "" or key2 == "" or key3 == "" or key4 == ""):
            self.decryptResult.setText("All fileds are required!")
        else:
            if len(cipherText) % 2 != 0:  # adding a z if not even length plain text
                cipherText += "Z"
            cipherText = [cipherText[i:i + 2] for i in
                          range(0, len(cipherText), 2)]  # spliting the cipherText into a list of letter pairs

            matrixKey = [[int(float(key1)), int(float(key2))], [int(float(key3)), int(float(key4))]]  # forming the key matrix

            # inversing the key matrix.........................
            determinant = matrixKey[0][0] * matrixKey[1][1] - matrixKey[0][1] * matrixKey[1][0]
            determinant = determinant % 26
            multiplicative_inverse = -1
            for multiplicative_inverse in range(
                    26):  # finding modular inverse of determinant, to multiply it with the key matrix
                if (determinant * multiplicative_inverse) % 26 == 1:
                    break
            if multiplicative_inverse == -1 or determinant == 0 or self.gcd(determinant,26) != 1:
                print("Decryption not possible")
            else:
                matrixKey[0][0], matrixKey[1][1] = matrixKey[1][1], matrixKey[0][
                    0]  # swaping value 1st and 4th element of key matrix
                matrixKey[0][1] *= -1  # changing the sign of 2nd and 3rd element of the key matrix
                matrixKey[1][0] *= -1

                for row in range(2):  # multiplying the modular inverse of determinant with the key matrix
                    for column in range(2):
                        matrixKey[row][column] *= multiplicative_inverse
                        matrixKey[row][column] = matrixKey[row][column] % 26
                plain = ""
                for pairs in cipherText:  # location of cipherText letter pairs
                    indx1 = alpha.find(pairs[0])
                    indx2 = alpha.find(pairs[1])

                    matrixCipher = [[indx1], [indx2]]  # forming the matrix cipher of cipherText pairs
                    plainMatrix = [[0] for i in range(2)]
                    for i in range(2):  # multiplying the inverse key matrix with cipher matrix
                        for j in range(1):
                            plainMatrix[i][j] = 0
                            for x in range(2):
                                plainMatrix[i][j] += (matrixKey[i][x] *
                                                      matrixCipher[x][j])
                            plainMatrix[i][j] = plainMatrix[i][j] % 26
                    plain += alpha[plainMatrix[0][0]] + alpha[plainMatrix[1][0]]
                self.decryptResult.setText(plain)
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(600, 900)
        Dialog.setMinimumSize(QtCore.QSize(600, 900))
        Dialog.setMaximumSize(QtCore.QSize(600, 900))
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
        self.label_2.setGeometry(QtCore.QRect(160, 10, 231, 31))
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
        self.encrypt = QtWidgets.QPushButton(Dialog)
        self.encrypt.setGeometry(QtCore.QRect(230, 360, 101, 31))
        self.encrypt.setStyleSheet("\n"
"image: url(:/newPrefix/encryptlogo.png);\n"
"background-color: rgb(34, 51, 99);\n"
"border-radius: 7px;\n"
"padding:3px;")
        self.encrypt.setText("")
        self.encrypt.setObjectName("encrypt")
        self.encrypt.clicked.connect(self.encryptHill)
        self.plainText = QtWidgets.QPlainTextEdit(Dialog)
        self.plainText.setGeometry(QtCore.QRect(150, 120, 251, 31))
        self.plainText.setObjectName("plainText")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(60, 410, 81, 41))
        self.label_6.setStyleSheet("font: 15pt \"Agency FB\";")
        self.label_6.setObjectName("label_6")
        self.showCipheredText = QtWidgets.QLabel(Dialog)
        self.showCipheredText.setGeometry(QtCore.QRect(160, 400, 251, 61))
        self.showCipheredText.setStyleSheet("font: 15pt \"Agency FB\";\n"
"\n"
"background-color: rgb(255, 255, 255);")
        self.showCipheredText.setText("")
        self.showCipheredText.setObjectName("showCipheredText")
        self.showCipheredText.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.cipheredTextField = QtWidgets.QPlainTextEdit(Dialog)
        self.cipheredTextField.setGeometry(QtCore.QRect(160, 510, 251, 31))
        self.cipheredTextField.setObjectName("cipheredTextField")
        self.keyb11 = QtWidgets.QPlainTextEdit(Dialog)
        self.keyb11.setGeometry(QtCore.QRect(160, 590, 251, 31))
        self.keyb11.setObjectName("keyb11")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(230, 460, 121, 41))
        self.label_8.setStyleSheet("font: 20pt \"Agency FB\";")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(60, 500, 81, 41))
        self.label_9.setStyleSheet("font: 15pt \"Agency FB\";")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(60, 590, 81, 41))
        self.label_10.setStyleSheet("font: 15pt \"Agency FB\";")
        self.label_10.setObjectName("label_10")
        self.decrypt = QtWidgets.QPushButton(Dialog)
        self.decrypt.setGeometry(QtCore.QRect(230, 760, 111, 31))
        self.decrypt.setStyleSheet("background-color: rgb(34, 51, 99);\n"
"border-image: url(:/newPrefix/decryptLogo.png);\n"
"border-radius: 7px;\n"
"padding:10px;")
        self.decrypt.setText("")
        self.decrypt.setObjectName("decrypt")
        self.decrypt.clicked.connect(self.decryptHill)
        self.decryptResult = QtWidgets.QLabel(Dialog)
        self.decryptResult.setGeometry(QtCore.QRect(160, 810, 251, 61))
        self.decryptResult.setStyleSheet("font: 15pt \"Agency FB\";\n"
"background-color: rgb(255, 255, 255);")
        self.decryptResult.setText("")
        self.decryptResult.setObjectName("decryptResult")
        self.decryptResult.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.label_12 = QtWidgets.QLabel(Dialog)
        self.label_12.setGeometry(QtCore.QRect(70, 820, 71, 41))
        self.label_12.setStyleSheet("font: 15pt \"Agency FB\";")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(Dialog)
        self.label_13.setGeometry(QtCore.QRect(440, 200, 121, 131))
        self.label_13.setStyleSheet("border-image: url(:/newPrefix/lock (2).png);")
        self.label_13.setText("")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(Dialog)
        self.label_14.setGeometry(QtCore.QRect(460, 600, 91, 141))
        self.label_14.setStyleSheet("border-image: url(:/newPrefix/key (2).png);")
        self.label_14.setText("")
        self.label_14.setObjectName("label_14")
        self.keyb12 = QtWidgets.QPlainTextEdit(Dialog)
        self.keyb12.setGeometry(QtCore.QRect(160, 630, 251, 31))
        self.keyb12.setObjectName("keyb12")
        self.keyb14 = QtWidgets.QPlainTextEdit(Dialog)
        self.keyb14.setGeometry(QtCore.QRect(160, 710, 251, 31))
        self.keyb14.setObjectName("keyb14")
        self.keyb13 = QtWidgets.QPlainTextEdit(Dialog)
        self.keyb13.setGeometry(QtCore.QRect(160, 670, 251, 31))
        self.keyb13.setObjectName("keyb13")
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(60, 630, 91, 41))
        self.label_11.setStyleSheet("font: 15pt \"Agency FB\";")
        self.label_11.setObjectName("label_11")
        self.label_15 = QtWidgets.QLabel(Dialog)
        self.label_15.setGeometry(QtCore.QRect(60, 710, 91, 41))
        self.label_15.setStyleSheet("font: 15pt \"Agency FB\";")
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(Dialog)
        self.label_16.setGeometry(QtCore.QRect(60, 670, 91, 41))
        self.label_16.setStyleSheet("font: 15pt \"Agency FB\";")
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(Dialog)
        self.label_17.setGeometry(QtCore.QRect(240, 540, 91, 41))
        self.label_17.setStyleSheet("font: 15pt \"Agency FB\";")
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(Dialog)
        self.label_18.setGeometry(QtCore.QRect(50, 200, 81, 41))
        self.label_18.setStyleSheet("font: 15pt \"Agency FB\";")
        self.label_18.setObjectName("label_18")
        self.key12 = QtWidgets.QPlainTextEdit(Dialog)
        self.key12.setGeometry(QtCore.QRect(150, 240, 251, 31))
        self.key12.setObjectName("key12")
        self.key14 = QtWidgets.QPlainTextEdit(Dialog)
        self.key14.setGeometry(QtCore.QRect(150, 320, 251, 31))
        self.key14.setObjectName("key14")
        self.label_19 = QtWidgets.QLabel(Dialog)
        self.label_19.setGeometry(QtCore.QRect(50, 240, 91, 41))
        self.label_19.setStyleSheet("font: 15pt \"Agency FB\";")
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(Dialog)
        self.label_20.setGeometry(QtCore.QRect(50, 320, 91, 41))
        self.label_20.setStyleSheet("font: 15pt \"Agency FB\";")
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(Dialog)
        self.label_21.setGeometry(QtCore.QRect(50, 280, 91, 41))
        self.label_21.setStyleSheet("font: 15pt \"Agency FB\";")
        self.label_21.setObjectName("label_21")
        self.key11 = QtWidgets.QPlainTextEdit(Dialog)
        self.key11.setGeometry(QtCore.QRect(150, 200, 251, 31))
        self.key11.setObjectName("key11")
        self.key13 = QtWidgets.QPlainTextEdit(Dialog)
        self.key13.setGeometry(QtCore.QRect(150, 280, 251, 31))
        self.key13.setObjectName("key13")
        self.label_22 = QtWidgets.QLabel(Dialog)
        self.label_22.setGeometry(QtCore.QRect(230, 160, 91, 31))
        self.label_22.setStyleSheet("font: 15pt \"Agency FB\";")
        self.label_22.setObjectName("label_22")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Encryption"))
        self.label_2.setText(_translate("Dialog", "Two Letter Hill Cipher"))
        self.label_4.setText(_translate("Dialog", "Plaintext"))
        self.label_6.setText(_translate("Dialog", "Ciphertext"))
        self.label_8.setText(_translate("Dialog", "Decryption"))
        self.label_9.setText(_translate("Dialog", "Ciphertext"))
        self.label_10.setText(_translate("Dialog", "Row1 Col1"))
        self.label_12.setText(_translate("Dialog", "PlainText"))
        self.label_11.setText(_translate("Dialog", "Row1 Col2"))
        self.label_15.setText(_translate("Dialog", "Row2 Col2"))
        self.label_16.setText(_translate("Dialog", "Row2 Col1"))
        self.label_17.setText(_translate("Dialog", "Key Matrix"))
        self.label_18.setText(_translate("Dialog", "Row1 Col1"))
        self.label_19.setText(_translate("Dialog", "Row1 Col2"))
        self.label_20.setText(_translate("Dialog", "Row2 Col2"))
        self.label_21.setText(_translate("Dialog", "Row2 Col1"))
        self.label_22.setText(_translate("Dialog", "Key Matrix"))
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
