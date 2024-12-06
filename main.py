from game import Game

if __name__ == "__main__":
    # If true, game is initialized with only the L, J, I, and O pieces. If not, game is initialized with all 7 pieces.
    simplified = False
    game = Game(simplified)

    # game.play_random()
    # game.play_naive(height_weight=16, rounds=100)
    game.play_search(depth=3, height_weight=16, rounds=100, anticipate_I=True)