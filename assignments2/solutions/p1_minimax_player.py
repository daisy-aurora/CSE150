# -*- coding: utf-8 -*-
__author__ = 'Dan'
__email__ = 'daz040@eng.ucsd.edu'

from assignment2 import Player, State, Action

class MinimaxPlayer(Player):
    def __init__(self):
        self.cache ={}

    #player = None

    def minimax(self, state, moveNum):
        global bestAction
        index = state.M * 2 + 2
        actions = state.actions()

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

        if not(actions):
            nextState = State(state.board, state.opponent_row, state.player)
            utility = self.minimax(nextState, moveNum + 1)

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

            elif utility > tempV:
                utility = tempV
                if (moveNum == 1):
                    bestAction = curAction
                    index = curAction.index

        return utility

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

        return bestAction
