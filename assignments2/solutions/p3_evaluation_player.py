# -*- coding: utf-8 -*-
__author__ = 'Dan'
__email__ = 'daz040@eng.ucsd.edu'

from assignment2 import Player, State, Action


class EvaluationPlayer(Player):
    def move(self, state):
        """Calculates the best move after 1-step look-ahead with a simple
        evaluation function.
        :param state: State, the current state of the board.
        :return: Action, the next move
        """

        # *You do not need to modify this method.*
        best_value = -1.0

        actions = state.actions()
        if not actions:
            actions = [None]

        best_move = actions[0]
        for action in actions:
            result_state = state.result(action)
            value = self.evaluate(result_state, state.player_row)
            if value > best_value:
                best_value = value
                best_move = action

        # Return the move with the highest evaluation value
        return best_move

    def evaluate(self, state, my_row):
        """
        Evaluates the state for the player with the given row
        """

        # row 0's variables
        zerosGoalNum = state.M
        zerosStonesGoal = 0
        zerosStonesLeft = 0

        # row 1's variables
        onesGoalNum = (2 * state.M) + 1
        onesStonesGoal = 0
        onesStonesLeft = 0

        # initialize stones in row 0 & 1's side
        for i in range (0, zerosGoalNum):
            zerosStonesLeft += state.board[i]

        for i in range (zerosGoalNum + 1, onesGoalNum):
            onesStonesLeft += state.board[i]

        zerosStonesGoal = state.board[zerosGoalNum]
        onesStonesGoal = state.board[onesGoalNum]

        # There's only 2 row: 0 and 1
        if my_row == 0:
            stonesLeft = zerosStonesLeft - onesStonesLeft
            goalScore = zerosStonesGoal - onesStonesGoal

            s = stonesLeft + goalScore

        else: # my_row = 1
            stonesLeft = onesStonesLeft - zerosStonesLeft
            goalScore =  onesStonesGoal - zerosStonesGoal

            s = stonesLeft + goalScore

        # 1/2MN
        denominator = 2 * zerosGoalNum * onesGoalNum
        score = float (s)/denominator

        return score

        #raise NotImplementedError("Need to implement this method")
