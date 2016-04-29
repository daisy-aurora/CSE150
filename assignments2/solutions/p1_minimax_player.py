# -*- coding: utf-8 -*-
__author__ = 'Dan'
__email__ = 'daz040@eng.ucsd.edu'

from assignment2 import Player, State, Action

class MinimaxPlayer(Player):
    def __init__(self):
        self.cache ={}

    def move(self, state):
        """
        Calculates the best move from the given board using the minimax
        algorithm.
        :param state: State, the current state of the board.
        :return: Action, the next move
        """
        global player
        player = state.player
        utility = self.minimax(state, 1)
        #print utility
        return bestAction

    def minimax(self, state, moveNum):
        global bestAction
        actions = state.actions()
        index = (2 * state.M) + 2

        # return utility if terminal
        if state.is_terminal():
            return state.utility(player)

        # initialize utility
        if player.row == state.player_row: # if max set to - infinity
            maxTurn = True
            utility = -999
        else: # if min set to infinity
            maxTurn = False
            utility = 999

        if not actions:
            nextState = state.result(None)
            utility = self.minimax(nextState, moveNum + 1)

        # while actions != []
        while (actions):
            if maxTurn:
                curAction = actions.pop()
            else:
                curAction = actions.pop(0)

            nextState = state.result(curAction)
            tempV = self.minimax(nextState, moveNum + 1)

            if (maxTurn and utility <= tempV):
                utility = tempV
                if (moveNum == 1):
                    bestAction = curAction
                    index = curAction.index

            if (not maxTurn and utility > tempV):
                utility = tempV
                if (moveNum == 1):
                    bestAction = curAction
                    index = curAction.index

        return utility
