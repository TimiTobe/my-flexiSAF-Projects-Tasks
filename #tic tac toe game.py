#tic tac toe game
"""
Tic-Tac-Toe with a simple learning AI agent.

The AI uses Q-learning: it plays many games against a random opponent
(training phase), updating a table of state-action values (Q-values)
based on wins, losses, and ties. After training, you can play against it
and it will use what it learned (while still exploring/improving a bit).

Run: python tictactoe_ai.py
"""

import random
import pickle
import os

# ---------------------------------------------------------------------
# 1. Define the game board
# ---------------------------------------------------------------------
EMPTY = " "
PLAYER_X = "X"   # Human (or Agent A during training)
PLAYER_O = "O"   # AI agent (or Agent B during training)

def create_board():
    """Return a fresh, empty 3x3 board as a list of 9 cells."""
    return [EMPTY] * 9


def print_board(board):
    """Pretty-print the board to the console."""
    rows = []
    for r in range(3):
        cells = board[r * 3:(r + 1) * 3]
        rows.append(" | ".join(cells))
    print("\n---------\n".join(rows))
    print()


def available_moves(board):
    """Return list of indices (0-8) that are still empty."""
    return [i for i, cell in enumerate(board) if cell == EMPTY]


# ---------------------------------------------------------------------
# 2. Check if a player has won
# ---------------------------------------------------------------------
WIN_LINES = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),   # rows
    (0, 3, 6), (1, 4, 7), (2, 5, 8),   # columns
    (0, 4, 8), (2, 4, 6),              # diagonals
]

def check_winner(board, player):
    """Return True if `player` has three in a row on `board`."""
    return any(
        board[a] == board[b] == board[c] == player
        for a, b, c in WIN_LINES
    )


# ---------------------------------------------------------------------
# 3. Check if the game is a tie
# ---------------------------------------------------------------------
def check_tie(board):
    """Return True if the board is full and nobody has won."""
    full = EMPTY not in board
    return full and not check_winner(board, PLAYER_X) and not check_winner(board, PLAYER_O)


def game_over(board):
    """Return True if X won, O won, or it's a tie."""
    return check_winner(board, PLAYER_X) or check_winner(board, PLAYER_O) or check_tie(board)


# ---------------------------------------------------------------------
# The learning AI agent (Q-learning)
# ---------------------------------------------------------------------
class QLearningAgent:
    """
    A simple Q-learning agent for tic-tac-toe.

    State  = tuple representation of the board
    Action = index (0-8) of the cell to play
    Q[(state, action)] = expected value of taking that action in that state
    """

    def __init__(self, player_symbol, alpha=0.3, gamma=0.9, epsilon=0.2):
        self.player = player_symbol
        self.alpha = alpha      # learning rate
        self.gamma = gamma      # discount factor
        self.epsilon = epsilon  # exploration rate
        self.q_table = {}       # {(state, action): value}
        self.history = []       # (state, action) pairs from the current game

    def _state(self, board):
        return tuple(board)

    def choose_action(self, board, training=True):
        state = self._state(board)
        moves = available_moves(board)

        # Explore: pick a random move
        if training and random.random() < self.epsilon:
            action = random.choice(moves)
        else:
            # Exploit: pick the move with the highest known Q-value
            q_values = [self.q_table.get((state, m), 0.0) for m in moves]
            max_q = max(q_values)
            best_moves = [m for m, q in zip(moves, q_values) if q == max_q]
            action = random.choice(best_moves)

        if training:
            self.history.append((state, action))
        return action

    def learn(self, reward):
        """
        Propagate the final game reward backward through the moves
        the agent made this game, discounting as we go.
        """
        next_max = 0.0
        for state, action in reversed(self.history):
            old_q = self.q_table.get((state, action), 0.0)
            new_q = old_q + self.alpha * (reward + self.gamma * next_max - old_q)
            self.q_table[(state, action)] = new_q
            next_max = new_q
        self.history = []

    def save(self, path="qtable.pkl"):
        with open(path, "wb") as f:
            pickle.dump(self.q_table, f)

    def load(self, path="qtable.pkl"):
        if os.path.exists(path):
            with open(path, "rb") as f:
                self.q_table = pickle.load(f)
            return True
        return False


# ---------------------------------------------------------------------
# Training: let the agent play against a random opponent many times
# ---------------------------------------------------------------------
def train_agent(agent, episodes=20000):
    print(f"Training AI agent for {episodes} games...")
    for i in range(episodes):
        board = create_board()
        current = PLAYER_X  # random opponent always starts, for variety

        while True:
            if current == agent.player:
                move = agent.choose_action(board, training=True)
            else:
                move = random.choice(available_moves(board))

            board[move] = current

            if check_winner(board, agent.player):
                agent.learn(1.0)      # agent won
                break
            elif check_winner(board, opponent(agent.player)):
                agent.learn(-1.0)     # agent lost
                break
            elif check_tie(board):
                agent.learn(0.5)      # small reward for a draw
                break

            current = opponent(current)

        if (i + 1) % 5000 == 0:
            print(f"  ...{i + 1}/{episodes} games played")

    print("Training complete!\n")


def opponent(player):
    return PLAYER_O if player == PLAYER_X else PLAYER_X


# ---------------------------------------------------------------------
# 4. Main game loop (human vs. trained AI agent)
# ---------------------------------------------------------------------
def get_human_move(board):
    while True:
        try:
            raw = input("Your move (1-9, left to right, top to bottom): ")
            move = int(raw) - 1
            if move in available_moves(board):
                return move
            print("That cell is taken or out of range. Try again.")
        except ValueError:
            print("Please enter a number from 1 to 9.")


def main():
    print("=" * 40)
    print("  TIC-TAC-TOE vs. a Self-Taught AI")
    print("=" * 40)

    agent = QLearningAgent(player_symbol=PLAYER_O, epsilon=0.2)

    # Train (or load a previously trained table, if present)
    if not agent.load("qtable.pkl"):
        train_agent(agent, episodes=20000)
        agent.save("qtable.pkl")
    else:
        print("Loaded a previously trained AI. (Delete qtable.pkl to retrain.)\n")

    play_again = "y"
    while play_again.lower().startswith("y"):
        board = create_board()
        current = PLAYER_X  # human goes first
        print("\nYou are X. The AI is O. Positions are numbered 1-9:")
        print(" 1 | 2 | 3\n---------\n 4 | 5 | 6\n---------\n 7 | 8 | 9\n")

        while True:
            print_board(board)

            if current == PLAYER_X:
                move = get_human_move(board)
            else:
                print("AI is thinking...")
                move = agent.choose_action(board, training=False)

            board[move] = current

            if check_winner(board, current):
                print_board(board)
                if current == PLAYER_X:
                    print("You win! 🎉")
                else:
                    print("The AI wins! 🤖")
                break
            elif check_tie(board):
                print_board(board)
                print("It's a tie!")
                break

            current = opponent(current)

        play_again = input("Play again? (y/n): ")

    print("Thanks for playing!")


# ---------------------------------------------------------------------
# Call the main game loop
# ---------------------------------------------------------------------
if __name__ == "__main__":
    main()