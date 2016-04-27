# -*- coding: utf-8 -*-
__author__ = 'Dan'
__email__ = 'daz040@eng.ucsd.edu'


from assignment2 import Player, Action


class HumanPlayer(Player):
    def move(self, state):
        """Reads the next move from the console.
        The move should be entered as two numbers separated by a space, like '3 3'.

        Args:
            state (State): The current state of the board.

        Returns:
            the next move (Action)
        """
        action = None
        if not state.actions():
            print "No valid move"
            return action

        while not self.is_time_up() and action is None:
            input_index = int(raw_input('%s move? ' % str(self)))
            lo, hi = state.possible_action_range()
            if state.board[input_index] == 0 or not(lo <= input_index < hi):
                print "Invalid input. Enter index in range [%d, %d) with non-zero stones" % (lo, hi)
            else:
                action = Action(state.player_row, input_index)

        return action
