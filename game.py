
#основной файл который будет вызывать остальные и в котором будет происходить игровой цикл
import urx #библиотека для общения с роботом
import chess #работа с игрой
import sys
from PyQt5.QtWidgets import QWidget, QAction, qApp, QApplication, QLabel,QGridLayout
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.Qt import QTextEdit, QVBoxLayout, QPushButton, QHBoxLayout
from PyQt5.QtCore import Qt
from _multiprocessing import send
import cv2
import numpy as np
from UtilityFucntions import *
import Gui
import InitScreen
from chessAi import *
import time
from Threads import *
from PyQt5 import QtCore
from pygame.mixer_music import play
from numpy.f2py.auxfuncs import isfalse
from urx.ursecmon import TimeoutException



class MainGame(QWidget):
    "it` a game class"
    def __init__(self,debug,playersNum):
        super().__init__()
        self.debug = debug
        
#         try:
#             while True:
#                 done = self.connect2Robot()
#                 if type(done)!='None':
#                     break
#         except TimeoutException:
#             pass
        
        if  self.debug:
            self.debug = debug
            print('this is debug mode')
        else:
            print('all fine')
        
        dialog = InitScreen.InitScreen(0)
        dialog.exec()
        #print('tratatata',dialog.playersNum)
            
        self.playersNum = dialog.playersNum    
              
        self.difficulties =dialog.plDifficult
        self.aiDifficulties=dialog.aiDifficult
        self.players = dialog.isPlayer
        self.isdone = True
        self.curPlayer = [0,1]
        self.loopDone = True
        self.InitUI(False)
        
        self.InitDraw()
    
    def connect2Robot(self):
            self.robot = urx.Robot("192.168.1.20", use_rt=True)
            return(self.robot)
            
    def InitUI(self,old): 
        
        
        
        if old==False:
            
            
            self.buttonsPause=[]
            self.buttonsChange=[]
            self.buttonsReset=[]
            self.buttonsStop=[]
            self.playerNamesLabels = []
            self.aiNamesLabels = []
            self.chessboardDisplays = []
            self.turn = ['w','w','w']
            self.curTurn = []
            self.logs = []

            
            
            for i in range(self.playersNum):

                self.playerNamesLabels.append(QLabel(self))
                if self.players[i]==True:
                    self.playerNamesLabels[i].setText("Player \nPlayer "+str(i+1))
                else:
                    self.playerNamesLabels[i].setText("Player \n Ai:"+str(self.aiDifficulties[i]))
                self.playerNamesLabels[i].resize(80,40)
                self.playerNamesLabels[i].move(500*i,0)
                
                self.aiNamesLabels.append(QLabel(self))
                self.aiNamesLabels[i].setText("Robot\n AI:"+ str(self.difficulties[i]))
                self.aiNamesLabels[i].resize(80,40)
                self.aiNamesLabels[i].move(500*i,55)
  
                self.curTurn.append(QLabel('123',self))
                if self.turn[i]=='w':
                    self.curTurn[i].setText('Current\n Turn:\n White')
                else:
                    self.curTurn[i].setText('Current\n Turn:\n Black')
                self.curTurn[i].resize(80,80)
                self.curTurn[i].move(500*i,110)    

                
                self.buttonsChange.append(QPushButton('Change settings',self))
                self.buttonsChange[i].clicked.connect(self.ChangeSetting)
                
                self.buttonsPause.append(QPushButton('Pause',self))
                self.buttonsReset.append(QPushButton('Restart',self))
                self.buttonsReset[i].clicked.connect(self.Restart)
                self.buttonsStop.append(QPushButton('Stop',self))
                self.buttonsStop[i].clicked.connect(self.StopGame)
                self.buttonsStop[i].clicked.connect(self.StopGame)
                self.buttonsChange[i].resize(150,40)
                self.buttonsChange[i].move(80+500*i,540)
                self.buttonsPause[i].resize(150,40)
                self.buttonsPause[i].move(80+500*i,590)  
                self.buttonsReset[i].resize(150,40)
                self.buttonsReset[i].move(250+500*i,540)
                self.buttonsStop[i].resize(150,40)
                self.buttonsStop[i].move(250+500*i,590)

                  
                  
                self.logs.append(QTextEdit(self))
                self.logs[i].setReadOnly(True)
                self.logs[i].resize(400,100)
                self.logs[i].move(55+500*i,420)
                  

                  
                self.chessboardDisplays.append(QLabel(self))
                self.chessboardDisplays[i].setPixmap(QPixmap("images/BoardBase.png"))
                self.chessboardDisplays[i].resize(400,400)
                self.chessboardDisplays[i].move(55+500*i,0)
                  

            self.setWindowTitle('ChessGamer')
            self.setGeometry(100, 100, 520*self.playersNum, 640)
            self.setFixedSize(520*self.playersNum, 640)
            

            self.show()
        else:
            sendButton = QPushButton("Send",self)
        
            cancelButton = QPushButton('Exit',self)
            cancelButton.clicked.connect(qApp.quit)
            self.textBox = QTextEdit()
            self.textBox.setReadOnly(True)
        
            self.textEdit = QTextEdit()
        
            self.pic = QLabel()
        
        
            self.pic.setPixmap(QPixmap("images/BoardBase.png"))
            self.pic.resize(350,350)
            self.pic.show()
        
            self.debugBoard =chess.Board()
            if self.debug:
                print('this is board in init: ',self.debugBoard)
            sendButton.clicked.connect(self.DrawBoard)
        
            vbox = QVBoxLayout()
            hbox = QHBoxLayout()
            hbox.addStretch(1)
            vbox.addStretch(1)
            hbox.addWidget(sendButton)
            hbox.addWidget(cancelButton)
            vbox.addWidget(self.pic)
            vbox.addWidget(self.textBox)
            vbox.addLayout(hbox)
            
       
        
            self.setGeometry(500, 300, 300, 200)
            self.setWindowTitle('ChessGamer')
            self.setLayout(vbox) 
            self.show()  
    
    
    def ChangeSetting(self):   
        
        self.close()
        self.__init__(False, 1)
        self.GameLoop()
        
        
    
    def InitDraw(self):
        #gameboard picture
        fontWhite = cv2.imread("images/white_square.png")
        fontBlack = cv2.imread("images/brown_square.png")  
        boardPic = np.zeros((400,400,3),dtype=np.uint8)
        tick =0
        
        for x in range(8):
            for y in range(8):
                
                if x%2 == 0:
                    if tick %2==0:
                    
                        boardPic[50*x:50+50*x,50*y:50+50*y]  = fontWhite
                
                    else:
                    
                        boardPic[50*x:50+50*x,50*y:50+50*y]  = fontBlack
                        
                    
                else:
                
                    if tick %2==0:
                    
                        boardPic[50*x:50+50*x,50*y:50+50*y]  = fontBlack
                
                    else:
                    
                        boardPic[50*x:50+50*x,50*y:50+50*y]  = fontWhite
                        
                tick += 1
        if self.debug:
            cv2.imshow("BoardPic",boardPic)
        else:
            cv2.imwrite("images/BoardBase.png",boardPic)
       
    def DrawBoard(self,board,player):
        if self.debug:
            print("im in drawBoardCall")
            try:
                board = self.debugBoard
            except AttributeError:
                pass
        
        stringBoard=Board2String(board)
        boardPic = DrawBoardPic(stringBoard, self.debug)
        tmpImagename = "images/tmp"+str(player)+".png"    
        cv2.imwrite(tmpImagename,boardPic)
        
        self.chessboardDisplays[player-1].setPixmap(QPixmap(tmpImagename))
        self.chessboardDisplays[player-1].show()

    def DrawGui(self):

        if self.playersNum ==1:
            self.chessboardDisplays[0].setPixmap(QPixmap('images/tmp0.png'))
            self.chessboardDisplays[0].show()
        if self.playersNum ==2:
            self.chessboardDisplays[0].setPixmap(QPixmap('images/tmp0.png'))
            self.chessboardDisplays[0].show()
            self.chessboardDisplays[1].setPixmap(QPixmap('images/tmp1.png'))
            self.chessboardDisplays[1].show()
        if self.playersNum ==3:
            self.chessboardDisplays[0].setPixmap(QPixmap('images/tmp0.png'))
            self.chessboardDisplays[0].show()
            self.chessboardDisplays[1].setPixmap(QPixmap('images/tmp1.png'))
            self.chessboardDisplays[1].show()
            self.chessboardDisplays[2].setPixmap(QPixmap('images/tmp2.png'))
            self.chessboardDisplays[2].show()
   
    def Draw(self,board,player):
        
        if player ==0:
            self.garbage = 0
            self.drawThread = DrawThread(board,player)
            self.drawThread.finished.connect(self.DrawGui)
            self.drawThread.start()
            
        if player ==1:
            self.garbage = 1
            self.drawThread1 = DrawThread(board,player)
            self.drawThread1.finished.connect(self.DrawGui)
            self.drawThread1.start()
        if player ==2:
            self.garbage = 2
            self.drawThread2 = DrawThread(board,player)
            self.drawThread2.finished.connect(self.DrawGui)
            self.drawThread2.start()
     
    def GainDataFromThread(self,strData):    
        self.gainedData=strData
        #print('this is data in main loop',strData)
        
    def MoveDone(self):
        self.isdone=True
        
    
    def LoopThreadDone(self):
        
        
        self.loopDone = True
        
        if self.isdone:
            a = int(self.gainedData[0:self.gainedData.find("-")])
            b = int(self.gainedData[self.gainedData.find("-")+1:len(self.gainedData)])
            move=chess.Move.from_uci(square2Uci(a)+square2Uci(b))
            prevBoard=self.playerStatus[self.curPlayer[0]][0]
            self.playerStatus[self.curPlayer[0]][0].push(move)
            self.isdone=False
            robotMoveThread=RoboWorker(self.curPlayer[0],[a,b],[prevBoard,self.playerStatus[self.curPlayer[0]][0]],self.robot) 
            robotMoveThread.doneSignal.connect(self.MoveDone)
            robotMoveThread.start()
        self.Draw(self.playerStatus[0][0],0)
        
        
        if self.playersNum>1:
            
            
            if self.curPlayer[0]==0 and self.playersNum==2:
                self.curPlayer[0]=1
            elif self.curPlayer[0]==1 and self.playersNum==2:
                self.curPlayer[0]=0
            
                
        if self.playersNum==3:        
            
            if self.curPlayer[0]==0  and self.curPlayer[1]==1:
                self.curPlayer[0]=1
            elif self.curPlayer[0]==1  and self.curPlayer[1]==1:
                self.curPlayer[0]=2
                self.curPlayer[1]=0
            elif self.curPlayer[0]==2  and self.curPlayer[1]==0:
                self.curPlayer[0]=1
            elif self.curPlayer[0]==1  and self.curPlayer[1]==0:
                self.curPlayer[0]=0
                self.curPlayer[1]=1
        
        
        
    def Loop(self):           
            
            #print('123',self.playersNum)
            currentPlayer = self.curPlayer[0]
            self.Draw(self.playerStatus[currentPlayer][0],currentPlayer)
            #print('Run loop with player num:',currentPlayer)
            #print('Current turn',BoardTurn(self.playerStatus[self.curPlayer[0]][0]))
            if self.playerStatus[currentPlayer][4]==False:
                
                if BoardTurn(self.playerStatus[self.curPlayer[0]][0]) =='w':
                    if self.playerStatus[self.curPlayer[0]][1]:
                        pass
                        #print('player Move')
                        #wait for videosource
                    else:
                        if self.loopDone and self.isdone:
                        
                            self.loopDone = False
                        
                            #print('self.curPlayer',currentPlayer)
                        
                            gameThread = GameLoop(self.playerStatus[currentPlayer][0],self.playerStatus[currentPlayer][2],self.engine)
                            gameThread.dataSignal[str].connect(self.GainDataFromThread)
                            gameThread.finished.connect(self.LoopThreadDone)
                            if gameThread.isFinished:
                                gameThread.start()
                else:
                    if self.loopDone and self.isdone:
                        self.loopDone = False
                    
                        print('self.curPlayer',currentPlayer)
                        gameThread1 = GameLoop(self.playerStatus[currentPlayer][0],self.playerStatus[currentPlayer][3],self.engine)
                        gameThread1.dataSignal[str].connect(self.GainDataFromThread)
                        gameThread1.finished.connect(self.LoopThreadDone)
                        if gameThread1.isFinished:
                            gameThread1.start()
                    
                if self.playersNum==1:
                    self.curPlayer[0]=0
                if self.playersNum==2:
                    pass
                if self.playersNum==3:
                    pass
            
            self.Draw(self.playerStatus[currentPlayer][0],currentPlayer)    
            
            
            
            
    def StopGame(self,number):        
            print(number)
            
            
    def Restart(self):       
           self.timer.start(0)  
            
            
            
            
            

                 
            
    
    def GameLoop(self):
        
        self.playerStatus =[]
        self.engine = ChessEngine(False)
        boards = []
        
        for i in range(self.playersNum):
            #playersStatus[доска,Тип игрока(True игрок),сложность ИИ робота, сложность ИИ игрока,Игра окончена(True\False)]
            self.playerStatus.append([chess.Board(),self.players[i],self.difficulties[i],self.aiDifficulties[i],False])
            #print(self.playerStatus[i])
            boards.append(chess.Board())  
            
            
            self.Draw(self.playerStatus[i][0],i)
            
        #print('playersStats',self.playerStatus)
        self.timer = QtCore.QTimer()
        #self.timer.timeout.connect(self.Loop)
        self.timer.setInterval(1000)
        self.timer.start(1) 
        
            
            
            
    
    
                


if __name__ == '__main__':
    app = QApplication(sys.argv)
    
       
    game = MainGame(False,3)
    
    game.GameLoop()
    
    sys.exit(app.exec_())

    