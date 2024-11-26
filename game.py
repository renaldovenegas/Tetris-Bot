from board import Board
from piece import *
import random

class Game:
    def __init__(self):
        self.board = Board(20, 10)
        self.pieces = set([PieceL(), PieceJ(), PieceI(), PieceO()])
        self.bag = self.pieces.copy()

        self.current_piece = self.bag.pop()
        self.queue = []
        while len(self.queue) < 4:
            if len(self.bag) > 0:
                self.queue.append(self.bag.pop())
            else:
                self.bag = self.pieces.copy()
                self.queue.append(self.bag.pop())

    def play(self):
        self.display()
        while True:
            input("Press enter to continue")

    def update_queue(self):
        self.current_piece = self.queue.pop(0)
        if len(self.bag) > 0:
            self.queue.append(self.bag.pop())
        else:
            self.bag = self.pieces.copy()
            self.queue.append(self.bag.pop())

    def play_search(self):
        self.display()
        while True:
            input("Press enter to continue")


    def play_random(self):
        self.display()
        while True:
            input("Press enter to continue")
            orientation = random.randint(1, self.current_piece.num_orientations)
            self.current_piece.rotate(orientation - 1)
            position = random.randint(0, self.board.num_columns - self.current_piece.num_cols)
            self.board.place_piece(self.current_piece, position)
            self.update_queue()
            self.display()
            if self.board.is_game_over():
                print("Game over!")
                break

    def display(self):
        print("Current piece:", self.current_piece.name, "| Queue:", [piece.name for piece in self.queue])
        print("Height:", self.board.num_rows - self.board.height, "| Holes:", self.board.holes)
        self.board.display()