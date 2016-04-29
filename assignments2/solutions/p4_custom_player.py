# -*- coding: utf-8 -*-

__author__ = 'Dan'
__email__ = 'daz040@eng.ucsd.edu'

from assignment2 import Player


class CustomPlayer(Player):
    """The custom player implementation.
    """

    def __init__(self):
        """Called when the Player object is initialized. You can use this to
        store any persistent data you want to store for the  game.

        For technical people: make sure the objects are picklable. Otherwise
        it won't work under time limit.
        """
        self.cache ={}
        self.bestAction = None
        #pass

    depthLimit = 0
    done = False
    
    def deepeningAlphaBetaSearch(self, state):
        global done
        global depthLimit
        
        bestV = -2
        bestAct = None
        for d in range(1, depthLimit):
            actions = state.actions()
            
            for action in actions:
                # v <- max-value(state, -infinity, infinity)
                utility = self.maxValue(state, -2, 2, d)
                if utility > bestV:
                    bestV = utility
                    bestAct = action
        
        action = self.cache.get(state.ser())
        if action is not None:
            self.bestAction = action[0]
            return action[1]
        else:
            return bestAct

    def maxValue(self, state, alpha, beta, depth):   
        global depthLimit    
        #check if there's already an entry in the table.
        action = self.cache.get(state.ser())
        if action is not None:
            return action[1]
            
        # return utility if terminal
        if state.is_terminal():
            self.cache[state.ser()] = (action, self)
            return state.utility(player)
        
        #use evaluate if time is up or limit depth reached
        if self.is_time_up == True or depth >= depthLimit:
            return self.evaluate(state, state.player_row)
        
        # v <- -inifinity
        utility = -2

        actions = state.actions()
        
        if not actions:
            #print("hello? amI here?")
            nextState = state.result(None)
            utility = self.minValue(nextState, alpha, beta, depth + 1)
            
        for action in actions:
            nextState = state.result(action)

            temp = self.minValue(nextState, alpha, beta, depth + 1)
            
            # get the max utility
            # v <- max(v, temp)
            if (temp > utility):
                utility = temp
                self.cache[state.ser()] = (action, utility)

            # if v >= beta then return v
            if (utility >= beta):
                return utility
            
            # alpha <= max(alpha, utility)
            if (utility > alpha):
                alpha = utility

        #print("utility on last line in maxValue")
        #print(utility)
        return utility

    def minValue(self, state, alpha, beta, depth):
        global depthLimit
        #check if there's already an entry in the table.
        action = self.cache.get(state.ser())
        if action is not None:
            return action[1]

        # return utility if terminal
        if state.is_terminal():
            self.cache[state.ser()] = (action, self)
            return state.utility(player)

        #use evaluate if time is up or limit depth reached
        if self.is_time_up == True or depth >= depthLimit:
            return self.evaluate(state, state.player_row)
                
        # v <- inifinity
        utility = 2

        actions = state.actions()

        if not actions:
            #print("inside min value not actions!")
            nextState = state.result(None)
            utility = self.maxValue(nextState, alpha, beta, depth + 1)

        for action in actions:
            nextState = state.result(action)

            temp = self.maxValue(nextState, alpha, beta, depth + 1)
            
            # get the min utility
            # v <- min(v, temp)
            if (temp < utility):
                utility = temp
                #print(state.ser())
                self.cache[state.ser()] = (action, utility)

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

    def move(self, state):
        """
        You're free to implement the move(self, state) however you want. Be
        run time efficient and innovative.
        :param state: State, the current state of the board.
        :return: Action, the next move
        """
        
        global player
        player = state.player
        
        global depthLimit
        depthLimit = 7

        utility = self.deepeningAlphaBetaSearch(state)
        #print(utility)
        return self.bestAction

