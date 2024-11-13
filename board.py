from piece import Piece

class Board:
    """
    2-D array of booleans (to represent occupied/unoccupied spots on the board)
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

    
    
    def can_place(self, piece, position): 
        """
        Check if the piece can be placed at the given position.

        - piece (Piece object): The piece to be placed.
        - position (tuple): (row, column) where the top-left of the piece will be placed.

        Returns True if the piece can be placed
        """
        top_row, left_col = position
        shape = piece.get_shape()
        num_rows = piece.get_num_rows()
        num_cols = piece.get_num_cols()

        # Check boundaries
        if top_row + num_rows > self.num_rows or left_col + num_cols > self.num_columns:
            return False  

        # Check for collisions with existing blocks
        for i in range(num_rows):
            for j in range(num_cols):
                if shape[i][j] == 1 and self.grid[top_row + i][left_col + j] == 1:  
                    return False

        return True


    def place_piece(self, piece, position):
        """
        Place the piece on the board at the given position and clear completed lines.

        Parameters:
        - piece (Piece): The piece to be placed.
        - position (tuple): (row, column) where the top-left of the piece will be placed.

        Returns the number of lines cleared after placing the piece.
        """
        if not self.can_place(piece, position):
            raise ValueError("Cannot place piece at the given position.")

        top_row, left_col = position
        shape = piece.get_shape()
        num_rows = piece.get_num_rows()
        num_cols = piece.get_num_cols()

        # Update the board
        for i in range(num_rows):
            for j in range(num_cols):
                if shape[i][j] == 1:
                    self.grid[top_row + i][left_col + j] = 1
        
        piece.set_location(top_row, left_col)

        # Clear completed lines
        return self.clear_lines()

    def clear_lines(self):
        """
        Identify rows that are not full and remove them from the grid

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
        print('\n' + '-' * self.columns)