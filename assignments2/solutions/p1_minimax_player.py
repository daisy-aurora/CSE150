# -*- coding: utf-8 -*-
__author__ = 'Dan'
__email__ = 'daz040@eng.ucsd.edu'

from assignment2 import Player, State, Action

class MinimaxPlayer(Player):
    def __init__(self):
        self.cache ={}

    player = None

    def minimax(self, state, moveNum):
        global index
        index = state.M * 2 + 2
        actions = state.actions()

        if state.is_terminal():
            return state.utility(player)
        elif player.row == state.player_row:
            utility = max(state, moveNum, actions)
        else:
            utility = min(state, moveNum, actions)

        return utility

    def max(self, state, moveNum, actions):
        v = -999

        if not(actions):
            nextState = State(state.board, state.opponent_row, state.player)
            v = self.minimax(nextState, moveNum + 1)

        while (actions):
            curAction = actions.pop()
            nextState = state.result(curAction)
            tempV = self.minimax(nextState, moveNum + 1)

            if (v <= tempV):
                v = tempV
                if (moveNum == 1):
                    bestMove(curAction)
                    index = curAction.index
        return v

    def min(self, state, moveNum, actions):
        v = 999

        if not(actions):
            nextState = State(state.board, state.opponent_row, state.player)
            v = self.minimax(nextState, moveNum + 1)

        while (actions):
            curAction = actions.pop(0)
            nextState = state.result(curAction)
            tempV = self.minimax(nextState, moveNum + 1)

            if (v > tempV):
                v = tempV
                if (moveNum == 1):
                    bestMove(curAction)
                    index = curAction.index
        return v

    def bestMove(action):
        global bestAction
        bestAction = action

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
