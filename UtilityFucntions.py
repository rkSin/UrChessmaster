import cv2
import numpy as np
import dataStructers
from PIL import Image
from PyQt5.QtCore import QThread, QObject, pyqtSignal
import time
import chess

def square2Uci(number):
    
    return(dataStructers.boardStructure[number])
    

def Board2String(board):
   
    stringBoard  = board.fen()
    return(stringBoard[0:stringBoard.find(" ")])

def BoardTurn(board):
    
    stringBoard  = board.fen()
    return(stringBoard[stringBoard.find(" ")+1])

def stringBoard2Struct(stringBoard,debug=False):
    
    data = [i for i in range(64)]
    
    tick =0
    stringPos = 0
    ticksTofig = 0
    status = True
    
    for x in range(8):
            base = 56-(8*x)
            
            for y in range(8):
                tick =base+y
                
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
                
                print(tick)
                
                if ticksTofig==0:
                            pass
                            data[tick]=stringBoard[stringPos]
                else:
                            pass
                            ticksTofig-=1
                            data[tick]= 0
                            status = False
                
                   
                        
                #tick += 1
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
                
    return(data)           

def DrawBoardPic(stringBoard,debug=False):
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
       
        
def AddWithMask (pic1,pic2,debug=False):
    
    pic1 = Image.open(pic1)
    pic2 = Image.open(pic2).convert("RGBA")
    pic1 = pic1.resize((50,50))
    pic2 = pic2.resize((50,50))
    res = Image.composite(pic2, pic1, pic2)
    #res.show()
    resCv= np.array(res)
    resCv = resCv[:, :, ::-1].copy()
    if debug:
        cv2.imshow('result',resCv)
        cv2.waitKey(0)
    return(res)

if __name__ == '__main__':
    import chess
    board = chess.Board()
    strBoard= Board2String(board)
    print (strBoard)
    #print(board.fen())
    #print('this is turn',BoardTurn(board))
    #print(BoardTurn(board))
    #bard = (Board2String(board))
    #print(board)
    #fenBoard = "rnbqkbnr/1ppppppp/8/p7/8/8/PPPPPPPP/RNBQKBNR"
    #pic = DrawBoardPic(fenBoard+"  ")
    #cv2.imshow('Image',pic)
    #cv2.waitKey(0)
    
    #AddWithMask(cv2.imread("images/brown_square.png"), cv2.resize(cv2.imread('images/Chess_bdt60.png'),(50,50)))
    #AddWithMask("images/white_square.png", "images/Chess_plt60.png")
    #AddWithMask("images/brown_square.png", "images/Chess_plt60.png")
    
    print(stringBoard2Struct(Board2String(board),False))       
    