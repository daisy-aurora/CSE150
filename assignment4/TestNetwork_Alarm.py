#!/usr/bin/env python

from BayesianNetwork import *
# 
#   * Creates and tests the alarm network as given in the book.
#   
class TestNetwork(object):
    """ generated source for class TestNetwork """
    @classmethod
    def main(cls, args):
        """ generated source for method main """
        alarmnet = BayesianNetwork()
        #  Add variables to network
        burglary = RandomVariable("Burglary")
        earthquake = RandomVariable("Earthquake")
        alarm = RandomVariable("Alarm")
        john = RandomVariable("John")
        mary = RandomVariable("Mary")
        alarmnet.addVariable(burglary)
        alarmnet.addVariable(earthquake)
        alarmnet.addVariable(alarm)
        alarmnet.addVariable(john)
        alarmnet.addVariable(mary)
        #  Add edges to network
        alarmnet.addEdge(burglary, alarm)
        alarmnet.addEdge(earthquake, alarm)
        alarmnet.addEdge(alarm, john)
        alarmnet.addEdge(alarm, mary)
        #  Initialize probability tables
        burglaryProbs = [0.001]
        earthquakeProbs = [0.002]
        alarmProbs = [0.95, 0.94, 0.29, 0.001]
        johnProbs = [0.9, 0.05]
        maryProbs = [0.7, 0.01]
        alarmnet.setProbabilities(burglary, burglaryProbs)
        alarmnet.setProbabilities(earthquake, earthquakeProbs)
        alarmnet.setProbabilities(alarm, alarmProbs)
        alarmnet.setProbabilities(john, johnProbs)
        alarmnet.setProbabilities(mary, maryProbs)

        #  Perform sampling tests
        #  ----------------------
        #  P(J=1|B=0,E=1) = TODO in writeup
        print("Test 1")
        given1 = {}
        given1[burglary]= False
        given1[earthquake]=True
        print("rejection sampling: " +str(alarmnet.performRejectionSampling(john, given1, 999999)))
        print("weighted sampling: " + str(alarmnet.performWeightedSampling(john, given1, 99999)))
        print("gibbs sampling: " + str(alarmnet.performGibbsSampling(john, given1, 99999)))
        #  P(B=1|J=1) = TODO in writeup
        print("Test 2")
        given2 = {}
        given2[john]=True
        print("rejection sampling: " + str(alarmnet.performRejectionSampling(burglary, given2, 999999)))
        print("weighted sampling: " + str(alarmnet.performWeightedSampling(burglary, given2, 99999)))
        print("gibbs sampling: " + str(alarmnet.performGibbsSampling(burglary, given2, 99999)))


if __name__ == '__main__':
    import sys
    TestNetwork.main(sys.argv)
import sys
TestNetwork.main(sys.argv)
