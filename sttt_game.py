class sttt_game:
    """A game emulator for super tic tac toe"""

    def __init__(self):
        # saved_board[i][j] = the turn a marking was placed on the square in row i column j
        self.saved_board = [[0] * 9 for _ in range(9)]  # The saved game board for replays
        self.finished = False

        # current state
        self.next_allowed = 0  # the box that the next player can play in (see 'game state')
        self.turn = 1  # the current turn (decides which player is active and what game state is returned)

    def game_state(self):
        """
        'game_state' returns a list containing 2 args:
        - [0] the current game board (9x9 array of ints)
            - 0 = open
            - 1 = taken by the opponent
            - 2 = taken by the current player
        - [1] the allowed space for the next move (int)
            - 0 = the last move was in a complete 3x3 square / the player can play anywhere [0-8, 0-8]
            - 1 = any coordinate within [0-2, 0-2]
            - 2 = any coordinate within [0-2, 3-5]
            - 3 = any coordinate within [0-2, 6-8]
            - 4 = any coordinate within [3-5, 0-2]
            - 5 = any coordinate within [3-5, 3-5]
            - 6 = any coordinate within [3-5, 6-8]
            - 7 = any coordinate within [6-8, 0-2]
            - 8 = any coordinate within [6-8, 3-5]
            - 9 = any coordinate within [6-8, 6-8]
        """
        pass

    def move(self):
        """
        'move' checks that a move is valid, executes if valid, and returns True/False accordingly
        if not valid, one of these error messages will be printed:
        - "Error: Not a move - {bot name} executed move {the move} on turn {the turn}"
            - No proper coordinates were given
        - "Error: Illegal move - {bot name} executed move {the move} on turn {the turn}"
            - A coordinate was given but it did not fit the allowed ranges as specified by game_state
        """
        pass

    def is_finished(self):
        """
        'is_finished' returns a boolean - True if the game is finished, False if not
        """
        return self.finished
