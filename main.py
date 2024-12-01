from game import Game

a = 4
depth = 5

if __name__ == "__main__":
    # If true, game is initialized with only the L, J, I, and O pieces. If not, game is initialized with all 7 pieces.
    simplified = False
    game = Game(simplified)

    # game.play_random()
    game.play_search(depth=5, height_weight=4)