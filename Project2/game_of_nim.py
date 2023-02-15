# GROUP: Andrew Hoblit, Ari Imam, Minkyu Park, Ahad Hussain

from games import *

class GameOfNim(Game):
    """Play Game of Nim with first player 'MAX'.
    A state has the player to move, a cached utility, a list of moves in
    the form of a list of (x, y) positions, and a board, in the form of
    a list with number of objects in each row."""
    def __init__(self, board=[3,1]):
        moves = []
        for row, val in enumerate(board):
            for i in range(val):
                moves.append((row, i+1))
        self.initial = GameState(to_move=True, utility=0, board=board, moves=moves)

    def actions(self, state):
        """Legal moves are at least one object, all from the same row."""
        return state.moves

    def result(self, state, move):
        """Returns the result state of a move"""
        if move not in state.moves:
            return state  # Illegal move has no effect
        board = state.board.copy()
        board[move[0]] -= move[1]
        utility = 0
        if board == [0]*len(board):
            if state.to_move:
                utility = 1
            else:
                utility = -1
        moves = []
        for row, val in enumerate(board):
            for i in range(val):
                moves.append((row, i+1))
        return GameState(to_move=not state.to_move, utility=utility, board=board, moves=moves)


    def utility(self, state, player):
        """Return the value to player; 1 for win, -1 for loss, 0 otherwise."""
        test = self.terminal_test(state)
        if not test:
            return 0
        elif player:
            return 1
        else:
            return -1

    def terminal_test(self, state):
        """A state is terminal if there are no objects left"""
        return state.board == [0]*len(state)

    def to_move(self, state):
        """Return the player whose move it is in this state."""
        return state.to_move

    def display(self, state):
        board = state.board
        print("board: ", board)


if __name__ == "__main__":
    nim = GameOfNim(board=[0, 5, 3, 1]) # Creating the game instance
    print(nim.initial)
    #nim = GameOfNim(board=[7, 5, 3, 1]) # a much larger tree to search
    #print(nim.initial.board) # must be [0, 5, 3, 1]
    #print(nim.initial.moves) # must be [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (2,1), (2, 2), (2, 3), (3, 1)]
    #print(nim.result(nim.initial, (1,3) ))

    
    utility = nim.play_game(alpha_beta_player, query_player) # computer moves first
    if (utility < 0):
        print("MIN won the game")
    else:
        print("MAX won the game")
    