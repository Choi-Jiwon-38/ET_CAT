# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ET_CAT_designer.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


# ================ QtDesigner로 GUI를 작성하였습니다 ============================
from PyQt5 import QtCore, QtGui, QtWidgets
from catFunction import checkingDictionary, end_talk, game_start_setting, loadWordList, updateWordList
from PyQt5.QtGui import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("ET CAT_끝말잇기 하는 고양이")
        MainWindow.resize(371, 555)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.labelEnglish = QtWidgets.QLabel(self.centralwidget)
        self.labelEnglish.setGeometry(QtCore.QRect(20, 10, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Bodoni MT Black")
        font.setPointSize(30)
        
        self.labelEnglish.setFont(font)
        self.labelEnglish.setObjectName("labelEnglish")
        
        self.labelKorean = QtWidgets.QLabel(self.centralwidget)
        self.labelKorean.setGeometry(QtCore.QRect(170, 60, 191, 21))
        font = QtGui.QFont()
        font.setFamily("휴먼매직체")
        font.setPointSize(12)
        
        self.labelKorean.setFont(font)
        self.labelKorean.setObjectName("labelKorean")
        
        self.screenEndTalk = QtWidgets.QTextBrowser(self.centralwidget)
        self.screenEndTalk.setGeometry(QtCore.QRect(20, 310, 331, 121))
        self.screenEndTalk.setObjectName("screenEndTalk")
        
        self.screenCat = QtWidgets.QLabel(self.centralwidget)
        self.screenCat.setGeometry(QtCore.QRect(20, 100, 331, 192))
        self.screenCat.setObjectName("screenCat")
        
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(20, 450, 281, 41))
        self.plainTextEdit.setObjectName("plainTextEdit")
        
        self.buttonInput = QtWidgets.QPushButton(self.centralwidget)
        self.buttonInput.setGeometry(QtCore.QRect(310, 450, 41, 41))
        font = QtGui.QFont()
        font.setFamily("BM JUA_TTF")
        font.setPointSize(15)
        self.buttonInput.setFont(font)
        self.buttonInput.setObjectName("buttonInput")
        # 함수 연결 __ buttonInput
        self.buttonInput.clicked.connect(self.entering_player_word)


        self.buttonUpgrade = QtWidgets.QPushButton(self.centralwidget)
        self.buttonUpgrade.setGeometry(QtCore.QRect(260, 20, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(11)
        self.buttonUpgrade.setFont(font)
        self.buttonUpgrade.setObjectName("buttonUpgrade")
        # 함수 연결 __ buttonUpgrade
        self.buttonUpgrade.clicked.connect(self.update_wordList)


        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 371, 21))
        self.menubar.setObjectName("menubar")
        
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.displaying_cat_image("reset")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "끝말잇기 하는 고양이"))
        self.labelEnglish.setText(_translate("MainWindow", "ET CAT"))
        self.labelKorean.setText(_translate("MainWindow", "고양이와 함께 하는 끝말잇기"))
        self.screenEndTalk.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.buttonInput.setText(_translate("MainWindow", "♥"))
        self.buttonUpgrade.setText(_translate("MainWindow", "UPDATE"))
# =============================================================================
    
    def entering_player_word(self):
        print('InputButton Clicked!') # debug1
        self.displaying_cat_image("reset")
        word = self.plainTextEdit.toPlainText()
        prev_word = self.screenEndTalk.toPlainText()
        self.screenEndTalk.append("플레이어: " + word)
        if word == "시작!":
            self.first_start_game()
        else:
            screenWord = end_talk(word, prev_word)
            if screenWord == "으.. 모르겠다... 나의 패배야...!":
                self.displaying_cat_image("win")
            elif screenWord == "없는 단어를 입력했네? 아쉽겠지만 나의 승리야!" or screenWord == "너 끝말을 잇는다는 거가 뭔지 몰라? 나의 승리야!":
                self.displaying_cat_image("defeated")

            self.screenEndTalk.append("고양이: " + screenWord)


    def update_wordList(self):
        print('UpdateButton Clicked') # debug2
        updateWordList()
        

    def displaying_cat_image(self, status):
        if status == "reset":
            reference = 'mainScreen.jpg'
        elif status == "win":
            reference = 'mainScreen_win.jpg'
        else:
            reference = 'mainScreen_defeated.jpg'
        self.pm = QPixmap(reference)
        self.pm.scaled(30,30)
        self.screenCat.setPixmap(self.pm)

    def first_start_game(self):
        self.screenEndTalk.append("고양이: 그러면 나 먼저 시작할게!")
        word = game_start_setting()
        self.screenEndTalk.append("고양이: 음.... " + word)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
