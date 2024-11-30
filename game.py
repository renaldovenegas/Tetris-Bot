from board import Board
from piece import *
from rewards import *
import random

class Game:
    def __init__(self):
        """
        Initialize the game. Sets up the board, pieces, and bag.
        """
        self.board = Board(20, 10)
        self.pieces = set([PieceL(), PieceJ(), PieceI(), PieceO()])
        self.bag = self.pieces.copy()

        self.current_piece = self.bag.pop()
        self.queue = []
        while len(self.queue) < 4:
            if len(self.bag) == 0:
                self.bag = self.pieces.copy()
            self.queue.append(self.bag.pop())


    def update_queue(self):
        """
        Updates the current piece, as well as the queue. Adds a piece from the "bag" of pieces and resets bag
        if empty.
        """
        self.current_piece = self.queue.pop(0)
        if len(self.bag) == 0:
            self.bag = self.pieces.copy()
        self.queue.append(self.bag.pop())

    def play_search(self):
        self.display()
        while True:
            input("Press enter to continue")
            best, reward = forward_search_with_heurstic_pruning(5, self.board, self.current_piece, self.queue)
            self.current_piece.rotate(best[0])
            self.board.place_piece(self.current_piece, best[1])
            self.update_queue()
            self.display()
            if self.board.is_game_over():
                print("Game over!")
                break



    def play_random(self):
        """
        Play the game randomly until game over.
        The game is played until game over. At each iteration, the current piece is rotated randomly, placed randomly at the top of the board, 
        and then the queue of pieces is updated. The game state is displayed after each iteration.
        """
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
        """
        Print the current state of the game, including the current piece, queue of pieces to come, height of the board, and the number of holes in the board.
        """
        print("Current piece:", self.current_piece.name, "| Queue:", [piece.name for piece in self.queue])
        print("Height:", self.board.num_rows - self.board.height, "| Holes:", self.board.holes)
        self.board.display()