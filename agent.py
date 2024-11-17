from board import Board
from piece import *

# This file is still in progress

# Reward function
def reward(board, piece, a):
    old_board = board
    if board.is_game_over() or board.num_cleared_lines() == -1:
        return -1
    placed = board.place_piece(piece, 0)
    return a * (board.height / ((board.num_rows - 1) ** 2)) + (placed ** 2)

def forward_search(depth, board, piece, queue):
    if depth == 0:
        return -1
    best = -1
    # in progress