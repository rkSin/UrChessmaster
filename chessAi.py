import chess
import chess.uci
import sys
from UtilityFucntions import *

    
class ChessEngine():
    def __init__(self,debug):
        super().__init__()
        self.debug = debug
        self.EngineInit()
    
    def EngineInit(self):
        self.engine = chess.uci.popen_engine("engine/stockfish_9_x64_popcnt.exe")
        if self.debug:
            print("enigine init done")
    
    def GenerateMove(self,board,difficult):
        self.engine.position(board)
        
        bestMove = self.engine.go(movetime=difficult)
            
                
        print(type(bestMove))
        try :
            print(square2Uci(bestMove[0].from_square))
            print(square2Uci(bestMove[0].to_square))
            data = str(bestMove[0].from_square)+"-"+str(bestMove[0].to_square)
            return(data)
        except AttributeError:
            data = str(bestMove[1].from_square)+"-"+str(bestMove[1].to_square)
            return(data)
        
        
        


if __name__ == '__main__':
    
    
       
    game = ChessEngine(True)
    testBoard = chess.Board()
    print(game.GenerateMove(testBoard,1000)[0])
    
    