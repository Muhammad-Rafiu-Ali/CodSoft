import random

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # Representing the Tic-Tac-Toe board as a list

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def check_winner(self, board, player):
        # Check rows, columns, and diagonals for a win
        winning_combinations = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
                                [0, 3, 6], [1, 4, 7], [2, 5, 8],
                                [0, 4, 8], [2, 4, 6]]

        for combo in winning_combinations:
            if all(board[i] == player for i in combo):
                return True
        return False

    def check_draw(self):
        return ' ' not in self.board

    def make_move(self, position, player):
        self.board[position] = player

    def minimax(self, board, depth, maximizing_player):
        if self.check_winner(board, 'O'):
            return 1
        elif self.check_winner(board, 'X'):
            return -1
        elif self.check_draw():
            return 0

        if maximizing_player:
            best_score = -float('inf')
            for move in self.available_moves():
                board[move] = 'O'
                score = self.minimax(board, depth+1, False)
                board[move] = ' '
                best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for move in self.available_moves():
                board[move] = 'X'
                score = self.minimax(board, depth+1, True)
                board[move] = ' '
                best_score = min(score, best_score)
            return best_score

    def get_best_move(self):
        best_score = -float('inf')
        best_move = None
        for move in self.available_moves():
            self.board[move] = 'O'
            score = self.minimax(self.board, 0, False)
            self.board[move] = ' '
            if score > best_score:
                best_score = score
                best_move = move
        return best_move

def play_game():
    game = TicTacToe()
    human_player = 'X'
    ai_player = 'O'

    print("Welcome to Tic-Tac-Toe!")
    game.print_board()

    while True:
        if human_player == 'X':
            human_move = int(input("Enter your move (0-8): "))
            game.make_move(human_move, human_player)
            game.print_board()

            if game.check_winner(game.board, human_player):
                print("You win!")
                break
            elif game.check_draw():
                print("It's a draw!")
                break

            ai_move = game.get_best_move()
            game.make_move(ai_move, ai_player)
            print(f"AI plays move {ai_move}")
            game.print_board()

            if game.check_winner(game.board, ai_player):
                print("AI wins!")
                break
            elif game.check_draw():
                print("It's a draw!")
                break
        else:
            ai_move = game.get_best_move()
            game.make_move(ai_move, ai_player)
            print(f"AI plays move {ai_move}")
            game.print_board()

            if game.check_winner(game.board, ai_player):
                print("AI wins!")
                break
            elif game.check_draw():
                print("It's a draw!")
                break

            human_move = int(input("Enter your move (0-8): "))
            game.make_move(human_move, human_player)
            game.print_board()

            if game.check_winner(game.board, human_player):
                print("You win!")
                break
            elif game.check_draw():
                print("It's a draw!")
                break

if __name__ == "__main__":
    play_game()
