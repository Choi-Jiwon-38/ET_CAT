import sys
from PyQt5.QtWidgets import QApplication, QHBoxLayout, QVBoxLayout, QWidget, QLabel, QPushButton, QToolTip
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtCore import QCoreApplication
import random

class ET_CAT(QWidget):
    def __init__(self):
        super().__init__()
        self.ResetUI()

    def ResetUI(self):
        # hbox1 에 들어갈 내용들
        self.titleLabel = QLabel('끝말잇기 고양이', self)
        self.titleLabel.setFont(QFont('Helvetica', pointSize = 20, weight = 2))

        # hbox2 에 들어갈 내용들
        surrenderButton = QPushButton("항복")
        rankingButton = QPushButton("랭킹")
        renewalButton = QPushButton("단어 갱신")


        # hbox 레이아웃 설정
        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.titleLabel)

        hbox2 = QHBoxLayout()
        hbox2.addWidget(surrenderButton)
        hbox2.addWidget(rankingButton)
        hbox2.addWidget(renewalButton)

        vbox1 = QVBoxLayout()
        vbox2 = QVBoxLayout()
        vbox1.addLayout(hbox1)
        vbox2.addLayout(hbox2)

        self.setLayout(vbox1)
        self.setLayout(vbox2)


        self.setWindowTitle('ET_CAT')
        self.setWindowIcon(QIcon('icon.png'))
        self.setGeometry(600, 600,400, 400)
    
    def QuitProgram(self):
        return QCoreApplication.instance().quit()
    
if __name__ == '__main__':
    
    import sys

    app = QApplication(sys.argv)
    EC = ET_CAT()
    EC.show()
    sys.exit(app.exec_())
