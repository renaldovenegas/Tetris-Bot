from board import Board
from piece import *

#Testing - see output in terminal

if __name__ == "__main__":
    board = Board(20, 10)
    piece = PieceL()
    J = PieceJ()
    J.rotate(2)
    I = PieceI()
    board.place_piece(piece, 0)
    board.display()
    board.place_piece(piece, 2)
    board.display()
    board.place_piece(piece, 4)
    board.display()
    board.place_piece(piece, 6)
    board.display()
    board.place_piece(piece, 8)
    board.display()
    board.place_piece(J, 1)
    board.display()
    board.place_piece(J, 3)
    board.display()
    board.place_piece(J, 5)
    board.display()
    board.place_piece(J, 7)
    board.display()
    board.place_piece(I, 9)
    board.display()
    print("done!")