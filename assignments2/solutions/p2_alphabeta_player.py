# -*- coding: utf-8 -*-
__author__ = 'Dan'
__email__ = 'daz040@eng.ucsd.edu'

from assignment2 import Player, State, Action

class AlphaBetaPlayer(Player):
    def __init__(self):
        self.cache ={}
        self.bestAction = None
    player = None
    
    def alphaBetaSearch(self, state):
        # v <- max-value(state, -infinity, infinity)
        utility = self.maxValue(state, -2, 2)
        
        action = self.cache.get(state.ser())
        self.bestAction = action[0]
        return action[1]

    def maxValue(self, state, alpha, beta):
        #check if there's already an entry in the table.
        action = self.cache.get(state.ser())
        if action is not None:
            return action[1]
        
        # return utility if terminal
        if state.is_terminal():
            return state.utility(player)

        # v <- -inifinity
        utility = -2

        actions = state.actions()
        
        if not(actions):
            #print("hello? amI here?")
            nextState = state.result(None)
            utility = self.minValue(nextState, alpha, beta)
            
        while (actions):
            curAction = actions.pop(0)
            #print(curAction)
            nextState = state.result(curAction)

            temp = self.minValue(nextState, alpha, beta)
            
            # get the max utility
            # v <- max(v, temp)
            if (temp > utility):
                utility = temp
                self.cache[state.ser()] = (curAction, utility)

            # if v >= beta then return v
            if (utility >= beta):
                return utility
            
            # alpha <= max(alpha, utility)
            if (utility > alpha):
                alpha = utility

        #print("utility on last line in maxValue")
        #print(utility)
        return utility

    def minValue(self, state, alpha, beta):
        #check if there's already an entry in the table.
        action = self.cache.get(state.ser())
        if action is not None:
            return action[1]

        # return utility if terminal
        if state.is_terminal():
            return state.utility(player)

        # v <- inifinity
        utility = 2

        actions = state.actions()

        if not(actions):
            #print("inside min value not actions!")
            nextState = state.result(None)
            utility = self.maxValue(nextState, alpha, beta)

        while (actions):
            curAction = actions.pop(0)
            #print(curAction)
            nextState = state.result(curAction)

            temp = self.maxValue(nextState, alpha, beta)
            
            # get the min utility
            # v <- min(v, temp)
            if (temp < utility):
                utility = temp
                #print(state.ser())
                self.cache[state.ser()] = (curAction, utility)

            # if v <= alpha then return v
            if (utility <= alpha):
                #print("inside utility <= alpha in minValue")
                #print(utility)
                return utility

            # beta <= min(beta, utility)
            if (utility < beta):
                beta = utility

        #print("utility on last line in minValue")
        #print(utility)
        return utility

    def move(self, state):
        """Calculates the best move from the given board using the minimax
        algorithm with alpha-beta pruning and transposition table.
        :param state: State, the current state of the board.
        :return: Action, the next move
        """
        
        global player
        player = state.player

        utility = self.alphaBetaSearch(state)
        #print(utility)
        return self.bestAction