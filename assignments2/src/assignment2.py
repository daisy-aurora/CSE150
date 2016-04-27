# -*- coding: utf-8 -*-
"""Contains the Mancala game state, player and actions classes.

These should not be modified!
"""

__author__ = 'Dan'
__email__ = 'daz040@eng.ucsd.edu'

BOTTOM = 0
TOP = 1

class Player(object):
    """The base class for all agents."""

    def _set_row(self, row):
        """sets the color of this player."""
        self.row = row
        return self

    @staticmethod
    def create_players(player_classes):
        """Instantiates Player objects from the given list of Player subclasses."""
        players = [player_class()._set_row(i % 2) for i, player_class in enumerate(player_classes)]

        for i, player in enumerate(players):
            player.next = players[(i + 1) % len(players)]

        return players

    def __int__(self):
        return self.row

    def __hash__(self):
        return self.row

    def __eq__(self, other):
        return self.row == other.row

    def __repr__(self):
        return "%s(%d)" % (self.__class__.__name__, self.row)

    def __str__(self):
        return "%s (%d)" % (self.name, self.row)

    def _do_move(self, state, result_q, signal_q):
        """Internal method. Do not modify."""
        pass

    @property
    def name(self):
        return self.__class__.__name__

    def is_time_up(self):
        """Returns True when the time is up."""
        return False

    def move(self, state):
        """
        Calculates the best move from the given board.
        Each agent should implement this method.
        :param state: The current state of the game
        :return: The action
        """
        raise NotImplementedError('Please implement the move() method')


class Action(object):
    """Represents a pick of stone at a pit index."""

    def __init__(self, row, index):
        self.row = row
        self.index = index

    def __hash__(self):
        return hash((self.row, self.index))

    def __eq__(self, other):
        return self.row == other.row and self.index == other.index

    def __repr__(self):
        return "Action(%d, %s)" % (self.row, repr(self.index))

    def __str__(self):
        return "Player %d played at %s" % (self.row, str(self.index))


class State(object):
    """Represents the board state. The 'board' attribute represents the game
    board in (2M+2) array.

    Pits from index $0$ to $M-1$ are the pits on your side. Pit $M$ is your goal
    pit. Pits from $M+1$ to $2M$ is the opponent's pits. Pit $2M+1$ is the
    opponent's goal pit.
    """

    @classmethod
    def initial(cls, M, N, player=None):
        """Creates the initial state.
        """
        cls.M = M
        cls.N = N
        return cls(None, None, player)

    def __init__(self, board_lst, player_row, player=None):
        """
        Copy constructor.
        """
        self._is_terminal = None
        self.player = player
        if board_lst is None or player_row is None:
            self.player_row = BOTTOM  # who will make the move
            self.board = [State.N]*(2*State.M+2)
            self.board[self.player_goal_idx] = 0
            self.board[self.opponent_goal_idx] = 0
        else:
            self.player_row = player_row
            self.board = board_lst

    def __eq__(self, other):
        """
        Returns whether two State instances represent the same board state.
        """
        return (self.board == other.board and
                self.player_row == other.player_row)

    def ser(self):
        """
        Use for transposition table
        """
        return (self.player_row, )+tuple(self.board)

    def __str__(self, *args, **kwargs):
        return str(self.board)

    def __repr__(self, *args, **kwargs):
        top = str(self.board[State.M + 1:2 * State.M + 1][::-1])
        bot = str(self.board[:State.M])
        ret = ("  %s\n"
               "%d %s %d\n"
               "  %s") % (top, self.board[2 * State.M + 1],
                           " " * len(top), self.board[State.M], bot)
        return ret

    @property
    def player_goal_idx(self):
        if self.player_row == BOTTOM:
            return State.M
        else:
            return 2 * State.M + 1

    @property
    def opponent_goal_idx(self):
        if self.player_row == BOTTOM:
            return 2 * State.M + 1
        else:
            return State.M

    def is_terminal(self):
        """
        Returns whether this state is a terminal state
        """
        if self._is_terminal is None:
            self._is_terminal = True
            for i, v in enumerate(self.board):
                if i not in (self.player_goal_idx, self.opponent_goal_idx):
                    if v != 0:
                        self._is_terminal = False
                        break

        return self._is_terminal

    @property
    def winner_row(self):
        """
        Returns the color of the player who won, or 0 if it was a draw,
        *only if it is a terminal state* (is_terminal() must have been True).
        """
        assert self._is_terminal, "is_terminal() must True to calculate the winner"
        if self.board[self.player_goal_idx] > self.board[self.opponent_goal_idx]:
            return self.player_row
        elif self.board[self.player_goal_idx] < self.board[self.opponent_goal_idx]:
            return self.opponent_row
        else:
            return -1  # draw


    def utility(self, for_player):
        """
        Returns the utility for the given player *if it is a terminal state*
        (is_terminal() must have been True).
        """
        assert self._is_terminal, "is_terminal() must True to calculate the utility value"
        if self.winner_row == -1:
            return 0.0

        return 1.0 if self.winner_row == for_player.row else -1.0

    def is_win(self):
        """
        Calculates whether the last action resulted in this state being a win
        for that player.
        """
        if self._is_terminal:
            return self.board[self.player_goal_idx] > self.board[self.opponent_goal_idx]


    def possible_action_range(self):
        """
        The possible pit index the player can act on
        :return: lo, hi as range
        """
        if self.player_row == BOTTOM:
            return 0, State.M
        else:
            return State.M + 1, 2*State.M + 1

    @property
    def opponent_row(self):
        """
        Get the opponent's row. 0's opponent is 1, and 1's opponent is 0
        :return: the opponent's row
        """
        return self.player_row ^ 1

    def actions(self):
        """
        The legal actions that the player can act
        :return: list[Action]
        """
        ret = []
        for i in xrange(*self.possible_action_range()):
            if self.board[i] > 0:
                ret.append(Action(self.player_row, i))

        return ret

    def result(self, action):
        """
        Return the new state resulting from the given action.
        :param action: Action
        :return: State
        """
        if not action:
            return State(list(self.board), self.opponent_row, self.player.next)

        idx =  action.index

        lo, hi = self.possible_action_range()
        if self.board[idx] == 0 or not(lo <= idx < hi):
            raise ValueError("Illegal action: %s" % repr(action))

        # move
        stones = self.board[idx]
        board = list(self.board)
        board[idx] = 0
        while stones:
            idx = (idx + 1) % len(board)
            if idx != self.opponent_goal_idx:
                stones -= 1
                board[idx] += 1

        # capture
        if board[idx] == 1 and lo <= idx < hi:
            opp_idx = 2*State.M - idx
            if board[opp_idx] > 0:
                board[self.player_goal_idx] += board[idx] + board[opp_idx]
                board[idx] = 0
                board[opp_idx] = 0


        return State(board, self.opponent_row, self.player.next)
