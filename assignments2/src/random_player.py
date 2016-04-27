# -*- coding: utf-8 -*-
__author__ = 'Dan'
__email__ = 'daz040@eng.ucsd.edu'


import random
from assignment2 import Player


class RandomPlayer(Player):
    def move(self, state):
        """Plays a random legal move.

        Args:
            state (State): The current state of the board.

        Returns:
            the next random move (Action)
        """
        actions = state.actions()
        if not actions:
            return None
        return random.choice(actions)