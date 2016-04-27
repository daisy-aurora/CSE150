# -*- coding: utf-8 -*-

__author__ = 'Dan'
__email__ = 'daz040@eng.ucsd.edu'

from assignment2 import Player


class PleasePleaseChangeThisToSomethingSomethingPlayer(Player):
    """The custom player implementation.
    """

    def __init__(self):
        """Called when the Player object is initialized. You can use this to
        store any persistent data you want to store for the  game.

        For technical people: make sure the objects are picklable. Otherwise
        it won't work under time limit.
        """
        pass

    def move(self, state):
        """
        You're free to implement the move(self, state) however you want. Be
        run time efficient and innovative.
        :param state: State, the current state of the board.
        :return: Action, the next move
        """
        raise NotImplementedError("Need to implement this method")

