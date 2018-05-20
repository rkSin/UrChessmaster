import cv2
picStruct = {'r':cv2.imread('images/Chess_tile_rd.png'),
             'n':cv2.imread('images/Chess_tile_nd.png'),
             'b':cv2.imread('images/Chess_tile_bd.png'),
             'q':cv2.imread('images/Chess_tile_qd.png'),
             'k':cv2.imread('images/Chess_tile_kd.png'),
             'p':cv2.imread('images/Chess_tile_pd.png'),
             'R':cv2.imread('images/Chess_tile_rl.png'),
             'N':cv2.imread('images/Chess_tile_nl.png'),
             'B':cv2.imread('images/Chess_tile_bl.png'),
             'Q':cv2.imread('images/Chess_tile_ql.png'),
             'K':cv2.imread('images/Chess_tile_kl.png'),
             'P':cv2.imread('images/Chess_tile_pl.png')}


figureGripStruc = {'r':0.01,'n':0.01,'b':0.01,'k':0.01,'q':0.01,'p':0.01,
                   'R':0.01,'N':0.01,'B':0.01,'K':0.01,'Q':0.01,'P':0.01,}

figuresDropPos = {'R1':[0,0],'R2':[0,1],'N1':[0,2],'N2':[0,3],'B1':[0,4],'B2':[0,5],'Q':[0,6],'K':[0,7],
                  'P1':[1,0],'P2':[1,1],'P3':[1,2],'P4':[1,3],'P5':[1,4],'P6':[1,5],'P7':[1,6],'P8':[1,7]}

figuresDropPos = {'r1':[0,0],'r2':[0,1],'n1':[0,2],'n2':[0,3],'b1':[0,4],'b2':[0,5],'q':[0,6],'k':[0,7],
                  'p1':[1,0],'p2':[1,1],'p3':[1,2],'p4':[1,3],'p5':[1,4],'p6':[1,5],'p7':[1,6],'p8':[1,7]}

figuresDropOneWhite = [1.749367356300354,
                 -1.547476593648092,
                 -2.7020931879626673,
                 -0.4850533644305628,
                 1.6391221284866333,
                 5.292202949523926]

figuresDropOneBlack = [1.749367356300354,
                       -1.547476593648092,
                       -2.7020931879626673,
                       -0.4850533644305628,
                       1.6391221284866333,
                       5.292202949523926]

playerOneJPose = [2.3685214519500732,
                  -2.047133270894186,
                  -2.4598169962512415,
                  -0.18449861208070928,
                  1.6375054121017456,
                  3.975792646408081]

playerOneLPose = [-0.09732080685276184,
                 0.2870880911505954,
                 0.07745986294849344,
                 0.02687277356235227,
                 -2.131265793757955,
                 2.2088345438841257]


playerTwoJPose = [0.8885269165039062,
                   -2.047133270894186,
                   -2.4597814718829554,
                   -0.18449861208070928,
                   1.6375293731689453,
                   3.975768566131592]

playerTwoLPose = [0.27707693345387663,
                  0.1229287095687264,
                  0.07745386032620757,
                  -1.1103325847609151,
                  -1.2471518571249813,
                  1.2194559647749499]
                   
playerThreePose = [1.749367356300354,
                 -1.547476593648092,
                 -2.7020931879626673,
                 -0.4850533644305628,
                 1.6391221284866333,
                 5.292202949523926]

boardStructure = ['a1','b1','c1','d1','e1','f1','g1','h1',
                  'a2','b2','c2','d2','e2','f2','g2','h2',
                  'a3','b3','c3','d3','e3','f3','g3','h3',
                  'a4','b4','c4','d4','e4','f4','g4','h4',
                  'a5','b5','c5','d5','e5','f5','g5','h5',
                  'a6','b6','c6','d6','e6','f6','g6','h6',
                  'a7','b7','c7','d7','e7','f7','g7','h7',
                  'a8','b8','c8','d8','e8','f8','g8','h8']





picStruct = {'r':cv2.resize(cv2.imread('images/Chess_tile_rd.png'),(50,50)),
             'n':cv2.resize(cv2.imread('images/Chess_tile_nd.png'),(50,50)),
             'b':cv2.resize(cv2.imread('images/Chess_tile_bd.png'),(50,50)),
             'q':cv2.resize(cv2.imread('images/Chess_tile_qd.png'),(50,50)),
             'k':cv2.resize(cv2.imread('images/Chess_tile_kd.png'),(50,50)),
             'p':cv2.resize(cv2.imread('images/Chess_tile_pd.png'),(50,50)),
             'R':cv2.resize(cv2.imread('images/Chess_tile_rl.png'),(50,50)),
             'N':cv2.resize(cv2.imread('images/Chess_tile_nl.png'),(50,50)),
             'B':cv2.resize(cv2.imread('images/Chess_tile_bl.png'),(50,50)),
             'Q':cv2.resize(cv2.imread('images/Chess_tile_ql.png'),(50,50)),
             'K':cv2.resize(cv2.imread('images/Chess_tile_kl.png'),(50,50)),
             'P':cv2.resize(cv2.imread('images/Chess_tile_pl.png'),(50,50))}