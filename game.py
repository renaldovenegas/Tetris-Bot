from board import Board
from piece import *
from rewards import *
import random

score_dict = {
    0: 0,
    1: 100,
    2: 300,
    3: 500,
    4: 800}

class Game:
    def __init__(self, simplified):
        """
        Initialize the game. Sets up the board, pieces, and bag.

        - simplified: If true, game is initialized with only the L, J, I, and O pieces. If not, game is initialized with all 7 pieces.
        """
        self.board = Board(20, 10)
        self.pieces = set([PieceL(), PieceJ(), PieceI(), PieceO(), PieceT(), PieceS(), PieceZ()])
        self.simplified = simplified
        if simplified:
            self.pieces = set([PieceL(), PieceJ(), PieceI(), PieceO()])
        self.num_pieces = len(self.pieces)
        self.bag = self.pieces.copy()
        self.score = 0

        if self.simplified:
            self.current_piece = self.bag.pop()
        else:
            # If not simplified, start with an I piece. This is to avoid a game starting with a S or Z piece which would 
            # cause the board to immediately have a hole.
            self.current_piece = PieceI()
            self.bag = set([PieceJ(), PieceL(), PieceO(), PieceT(), PieceS(), PieceZ()])

        self.queue = []
        while len(self.queue) < 4:
            if len(self.bag) == 0:
                self.bag = self.pieces.copy()
            cur = (random.sample(self.bag, 1)[0])
            self.queue.append(cur)
            self.bag.remove(cur)   


    def update_queue(self):
        """
        Updates the current piece, as well as the queue. Adds a piece from the "bag" of pieces and resets bag
        if empty.
        """
        self.current_piece = self.queue.pop(0)
        if len(self.bag) == 0:
            self.bag = self.pieces.copy()
        cur = (random.sample(self.bag, 1)[0])
        self.queue.append(cur)
        self.bag.remove(cur)    


    def play_search(self, depth=5, height_weight=16, rounds=100, anticipate_I=True):
        """
        Play the game using forward search with heurstic pruning. 
        The game is played until game over. At each iteration, the current piece is rotated, 
        placed at the top of the board, and then the queue of pieces is updated. The game state is displayed after each iteration.

        This agent is told there is always an I piece coming so that the planning can be done with an I piece in mind.

        - depth: The depth of the search tree. Value must be between 2 and 5, inclusive.
        - height_weight: The weight of the height heuristic.
        """
        self.display()
        for _ in range(rounds):
            # input("Press enter to continue")
            # Inserts an I piece into a copy of the queue, so the planning can be done with an I piece in mind.
            queue_copy = self.queue.copy()
            if anticipate_I:
                queue_copy[depth - 2] = PieceI()
            # Finds optimal move with forward search
            best, _ = forward_search_with_heurstic_pruning(depth, self.board, self.current_piece, queue_copy, height_weight)
            self.current_piece.rotate(best[0])
            lines = self.board.place_piece(self.current_piece, best[1])
            if lines == -1:
                self.display()
                print("Game over!")
                break
            self.score += score_dict[lines]
            self.update_queue()
            self.display()
        
        print("Score after", rounds, "rounds:", self.score)
        return self.score
    
    def play_naive(self, height_weight=16, rounds=100):
        """
        Play the game naively, maximizing the immediate heuristic reward for each piece. There is no pruning done: 
        Placing a piece that results in a hole is possible.The game is played until game over. 
        At each iteration, the current piece is rotated and placed such that the immediate herustic reward is maximized. 
        The game state is displayed after each iteration.
        """
        self.display()
        for _ in range(rounds):
            # input("Press enter to continue")
            best, _ = naive_search(self.board, self.current_piece, height_weight)
            self.current_piece.rotate(best[0])
            lines = self.board.place_piece(self.current_piece, best[1])
            if lines == -1:
                self.display()
                print("Game over!")
                break
            self.score += score_dict[lines]
            self.update_queue()
            self.display()
        
        print("Score after", rounds, "rounds:", self.score)
        return self.score

    def play_random(self, rounds=100):
        """
        Play the game randomly until game over.
        The game is played until game over. At each iteration, the current piece is rotated randomly, placed randomly at the top of the board, 
        and then the queue of pieces is updated. The game state is displayed after each iteration.
        """
        self.display()
        for _ in range(rounds):
            # input("Press enter to continue")
            orientation = random.randint(1, self.current_piece.num_orientations)
            self.current_piece.rotate(orientation - 1)
            position = random.randint(0, self.board.num_columns - self.current_piece.num_cols)
            lines = self.board.place_piece(self.current_piece, position)
            if lines == -1:
                self.display()
                print("Game over!")
                break
            self.score += score_dict[lines]
            self.update_queue()
            self.display()
        
        print("Score after", rounds, "rounds:", self.score)
        return self.score
    
    def display(self):
        """
        Print the current state of the game, including the current piece, queue of pieces to come, 
        height of the board, and the number of holes in the board.
        """
        print("Current piece:", self.current_piece.name, "| Queue:", [piece.name for piece in self.queue])
        print("Height:", self.board.num_rows - self.board.height, "| Holes:", self.board.holes, "| Score:", self.score)
        self.board.display()