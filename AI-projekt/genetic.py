from tetris import Tetris
import numpy as np
from copy import deepcopy

# weigths: heightmax, heightmin, empty_holes

t = Tetris(start_level=29)
firsttrun = True
board, next_piece, level, cleared_rows, score, running = t.gameloop() 
# current_piece = t.piece

# print(current_piece.current_piece)
print(board)

def getBestMove(t, weights):
    pass

while running:
    side = False
    t_test = deepcopy(t)
    current_piece = t_test.piece
    for rotation in range(4):
        if rotation == 0:
            current_piece.rotatePiece(0)
        else:
            current_piece.rotatePiece(1)
        for x in range(len(board[0])):
            for y in range(len(board)):
                current_piece.loc = [x, y]
                if t_test.board.checkSideCollision(current_piece, 1):
                    print(t_test.getRender())
                    # print(t_test.getRender()[:,current_piece.loc[0]][current_piece.loc[1]+1:])
                    # print(np.count_nonzero(t_test.getRender()[:,current_piece.loc[0]][current_piece.loc[1]+1:] == 0))

                    n_gaps = 0
                    checked_cols = []
                    for dy in range(len(current_piece.current_piece)):
                        for dx in range(len(current_piece.current_piece[0])):
                            if current_piece.current_piece[dy][dx] and dx not in checked_cols:
                                print(np.count_nonzero(t_test.getRender()[:,current_piece.loc[0]+dx][current_piece.loc[1]+1+dy:] == 0))
                                n_gaps += np.count_nonzero(t_test.getRender()[:,current_piece.loc[0]+dx][current_piece.loc[1]+1+dy:] == 0)
                                checked_cols.append(dx)
                    
                    for dy in range(len(current_piece.current_piece)):
                        if np.count_nonzero(current_piece.current_piece[dy] != 0) != 0:
                            top_height = current_piece.loc[1] - dy

                    for dy in range(len(current_piece), 0, -1):
                        if np.count_nonzero(current_piece.current_piece[dy - 1] != 0) != 0:
                            bottom_height = current_piece.loc[1] - dy
                    
                if t_test.board.checkDownCollision(current_piece):
                    # print(t_test.getRender())
                    # print(t_test.getRender()[:,current_piece.loc[0]][current_piece.loc[1]+1:])
                    # print(np.count_nonzero(t_test.getRender()[:,current_piece.loc[0]][current_piece.loc[1]+1:] == 0))
                    break
                if len(current_piece.current_piece[0]) + current_piece.loc[0] == len(board[0]):
                    print("Far edge")
                    side = True
                    
            if side:
                side = False
                break
    print(t.getRender())
    board, next_piece, level, cleared_rows, score, running = t.gameloop() 
    print("Checked all locations")
    