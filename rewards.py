from board import Board
from piece import *
import math

# This file is still in progress

A = 4
B = 4

def reward(board, piece, position):
    """
    Returns the raw reward for dropping the piece at the given position, i.e. the points gained by clearing lines。returns -1 if
    the piece at the given position results in game over.
    """
    if board.is_game_over() or board.num_cleared_lines(piece, position) == -1:
        return -math.inf
    return (board.num_cleared_lines(piece, position) ** 2)

def heursitic_reward(board, piece, position, a, b):
    """
    Returns the heurstic reward for the current state of the board, accounting not only for the points gained from clearing lines
    but also the height of the board, along with if there is a hole or not. 
    Returns -1 if the piece at the given position results in game over. the parameter a controls
    how much the height of the board matters, and b controls how much the number of holes matters. 
    """
    old_grid = board.grid
    if board.is_game_over() or board.num_cleared_lines(piece, position) == -1:
        return -math.inf
    placed = board.place_piece(piece, position)
    height = board.height
    num_rows = board.num_rows
    holes = board.holes
    board.grid = old_grid
    return (a * (height / ((num_rows - 1) ** 2)) + (placed ** 2) - b * holes, holes)

def forward_search(depth, board, piece, queue):
    if depth == 0:
        return reward(board, piece, A)
    best = (0, 0)
    max_reward = 0
    old_grid = board.grid
    for j, orientation in enumerate(piece.orientations):
        width = len(orientation[0])
        for i in range(board.num_columns - width + 1):
            board.place_piece(piece, i)
            recursive_step = forward_search(depth - 1, board, queue[0], queue[1:])
            if recursive_step > max_reward:
                max_reward = recursive_step
                best = (j, i)
            board.grid = old_grid
    return max_reward

def forward_search_with_heurstic_pruning(depth, board, piece, queue):
    best = (0, 0)
    if depth == 1:
        max_reward = 0
        for i in range(piece.num_orientations):
            piece.rotate(1)
            for j in range(board.num_columns - piece.num_cols + 1):
                reward = heursitic_reward(board, piece, j, A, B)[0]
                if reward > max_reward:
                    max_reward = reward
                    best = ((i + 1) % piece.num_orientations, j)
        
        return best, max_reward
    else:
        # write recursive step
        pass