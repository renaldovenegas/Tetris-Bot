from piece import *
import copy

class Board:
    """
    2-D array of booleans (to represent occupied/unoccupied spots on the board). The 0th index row corresponds to the top row on the board,
    and the 0th index column corresponds to the leftmost column on the board.
    """
    def __init__(self, num_rows, num_columns):
        """
        Initialize the game board.
        - rows: Number of rows in the board.
        - columns: Number of columns in the board.
        """
        self.num_rows = num_rows
        self.num_columns = num_columns
        self.grid = [[0 for x in range(num_columns)] for y in range(num_rows)]

        # index of the height: Since index 0 corresponds to the top of the board and index num_rows - 1 corresponds to the bottom of the board
        self.height = num_rows - 1
        # number of holes, i.e. unreachable pixels on the board.
        self.holes = 0

    def __copy__(self):
        return copy.deepcopy(self)
    
    def can_place(self, piece, position): 
        """
        Check if the piece can be placed at the given position. Starts at the top of the board.

        - piece (Piece object): The piece to be placed.
        - position (int): column number where the leftmost column of the piece will be placed.

        Returns True if the piece can be placed. 
        """
        shape = piece.get_shape()
                
        for i, piece_row in enumerate(shape):
            for j, mino in enumerate(piece_row):
                if shape[i][j] == 1 and self.grid[i][position + j]:
                    return False
                
        return True


    def place_piece(self, piece, position):
        """
        Place the piece on the board at the given position and clear completed lines.

        Parameters:
        - piece (Piece): The piece to be placed.
        - position (int): column number where the leftmost column of the piece will be placed.

        Returns the number of lines cleared after placing the piece.
        """
        shape = piece.get_shape()

        if not self.can_place(piece, position):
            for i, piece_row in enumerate(shape):
                for j, mino in enumerate(piece_row):
                    if mino == 1:
                        self.grid[i][position + j] = 1
            return -1

        for i, piece_row in enumerate(shape):
            for j, mino in enumerate(piece_row):
                if mino == 1:
                    self.grid[i][position + j] = 1

        piece_indices = [(i, position + j) for i, piece_row in enumerate(shape) for j, mino in enumerate(piece_row) if mino == 1]

        # Let piece fall until there are no empty lines between piece and existing board
        # valid_board = False
        # while not valid_board:
        #     prev_row_nonempty = False
        #     for i, row in enumerate(self.grid):
        #         if 1 in row and i == self.num_rows - 1:
        #             valid_board = True
        #             break
        #         elif 1 in row:
        #             prev_row_nonempty = True
        #         elif 1 not in row and prev_row_nonempty:
        #             for i, j in piece_indices:
        #                 self.grid[i][j] = False
        #             piece_indices = [(i + 1, j) for (i, j) in piece_indices]
        #             for i, j in piece_indices:
        #                 self.grid[i][j] = True
        #             break
        #         else:
        #             continue
        
        bottom_of_piece = max(mino[0] for mino in piece_indices)
        while bottom_of_piece < self.num_rows - 1:
            done = False
            for (i, j) in piece_indices:
                if ((i + 1, j) not in piece_indices and self.grid[i + 1][j]):
                    done = True

            if done:
                break

            for i, j in piece_indices:
                self.grid[i][j] = 0
            piece_indices = [(i + 1, j) for (i, j) in piece_indices]
            for i, j in piece_indices:
                self.grid[i][j] = 1

            bottom_of_piece += 1


        # Clear completed lines
        cleared = self.clear_lines()

        # Update height
        for i in range(0, self.num_rows):
            if 1 in self.grid[i]:
                self.height = i
                break

        # Re-count the number of holes
        self.holes = 0
        ceiling = self.grid[0]
        for i in range(1, self.num_rows):
            for j in range(self.num_columns):
                if not self.grid[i][j] and ceiling[j]:
                    self.holes += 1
            ceiling = [self.grid[i][k] or ceiling[k] for k in range(self.num_columns)]

        return cleared


    def clear_lines(self):
        """
        Identify rows that are full and remove them from the grid

        Returns the number of rows cleared 
        """
        new_grid = [row for row in self.grid if 0 in row]
        lines_cleared = len(self.grid) - len(new_grid)  # Calculate how many lines were cleared

        # Add empty rows to maintain grid size
        for _ in range(lines_cleared):
            new_grid.insert(0, [0] * self.num_columns)

        #can add check here to make sure grid size is consistent 

        self.grid = new_grid
        return lines_cleared


    def num_cleared_lines(self, piece, position):
        """
        Given a piece and position, returns the number of lines that will be cleared. Does not modify the board.

        Returns the number of rows cleared. If placing the piece results in game over, returns -1.
        """
        temp_board = copy.copy(self)
        res = temp_board.place_piece(piece, position)
        if temp_board.is_game_over():
            res = -1
        return res


    def is_game_over(self):
        """
        Check if the game is over.

        Returns True if any cell in the top row is filled, False otherwise.
        """
        return any(cell != 0 for cell in self.grid[0])


    def display(self):
        """
        Display the current state of the board.
        """
        for row in self.grid:
            print(''.join(['X' if cell else '.' for cell in row]))
        print('\n' + '-' * self.num_columns)