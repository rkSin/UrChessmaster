import cv2
import numpy as np
import dataStructers
from PIL import Image
from PyQt5.QtCore import QThread, QObject, pyqtSignal
import time
import chess
from UtilityFucntions import *
from chessAi import *
from distutils.log import debug
import urx

class GameLoop(QThread):
    #print('thread object')
    """
    Input: Board, Difficulty, Engine
    This is game loop thread
    """
    dataSignal = pyqtSignal(str)
    
    def __init__(self,board,difficlulty,engine):
       
        super().__init__()
        self.board= board
        self.difficlulty = difficlulty
        
        self.engine = engine
        #print(' Game thread init done')
        
    def __del__(self):
        
        if self.isRunning():
            self.wait()
    
    def gameLoopThread(self,debug):
        
            move = self.engine.GenerateMove(self.board, self.difficlulty)
            print('this is best move',move)
            #self.board.push(move)
            self.dataSignal.emit(move)
            time.sleep(1)
            #return(self.board)
            if debug:
                print ('Game loop thread Done')
    
    def run(self):
        
        board = self.gameLoopThread(False)
        
    
        
            
    
 
        


class DrawThread(QThread):
    #print('thread object')
    """
    this class is constructing chess picture with figures
    depending on chess.board status
    
    trying 
    """
    def __init__(self,board,player):
        super().__init__()
        self.board= board
        self.player = player
        
    def __del__(self):
        if self.isRunning():
            self.wait()
     
    
              
    def DrawBoardPic(self,stringBoard,debug=False):
        #print("let`s run function")
        picStruct = {'r':'images/Chess_rdt60.png',
                     'n':'images/Chess_ndt60.png',
                     'b':'images/Chess_bdt60.png',
                     'q':'images/Chess_qdt60.png',
                     'k':'images/Chess_kdt60.png',
                     'p':'images/Chess_pdt60.png',
                     'R':'images/Chess_rlt60.png',
                     'N':'images/Chess_nlt60.png',
                     'B':'images/Chess_blt60.png',
                     'Q':'images/Chess_qlt60.png',
                     'K':'images/Chess_klt60.png',
                     'P':'images/Chess_plt60.png'}
    
        fontWhite = cv2.imread("images/white_square.png")
        fontBlack = cv2.imread("images/brown_square.png")  
        boardPic = np.zeros((400,400,3),dtype=np.uint8)
        tick =0
        stringPos = 0
        ticksTofig = 0
        status = True
        #print('starting tocreate pic')
        for x in range(8):
            for y in range(8):
                try:
                    if stringBoard[stringPos] == "/" and stringPos<=len(stringBoard):
                        stringPos+=1
                    
                    try:
                        if status:
                            ticksTofig = int(stringBoard[stringPos])
                        if debug:    
                            print('this is ticks to fig: ',ticksTofig)
                    except ValueError:
                            pass
                         
                except IndexError:
                    pass
                
                
                if x%2 == 0:
                    if tick %2==0:
                        if ticksTofig==0:
                            
                            boardPic[50*x:50+50*x,50*y:50+50*y]  = AddWithMask("images/white_square.png",picStruct[stringBoard[stringPos]])
                            
                        else:
                            boardPic[50*x:50+50*x,50*y:50+50*y] = fontWhite
                            status = False
                            ticksTofig =ticksTofig-1
                
                    else:
                        if ticksTofig==0:
                            boardPic[50*x:50+50*x,50*y:50+50*y]  = AddWithMask("images/brown_square.png",picStruct[stringBoard[stringPos]])
                            
                        else:
                            fb = fontBlack[:, :, ::-1]
                            boardPic[50*x:50+50*x,50*y:50+50*y]  = fb
                            ticksTofig =ticksTofig-1
                            status = False
                    
                else:
                
                    if tick %2==0:
                        
                    
                        if ticksTofig==0:
                            boardPic[50*x:50+50*x,50*y:50+50*y]  = AddWithMask("images/brown_square.png",picStruct[stringBoard[stringPos]])
                            
                        else:
                            fb = fontBlack[:, :, ::-1]
                            boardPic[50*x:50+50*x,50*y:50+50*y]  = fb
                            ticksTofig =ticksTofig-1
                            status = False
                
                    else:
                    
                        if ticksTofig==0:
                            boardPic[50*x:50+50*x,50*y:50+50*y]  = AddWithMask("images/white_square.png",picStruct[stringBoard[stringPos]])
                        else:
                            boardPic[50*x:50+50*x,50*y:50+50*y]  = fontWhite
                            ticksTofig =ticksTofig-1
                            status = False
                        
                tick += 1
                if debug:
                    print ('this is tick: ',tick)
               
                    if stringPos<=len(stringBoard):
                        try:
                            print('this is stringletter: ',stringBoard[stringPos])
                        
                        except IndexError:
                            pass
                if ticksTofig==0:
                    stringPos+=1
                    status = True
                
        return(boardPic)           
        cv2.imwrite('images/tmp0.png',boardPic)
        
        
    def run(self):
        #print('run draw in thread')
        #print(self.stringBoard)
        stringBoard = Board2String(self.board)
        pic = DrawBoardPic(stringBoard, False)
        
        string = 'images/tmp'+ str(self.player)+'.png'
        cv2.imwrite(string,pic)
     
class RoboWorker(QThread):
    
    doneSignal = pyqtSignal()
    
    def __init__(self,player,move,moveBoards,robot):
        super().__init__()
        self.player = player
        self.move = move
        self.moveBoards=moveBoards
        self.robot = robot
        self.acc = 0.1
        self.vel =0.1
    def __del__(self):
        
        if self.isRunning():
            self.wait()
    
    def ReturnCoords(self,square):
        tick = 0
        res=[0,0]
        for x in range(8):
            for y in range(8):
                if tick ==square:
                    res[1]=x
                    res[0]=y
                
                tick+=1    
        
        return(res)
            
        
    def MoveToZero(self):
        if self.player ==0:
            curPose = self.robot.getj()
            
            if curPose[0] >=1.0901128053665161 and curPose[0]<=dataStructers.playerOneJPose[0]:
                pass
            else:
                self.robot.movej(dataStructers.playerOneJPose, acc=0.1, vel=0.1)
        if self.player ==1:
            
            self.robot.movej(dataStructers.playerTwoJPose, acc=0.1, vel=0.1)
        if self.player ==2:
            
            self.robot.movej(dataStructers.playerThreePose, acc=0.1, vel=0.1)
    
    def CheckAtacked(self):
        pass
    
    def MakeMove(self):
        
        
        #print('this is move',self.move)
        #print('Move to square',to_square)
        boardStruct = stringBoard2Struct(self.moveBoards[0].fen())
        to_square = self.ReturnCoords(self.move[1])
        figure = boardStruct[self.move[1]]
        print('figure tha is needed to move ',figure)
        if figure:
        #''' move from square to square'''
            
            self.MoveXY(to_square, self.player)    
            self.GripFigure(figure,True) 
            #self.DropFigure(figure,  stringBoard2Struct(self.moveBoards[0].fen()))
            
            
        
            
        from_square =  self.ReturnCoords(self.move[0])
        #print('Move from square',from_square)
        boardStruct = stringBoard2Struct(self.moveBoards[0].fen())
        figure = boardStruct[self.move[0]]
        print('moving figure is',figure)
        self.MoveXY(from_square, self.player)
        #self.GripFigure(figure,True) 
        self.MoveXY(to_square, self.player)
        #self.GripFigure(figure,False)
        self.doneSignal.emit()
            
            
        
    
    def DropFigure(self,figure,listBoard):
        if figure in ['B','R','N','K','Q']:
            count = listBoard.count(figure)
            if count ==2:
                key = figure+"1"
            elif count ==1:
                key = figure+'2'
            position = dataStructers.figuresDropOneWhite
            position[0]+= 0.038* dataStructers.figuresDropPos[key][0]
            position[1]+= 0.038* dataStructers.figuresDropPos[key][1]
            self.robot.movel(position,self.acc,self.vel)
            self.GripFigure(figure,False) 
        elif figure=='P':
            tmp = ('8','7','6','5','4','3','2','1')
            print('this is count of Pawns on board',listBoard.count(figure))
            key  =figure+tmp[listBoard.count(figure)]
            position = dataStructers.figuresDropOneWhite
            position[0]+= 0.038* dataStructers.figuresDropPos[key][0]
            position[1]+= 0.038* dataStructers.figuresDropPos[key][1]
            self.robot.movel(position,self.acc,self.vel)
            self.GripFigure(figure,False)
        elif figure in ['b','r','n','k','q']:
            count = listBoard.count(figure)
            if count ==2:
                key = figure+"1"
            elif count ==1:
                key = figure+'2'
            position = dataStructers.figuresDropOneBlack
            position[0]+= 0.038* dataStructers.figuresDropPos[key][0]
            position[1]+= 0.038* dataStructers.figuresDropPos[key][1]
            self.robot.movel(position,self.acc,self.vel)
            self.GripFigure(figure,False)
        elif figure =='p':
            tmp = ('8','7','6','5','4','3','2','1')
            key  =figure+tmp[listBoard.count(figure)]
            position = dataStructers.figuresDropOneBlack
            position[0]+= 0.038* dataStructers.figuresDropPos[key][0]
            position[1]+= 0.038* dataStructers.figuresDropPos[key][1]
            self.robot.movel(position,self.acc,self.vel)
            self.GripFigure(figure,False)
            
    def MoveXY(self,square,player): 
        print('player',player)
        pose =[]
        if player ==0:
            pose = dataStructers.playerOneLPose
        elif player ==1:
            pose = dataStructers.playerTwoLPose
        elif player ==2:
            pose = dataStructers.playerThreeLPose
        poseToMove=pose.copy()
        poseToMove[0] =pose[0] + 0.038*square[0]
        poseToMove[1] = pose[1]+ 0.038*square[1]
        self.robot.movel (poseToMove, self.acc, self.vel)
        
    def GripFigure(self,figure,grip):
        pose = self.robot.getl()
        pose[2] -=dataStructers.figureGripStruc[figure]
        self.robot.movel (pose, self.acc, self.vel)
        # grip
        #if grip:
        # grip
        #else:
        # drop     
        pose[2] +=dataStructers.figureGripStruc[figure]
        self.robot.movel (pose, self.acc, self.vel)
        
    def run(self):
        
        print('MoveThread',self.move)
        self.MoveToZero()
        self.MakeMove()
        
        
        
if __name__ == '__main__':
    
    #testBoard = chess.Board()
    #engine = ChessEngine(False)
       
    #game = GameLoop(testBoard,100,engine)
    #game.gameLoopThread(True)
    
    robot = urx.Robot("192.168.1.20", use_rt=True)
    
    rm= RoboWorker(0,[5,12],[1,1],robot)
    rm.run()

     
 