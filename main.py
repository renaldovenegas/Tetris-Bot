from game import Game
import statistics

if __name__ == "__main__":
    # # If true, game is initialized with only the L, J, I, and O pieces. If not, game is initialized with all 7 pieces.
    # simplified = False
  
    # Number of runs per game version
    num_runs = 100
    rounds = 100
    height_weight = 16
    depth = 3

    # Lists to hold scores from multiple runs
    random_scores = []
    naive_scores = []
    search_scores = []
    search_I_scores = []

    # Run the random version
    for i in range(num_runs):
        game = Game(simplified=False)
        score = game.play_random(rounds=rounds)
        random_scores.append(score)

    # Run the naive version
    for i in range(num_runs):
        game = Game(simplified=False)
        score = game.play_naive(height_weight=height_weight, rounds=rounds)
        naive_scores.append(score)

    # Run the search version
    for i in range(num_runs):
        game = Game(simplified=False)
        score = game.play_search(depth=depth, height_weight=height_weight, rounds=rounds, anticipate_I=False)
        search_scores.append(score)

       # Run the search version
    for i in range(num_runs):
        game = Game(simplified=False)
        score = game.play_search(depth=depth, height_weight=height_weight, rounds=rounds, anticipate_I=True)
        search_I_scores.append(score)

    # Compute averages
    avg_random = statistics.mean(random_scores)
    avg_naive = statistics.mean(naive_scores)
    avg_search = statistics.mean(search_scores)
    avg_search_I = statistics.mean(search_I_scores)



    # # Print out the results
    print(f"Average score (Random): {avg_random}")
    print(f"Average score (Naive): {avg_naive}")
    print(f"Average score (Search): {avg_search}")

    # Save results to a file
    with open("foward_search_noI_results_log.txt", "w") as f:
        f.write("Individual scores:\n")
        f.write("Random:\n")
        f.write(", ".join(map(str, random_scores)) + "\n")
        f.write("Naive:\n")
        f.write(", ".join(map(str, naive_scores)) + "\n")
        f.write("Search:\n")
        f.write(", ".join(map(str, search_scores)) + "\n\n")
        f.write("Search Anticipate I:\n")
        f.write(", ".join(map(str, search_I_scores)) + "\n\n")

        f.write("Averages:\n")
        f.write(f"Average score (Random): {avg_random}\n")
        f.write(f"Average score (Naive): {avg_naive}\n")
        f.write(f"Average score (Search): {avg_search}\n")
        f.write(f"Average score (Search, Anticipate I): {avg_search_I}\n")

