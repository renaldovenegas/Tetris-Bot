from board import Board
from piece import *
import math
import copy


# def reward(board, piece, position):
#     """
#     Returns the raw reward for dropping the piece at the given position, i.e. the points gained by clearing lines。returns -1 if
#     the piece at the given position results in game over.
#     """
#     if board.is_game_over() or board.num_cleared_lines(piece, position) == -1:
#         return -math.inf
#     return (board.num_cleared_lines(piece, position) ** 2)

def heursitic_reward(board, piece, position, a):
    """
    Returns the heurstic reward for the current state of the board given we drop the given piece at the given position, 
    accounting not only for the points gained from clearing lines
    but also the height of the board, along with if there is a hole or not. 
    Returns -1 if the piece at the given position results in game over. the parameter a controls
    how much the height of the board matters. 
    """
    temp_board = copy.copy(board)
    if board.is_game_over() or board.num_cleared_lines(piece, position) == -1:
        return -1
    placed = temp_board.place_piece(piece, position)
    height = temp_board.height
    num_rows = temp_board.num_rows
    holes = temp_board.holes
    # temp_board.display()
    # print(piece.name, "placed at", position)
    return (a * (height / ((num_rows - 1) ** 2)) + (placed ** 2), holes)

# def forward_search(depth, board, piece, queue):
#     if depth == 0:
#         return reward(board, piece, A)
#     best = (0, 0)
#     max_reward = 0
#     old_grid = board.grid
#     for j, orientation in enumerate(piece.orientations):
#         width = len(orientation[0])
#         for i in range(board.num_columns - width + 1):
#             board.place_piece(piece, i)
#             recursive_step = forward_search(depth - 1, board, queue[0], queue[1:])
#             if recursive_step > max_reward:
#                 max_reward = recursive_step
#                 best = (j, i)
#             board.grid = old_grid
#     return max_reward

def forward_search_with_heurstic_pruning(depth, board, piece, queue, height_weight):
    """
    Recursively search all the possible moves of the current piece and all the pieces in the queue, 
    and return the best move and the corresponding best reward. The search is done with heurstic pruning, 
    i.e. if the current move results in a hole, then the search will stop and return the best reward found so far. 
    The heurstic used is a * (height of the board / ((number of rows - 1) ** 2)) + (number of lines cleared ** 2). 
    """
    best = (0, 0)
    max_reward = 0
    old_holes = board.holes

    # Base case
    if depth == 1:
        for i in range(piece.num_orientations):
            piece.rotate(1)
            for j in range(board.num_columns - piece.num_cols + 1):
                reward = heursitic_reward(board, piece, j, height_weight)

                # Checks if the piece at the given position results in game over
                if reward == -1:
                    break
                holes = reward[1]
                reward = reward[0]

                if holes - old_holes > 0:
                    continue

                if reward > max_reward:
                    max_reward = reward
                    best = ((i + 1) % piece.num_orientations, j)

        return best, max_reward
    else:
        for i in range(piece.num_orientations):
            piece.rotate(1)
            for j in range(board.num_columns - piece.num_cols + 1):
                reward = heursitic_reward(board, piece, j, height_weight)
                if reward == -1:
                    break
                holes = reward[1]
                reward = reward[0]

                if holes - old_holes > 0:
                    continue

                temp_board = copy.copy(board)
                temp_board.place_piece(piece, j)

                _, recursive_reward = forward_search_with_heurstic_pruning(depth - 1, temp_board, queue[0], queue[1:], height_weight)
                if reward + recursive_reward > max_reward:
                    max_reward = reward + recursive_reward
                    best = ((i + 1) % piece.num_orientations, j)
                
        return best, max_reward