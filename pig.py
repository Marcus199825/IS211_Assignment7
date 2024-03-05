import random

def roll_dice():
    return random.randint(1, 6)

def play_pig():
    scores = [0, 0]
    current_player = 0

    while all(score < 100 for score in scores):
        print(f"Player {current_player + 1}'s turn:")
        turn_score = 0
        while True:
            roll = roll_dice()
            print(f"Roll: {roll}")
            if roll == 1:
                print("You rolled a 1. Turn over. You scored nothing this turn.")
                break
            else:
                turn_score += roll
                print(f"Turn total: {turn_score}")
                choice = input("Roll again (r) or hold (h)? ")
                if choice.lower() == 'h':
                    scores[current_player] += turn_score
                    print(f"Score for this turn: {turn_score}")
                    print(f"Total score for Player {current_player + 1}: {scores[current_player]}")
                    break
        current_player = (current_player + 1) % 2

    print(f"Player {scores.index(max(scores)) + 1} wins with a score of {max(scores)}!")

if __name__ == "__main__":
    play_pig()
    pass
    
