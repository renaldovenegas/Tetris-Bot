from board import Board
from piece import *
from rewards import *
from game import Game
import random

a = 4
depth = 5

if __name__ == "__main__":
    game = Game()
    game.play_random()
    print("done!")