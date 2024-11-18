from board import Board
from piece import *

# This file is still in progress

A = 4

# Reward function
def reward(board, piece, a):
    old_board = board
    if board.is_game_over() or board.num_cleared_lines() == -1:
        return -1
    placed = board.place_piece(piece, 0)
    return a * (board.height / ((board.num_rows - 1) ** 2)) + (placed ** 2)

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