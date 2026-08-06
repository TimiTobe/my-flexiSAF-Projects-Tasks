# code for rock, paper, scissors game starts here.........start
import random

def get_computer_choice(choices):
    """Randomly select a choice for the computer."""
    return random.choice(choices)


def get_user_choice(choices):
    """Prompt the user for a valid choice."""
    while True:
        choice = input(f"Choose one of {', '.join(choices)}: ").strip().lower()
        if choice in choices:
            return choice
        print(f"Invalid choice. Please choose from {', '.join(choices)}.")


def determine_winner(user_choice, computer_choice):
    """Return 'user', 'computer', or 'tie' based on RPS rules."""
    if user_choice == computer_choice:
        return "tie"

    beats = {
        "rock": "scissors",
        "scissors": "paper",
        "paper": "rock",
    }

    if beats[user_choice] == computer_choice:
        return "user"
    else:
        return "computer"


def play_game():
    choices = ["rock", "paper", "scissors"]

    print("=== Rock, Paper, Scissors ===")

    user_choice = get_user_choice(choices)
    computer_choice = get_computer_choice(choices)

    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    result = determine_winner(user_choice, computer_choice)

    if result == "tie":
        print("\nIt's a tie!")
    elif result == "user":
        print("\nYou win!")
    else:
        print("\nComputer wins!")


def main():
    play_game()

    while True:
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again == "y":
            print()
            play_game()
        elif again == "n":
            print("Thanks for playing!")
            break
        else:
            print("Please enter 'y' or 'n'.")


if __name__ == "__main__":
    main()
# code for game ends here................stop