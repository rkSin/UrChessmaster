from PyQt5.QtWidgets import QWidget, QAction, qApp, QApplication, QLabel,QInputDialog,QCheckBox,QDialog, QComboBox,QGridLayout, QLineEdit
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.Qt import QTextEdit, QVBoxLayout, QPushButton, QHBoxLayout, pyqtSlot
from PyQt5.QtCore import Qt

import sys

class InitScreen(QDialog):
    def __init__(self,playerTocorrect):
        
        super().__init__()
         
        self.Result = 0
        self.playersNum = 1
        self.aiDifficult =[1,1,1]
        self.plDifficult =[1,1,1]
        self.isPlayer=[True,True,True]
        self.error = [False,False,False]
        if playerTocorrect ==0:
            self.initUI()
        elif playerTocorrect==1:
            self.initUI1()
        elif playerTocorrect==2:
            self.initUI2()
        elif playerTocorrect==3:
            self.initUI3()
        
        
    def initUI(self):      
        
        grid = QGridLayout(self)
        self.setLayout(grid)
        
        text1 = QLabel('Players Number')
        text2 = QLabel('Hostile Ai difficulty')
        text3 = QLabel('Player Ai')
        
        self.errorLabel1 =  QLabel(self)
        self.errorLabel2 =  QLabel(self)
        self.errorLabel3 =  QLabel(self)
        
        self.status =QLabel(self)
        
        self.errorLabel1.setText("Error status\n"+str(self.error[0]))
        self.errorLabel2.setText("Error status\n"+str(self.error[1]))
        self.errorLabel3.setText("Error status\n"+str(self.error[2]))
        
        self.setPlayersNum = QComboBox(self)
        self.setPlayersNum.addItem("1")
        self.setPlayersNum.addItem("2")
        self.setPlayersNum.addItem("3")
        self.setPlayersNum.activated[str].connect(self.Activation)
        
        self._togglep1 =True
        self.playerOne = QCheckBox('Player 1 is human', self)
        self.playerOne.toggle()
        self.playerOne.clicked.connect(self.togglep1)
        self.playerOneAi = QCheckBox('Player 1 is AI', self)
        self.playerOneAi.clicked.connect(self.togglep1)
        
        self._togglep2 =True
        self.playerTwo = QCheckBox('Player 2 is human', self)
        self.playerTwo.toggle()
        self.playerTwo.clicked.connect(self.togglep2)
        self.playerTwoAi = QCheckBox('Player 2 is AI', self)
        self.playerTwoAi.clicked.connect(self.togglep2)
        self.playerTwo.setDisabled(True)
        self.playerTwoAi.setDisabled(True)
        
        self._togglep3 =True
        self.playerThree = QCheckBox('Player 3 is human', self)
        self.playerThree.toggle()
        self.playerThree.clicked.connect(self.togglep3)
        self.playerThreeAi = QCheckBox('Player 3 is AI', self)
        self.playerThreeAi.clicked.connect(self.togglep3)
        self.playerThreeAi.setDisabled(True)
        self.playerThree.setDisabled(True)
        cancelButton = QPushButton('Done',self)
        
        self.difAi1 = QLineEdit(self)
        self.difAi1.setText("1")
        self.difAi1.textChanged[str].connect(self.TextChengedAi1)
        self.difPl1 = QLineEdit(self)
        self.difPl1.setText("1")
        self.difPl1.textChanged[str].connect(self.TextChengedPl1)
        self.difAi2 = QLineEdit(self)
        self.difAi2.setText("1")
        self.difAi2.setReadOnly(True)
        self.difAi2.textChanged[str].connect(self.TextChengedAi2)
        self.difPl2 = QLineEdit(self)
        self.difPl2.setText("1")
        self.difPl2.setReadOnly(True)
        self.difPl2.textChanged[str].connect(self.TextChengedPl2)
        self.difAi3 = QLineEdit(self)
        self.difAi3.setText("1")
        self.difAi3.setReadOnly(True)
        self.difAi3.textChanged[str].connect(self.TextChengedAi3)
        self.difPl3 = QLineEdit(self)
        self.difPl3.setText("1")
        self.difPl3.setReadOnly(True)
        self.difPl3.textChanged[str].connect(self.TextChengedPl3)
        
        
        cancelButton.clicked.connect(self.Close)
        cancelButton.move(60,20)   
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('QCheckBox')
        grid.addWidget(text1,0,0)
        grid.addWidget(text2,3,0)
        grid.addWidget(text3,4,0)
        
        grid.addWidget(self.status,0,2)
        grid.addWidget(self.setPlayersNum,0,1)
        
        grid.addWidget(self.playerOne,1,1)
        grid.addWidget(self.playerOneAi,2,1)
        grid.addWidget(self.playerTwo,1,2) 
        grid.addWidget(self.playerTwoAi,2,2)
        grid.addWidget(self.playerThree,1,3)
        grid.addWidget(self.playerThreeAi,2,3)
        
        grid.addWidget(cancelButton,0,3)
        
        grid.addWidget(self.difAi1,4,1)
        grid.addWidget(self.difPl1,3,1)
        grid.addWidget(self.difAi2,4,2)
        grid.addWidget(self.difPl2,3,2)
        grid.addWidget(self.difAi3,4,3)
        grid.addWidget(self.difPl3,3,3)
        
        grid.addWidget(self.errorLabel1,5,1)
        grid.addWidget(self.errorLabel2,5,2)
        grid.addWidget(self.errorLabel3,5,3)
        
        self.setWindowTitle("Settings")
        self.show()
    
    def initUI1(self):      
        
        grid = QGridLayout(self)
        self.setLayout(grid)
        
        
        text2 = QLabel('Hostile Ai difficulty')
        text3 = QLabel('Player Ai')
        
        self.errorLabel1 =  QLabel(self)
        self.errorLabel2 =  QLabel(self)
        self.errorLabel3 =  QLabel(self)
        
        self.status =QLabel(self)
        
        self.errorLabel1.setText("Error status\n"+str(self.error[0]))
        self.errorLabel2.setText("Error status\n"+str(self.error[1]))
        self.errorLabel3.setText("Error status\n"+str(self.error[2]))
        
        
        
        self._togglep1 =True
        self.playerOne = QCheckBox('Player 1 is human', self)
        self.playerOne.toggle()
        self.playerOne.clicked.connect(self.togglep1)
        self.playerOneAi = QCheckBox('Player 1 is AI', self)
        self.playerOneAi.clicked.connect(self.togglep1)
        
        self._togglep2 =True
        self.playerTwo = QCheckBox('Player 2 is human', self)
        self.playerTwo.toggle()
        self.playerTwo.clicked.connect(self.togglep2)
        self.playerTwoAi = QCheckBox('Player 2 is AI', self)
        self.playerTwoAi.clicked.connect(self.togglep2)
        self.playerTwo.setDisabled(True)
        self.playerTwoAi.setDisabled(True)
        
        self._togglep3 =True
        self.playerThree = QCheckBox('Player 3 is human', self)
        self.playerThree.toggle()
        self.playerThree.clicked.connect(self.togglep3)
        self.playerThreeAi = QCheckBox('Player 3 is AI', self)
        self.playerThreeAi.clicked.connect(self.togglep3)
        self.playerThreeAi.setDisabled(True)
        self.playerThree.setDisabled(True)
        cancelButton = QPushButton('Done',self)
        
        self.difAi1 = QLineEdit(self)
        self.difAi1.setText("1")
        self.difAi1.textChanged[str].connect(self.TextChengedAi1)
        self.difPl1 = QLineEdit(self)
        self.difPl1.setText("1")
        self.difPl1.textChanged[str].connect(self.TextChengedPl1)
        self.difAi2 = QLineEdit(self)
        self.difAi2.setText("1")
        self.difAi2.setReadOnly(True)
        self.difAi2.textChanged[str].connect(self.TextChengedAi2)
        self.difPl2 = QLineEdit(self)
        self.difPl2.setText("1")
        self.difPl2.setReadOnly(True)
        self.difPl2.textChanged[str].connect(self.TextChengedPl2)
        self.difAi3 = QLineEdit(self)
        self.difAi3.setText("1")
        self.difAi3.setReadOnly(True)
        self.difAi3.textChanged[str].connect(self.TextChengedAi3)
        self.difPl3 = QLineEdit(self)
        self.difPl3.setText("1")
        self.difPl3.setReadOnly(True)
        self.difPl3.textChanged[str].connect(self.TextChengedPl3)
        
        
        cancelButton.clicked.connect(self.Close)
        cancelButton.move(60,20)   
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('QCheckBox')
        
        grid.addWidget(text2,3,0)
        grid.addWidget(text3,4,0)
        
        grid.addWidget(self.status,0,2)
        
        
        grid.addWidget(self.playerOne,1,1)
        grid.addWidget(self.playerOneAi,2,1)
        grid.addWidget(self.playerTwo,1,2) 
        grid.addWidget(self.playerTwoAi,2,2)
        grid.addWidget(self.playerThree,1,3)
        grid.addWidget(self.playerThreeAi,2,3)
        
        grid.addWidget(cancelButton,0,3)
        
        grid.addWidget(self.difAi1,4,1)
        grid.addWidget(self.difPl1,3,1)
        grid.addWidget(self.difAi2,4,2)
        grid.addWidget(self.difPl2,3,2)
        grid.addWidget(self.difAi3,4,3)
        grid.addWidget(self.difPl3,3,3)
        
        grid.addWidget(self.errorLabel1,5,1)
        grid.addWidget(self.errorLabel2,5,2)
        grid.addWidget(self.errorLabel3,5,3)
        
        grid
        self.show()
        
    def initUI2(self):      
        
        grid = QGridLayout(self)
        self.setLayout(grid)
        
        
        text2 = QLabel('Hostile Ai difficulty')
        text3 = QLabel('Player Ai')
        
        self.errorLabel1 =  QLabel(self)
        self.errorLabel2 =  QLabel(self)
        self.errorLabel3 =  QLabel(self)
        
        self.status =QLabel(self)
        
        self.errorLabel1.setText("Error status\n"+str(self.error[0]))
        self.errorLabel2.setText("Error status\n"+str(self.error[1]))
        self.errorLabel3.setText("Error status\n"+str(self.error[2]))
        
        
        
        self._togglep1 =True
        self.playerOne = QCheckBox('Player 1 is human', self)
        self.playerOne.toggle()
        self.playerOne.clicked.connect(self.togglep1)
        self.playerOneAi = QCheckBox('Player 1 is AI', self)
        self.playerOneAi.clicked.connect(self.togglep1)
        self.playerOne.setDisabled(True)
        self.playerOneAi.setDisabled(True)
        
        self._togglep2 =True
        self.playerTwo = QCheckBox('Player 2 is human', self)
        self.playerTwo.toggle()
        self.playerTwo.clicked.connect(self.togglep2)
        self.playerTwoAi = QCheckBox('Player 2 is AI', self)
        self.playerTwoAi.clicked.connect(self.togglep2)
        
        
        self._togglep3 =True
        self.playerThree = QCheckBox('Player 3 is human', self)
        self.playerThree.toggle()
        self.playerThree.clicked.connect(self.togglep3)
        self.playerThreeAi = QCheckBox('Player 3 is AI', self)
        self.playerThreeAi.clicked.connect(self.togglep3)
        self.playerThreeAi.setDisabled(True)
        self.playerThree.setDisabled(True)
        cancelButton = QPushButton('Done',self)
        
        self.difAi1 = QLineEdit(self)
        self.difAi1.setText("1")
        self.difAi1.textChanged[str].connect(self.TextChengedAi1)
        self.difPl1 = QLineEdit(self)
        self.difPl1.setText("1")
        self.difPl1.textChanged[str].connect(self.TextChengedPl1)
        self.difAi2 = QLineEdit(self)
        self.difAi2.setText("1")
        self.difAi1.setReadOnly(True)
        self.difAi2.textChanged[str].connect(self.TextChengedAi2)
        self.difPl2 = QLineEdit(self)
        self.difPl2.setText("1")
        self.difPl1.setReadOnly(True)
        self.difPl2.textChanged[str].connect(self.TextChengedPl2)
        self.difAi3 = QLineEdit(self)
        self.difAi3.setText("1")
        self.difAi3.setReadOnly(True)
        self.difAi3.textChanged[str].connect(self.TextChengedAi3)
        self.difPl3 = QLineEdit(self)
        self.difPl3.setText("1")
        self.difPl3.setReadOnly(True)
        self.difPl3.textChanged[str].connect(self.TextChengedPl3)
        
        
        cancelButton.clicked.connect(self.Close)
        cancelButton.move(60,20)   
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('QCheckBox')
        
        grid.addWidget(text2,3,0)
        grid.addWidget(text3,4,0)
        
        grid.addWidget(self.status,0,2)
        
        
        grid.addWidget(self.playerOne,1,1)
        grid.addWidget(self.playerOneAi,2,1)
        grid.addWidget(self.playerTwo,1,2) 
        grid.addWidget(self.playerTwoAi,2,2)
        grid.addWidget(self.playerThree,1,3)
        grid.addWidget(self.playerThreeAi,2,3)
        
        grid.addWidget(cancelButton,0,3)
        
        grid.addWidget(self.difAi1,4,1)
        grid.addWidget(self.difPl1,3,1)
        grid.addWidget(self.difAi2,4,2)
        grid.addWidget(self.difPl2,3,2)
        grid.addWidget(self.difAi3,4,3)
        grid.addWidget(self.difPl3,3,3)
        
        grid.addWidget(self.errorLabel1,5,1)
        grid.addWidget(self.errorLabel2,5,2)
        grid.addWidget(self.errorLabel3,5,3)
        
        grid
        self.show()
        
    def initUI3(self):      
        
        grid = QGridLayout(self)
        self.setLayout(grid)
        
        
        text2 = QLabel('Hostile Ai difficulty')
        text3 = QLabel('Player Ai')
        
        self.errorLabel1 =  QLabel(self)
        self.errorLabel2 =  QLabel(self)
        self.errorLabel3 =  QLabel(self)
        
        self.status =QLabel(self)
        
        self.errorLabel1.setText("Error status\n"+str(self.error[0]))
        self.errorLabel2.setText("Error status\n"+str(self.error[1]))
        self.errorLabel3.setText("Error status\n"+str(self.error[2]))
        
        
        
        self._togglep1 =True
        self.playerOne = QCheckBox('Player 1 is human', self)
        self.playerOne.toggle()
        self.playerOne.clicked.connect(self.togglep1)
        self.playerOneAi = QCheckBox('Player 1 is AI', self)
        self.playerOneAi.clicked.connect(self.togglep1)
        
        self._togglep2 =True
        self.playerTwo = QCheckBox('Player 2 is human', self)
        self.playerTwo.toggle()
        self.playerTwo.clicked.connect(self.togglep2)
        self.playerTwoAi = QCheckBox('Player 2 is AI', self)
        self.playerTwoAi.clicked.connect(self.togglep2)
        self.playerTwo.setDisabled(True)
        self.playerTwoAi.setDisabled(True)
        
        self._togglep3 =True
        self.playerThree = QCheckBox('Player 3 is human', self)
        self.playerThree.toggle()
        self.playerThree.clicked.connect(self.togglep3)
        self.playerThreeAi = QCheckBox('Player 3 is AI', self)
        self.playerThreeAi.clicked.connect(self.togglep3)
        self.playerOneAi.setDisabled(True)
        self.playerOne.setDisabled(True)
        cancelButton = QPushButton('Done',self)
        
        self.difAi1 = QLineEdit(self)
        self.difAi1.setText("1")
        self.difAi1.textChanged[str].connect(self.TextChengedAi1)
        self.difPl1 = QLineEdit(self)
        self.difPl1.setText("1")
        self.difPl1.textChanged[str].connect(self.TextChengedPl1)
        self.difAi2 = QLineEdit(self)
        self.difAi2.setText("1")
        self.difAi2.setReadOnly(True)
        self.difAi2.textChanged[str].connect(self.TextChengedAi2)
        self.difPl2 = QLineEdit(self)
        self.difPl2.setText("1")
        self.difPl2.setReadOnly(True)
        self.difPl2.textChanged[str].connect(self.TextChengedPl2)
        self.difAi3 = QLineEdit(self)
        self.difAi3.setText("1")
        self.difAi1.setReadOnly(True)
        self.difAi3.textChanged[str].connect(self.TextChengedAi3)
        self.difPl3 = QLineEdit(self)
        self.difPl3.setText("1")
        self.difPl1.setReadOnly(True)
        self.difPl3.textChanged[str].connect(self.TextChengedPl3)
        
        
        cancelButton.clicked.connect(self.Close)
        cancelButton.move(60,20)   
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('QCheckBox')
        
        grid.addWidget(text2,3,0)
        grid.addWidget(text3,4,0)
        
        grid.addWidget(self.status,0,2)
        
        
        grid.addWidget(self.playerOne,1,1)
        grid.addWidget(self.playerOneAi,2,1)
        grid.addWidget(self.playerTwo,1,2) 
        grid.addWidget(self.playerTwoAi,2,2)
        grid.addWidget(self.playerThree,1,3)
        grid.addWidget(self.playerThreeAi,2,3)
        
        grid.addWidget(cancelButton,0,3)
        
        grid.addWidget(self.difAi1,4,1)
        grid.addWidget(self.difPl1,3,1)
        grid.addWidget(self.difAi2,4,2)
        grid.addWidget(self.difPl2,3,2)
        grid.addWidget(self.difAi3,4,3)
        grid.addWidget(self.difPl3,3,3)
        
        grid.addWidget(self.errorLabel1,5,1)
        grid.addWidget(self.errorLabel2,5,2)
        grid.addWidget(self.errorLabel3,5,3)
        
        grid
        self.show()
    
    
    def Activation(self,text):
        print(text)
        self.playersNum = int(text)
        #print(type(self.playersNum))
        if self.playersNum ==1:
            self.playerTwo.setDisabled(True)
            self.playerTwoAi.setDisabled(True)
            self.playerThree.setDisabled(True)
            self.playerThreeAi.setDisabled(True)
            self.difPl2.setReadOnly(True)
            self.difPl3.setReadOnly(True)
            self.difAi2.setReadOnly(True)
            self.difAi3.setReadOnly(True)
        if self.playersNum ==2:
            self.playerTwo.setDisabled(False)
            self.playerTwoAi.setDisabled(False)
            self.playerThree.setDisabled(True)
            self.playerThreeAi.setDisabled(True)
            self.difPl2.setReadOnly(False)
            self.difPl3.setReadOnly(False)
            self.difAi2.setReadOnly(True)
            self.difAi3.setReadOnly(True)
        if self.playersNum ==3:
            self.playerTwo.setDisabled(False)
            self.playerTwoAi.setDisabled(False)
            self.playerThree.setDisabled(False)
            self.playerThreeAi.setDisabled(False)
            self.difPl2.setReadOnly(False)
            self.difPl3.setReadOnly(False)
            self.difAi2.setReadOnly(False)
            self.difAi3.setReadOnly(False)
    
    def Close(self):
        if self.error[0] !=True and self.error[2] !=True and self.error[2] !=True:
            self.status.setText("all k go on")
            self.close()
        else:
            self.status.setText("Correct Data!")
        
    @pyqtSlot()    
    def togglep1(self):
        
        self._togglep1 = not self._togglep1
        self.playerOne.setChecked(self._togglep1)
        self.playerOneAi.setChecked(not self._togglep1)
        if self.playerOne.isChecked():
            self.isPlayer[0]=True
        else:
            self.isPlayer[0]=False
    
    @pyqtSlot()    
    def togglep2(self):
        
        self._togglep2 = not self._togglep2
        self.playerTwo.setChecked(self._togglep2)
        self.playerTwoAi.setChecked(not self._togglep2)
        if self.playerTwo.isChecked():
            self.isPlayer[1]=True
        else:
            self.isPlayer[1]=False
    
    @pyqtSlot()    
    def togglep3(self):
        
        self._togglep3 = not self._togglep3
        self.playerThree.setChecked(self._togglep3)
        self.playerThreeAi.setChecked(not self._togglep3)
        if self.playerThree.isChecked():
            self.isPlayer[2]=True
        else:
            self.isPlayer[2]=False
        
        
    def TextChengedAi1(self,data):
        try:
            self.aiDifficult[0] = int(data)
            if self.aiDifficult[0]>0:
                self.error[0]= False
                self.errorLabel1.setText("Error status\n"+str(self.error[0]))
            else:
                self.error[0]= True
                self.errorLabel1.setText("Error status\n"+str(self.error[0]))
        except ValueError:
            self.error[0]= True
            self.errorLabel1.setText("Error status\n"+str(self.error[0]))
        
    def TextChengedPl1(self,data):
        try:
            self.plDifficult[0] = int(data)
            if self.plDifficult[0]>0:
                self.error[0]= False
                self.errorLabel1.setText("Error status\n"+str(self.error[0]))
            else:
                self.error[0]= True
                self.errorLabel1.setText("Error status\n"+str(self.error[0]))
        except ValueError:
            self.error[0]= True
            self.errorLabel1.setText("Error status\n"+str(self.error[0]))    
    
    def TextChengedAi2(self,data):
        try:
            self.aiDifficult[1] = int(data)
            if self.aiDifficult[1]>0:
                self.error[1]= False
                self.errorLabel2.setText("Error status\n"+str(self.error[1]))
            else:
                self.error[1]= True
                self.errorLabel2.setText("Error status\n"+str(self.error[1]))
        except ValueError:
            self.error[1]= True
            self.errorLabel1.setText("Error status\n"+str(self.error[1]))
    def TextChengedPl2(self,data):
        try:
            self.plDifficult[1] = int(data)
            if self.plDifficult[1]>0:
                self.error[1]= False
                self.errorLabel2.setText("Error status\n"+str(self.error[1]))
            else:
                self.error[1]= True
                self.errorLabel2.setText("Error status\n"+str(self.error[1]))
        except ValueError:
            self.error[1]= True
            self.errorLabel2.setText("Error status\n"+str(self.error[1]))
    
    def TextChengedAi3(self,data):
        try:
            self.aiDifficult[2] = int(data)
            if self.aiDifficult[2]>0:
                self.error[2]= False
                self.errorLabel3.setText("Error status\n"+str(self.error[2]))
            else:
                self.error[2]= True
                self.errorLabel3.setText("Error status\n"+str(self.error[2]))
        except ValueError:
            self.error[2]= True
            self.errorLabel3.setText("Error status\n"+str(self.error[2]))
            
    def TextChengedPl3(self,data):
        try:
            self.plDifficult[2] = int(data)
            if self.plDifficult[2]>0:
                self.error[2]= False
                self.errorLabel3.setText("Error status\n"+str(self.error[2]))
            else:
                self.error[2]= True
                self.errorLabel3.setText("Error status\n"+str(self.error[2]))
        except ValueError:
            self.error[2]= True
            self.errorLabel3.setText("Error status\n"+str(self.error[2]))


class InittRoi(QDialog):
    
    def __init__(self,playersNum):
        
        super().__init__()
        self.playersNum = playersNum
        self.iniUi()
    
    def iniUi(self):
        
        self.roi =QLabel(self)
        self.roi.resize(400,400)
        self.roi.move(25,25)
        startButton=QPushButton('Correct Roi',self)
        startButton.resize(100,50)
        startButton.move(450,25)
        #self.setPlayersNum.activated[str].connect(self.Activation)
        cancelButton = QPushButton('Done',self)
        cancelButton.resize(100,50)
        cancelButton.move (450,100)
        
        self.setGeometry(300,300,550,500)
        self.setWindowTitle('Roi Correction')
        self.show()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = InittRoi(0)
    sys.exit(app.exec_())
