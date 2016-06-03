#!/usr/bin/env python
""" generated source for module BayesianNetwork """
from Assignment4 import *
import random
#
#  * A bayesian network
#  * @author Panqu
#
class BayesianNetwork(object):
    """ generated source for class BayesianNetwork """
    #
    #     * Mapping of random variables to nodes in the network
    #
    varMap = None

    #
    #     * Edges in this network
    #
    edges = None

    #
    #     * Nodes in the network with no parents
    #
    rootNodes = None

    #
    #     * Default constructor initializes empty network
    #
    def __init__(self):
        """ generated source for method __init__ """
        self.varMap = {}
        self.edges = []
        self.rootNodes = []

    #
    #     * Add a random variable to this network
    #     * @param variable Variable to add
    #
    def addVariable(self, variable):
        """ generated source for method addVariable """
        node = Node(variable)
        self.varMap[variable]=node
        self.rootNodes.append(node)

    #
    #     * Add a new edge between two random variables already in this network
    #     * @param cause Parent/source node
    #     * @param effect Child/destination node
    #
    def addEdge(self, cause, effect):
        """ generated source for method addEdge """
        source = self.varMap.get(cause)
        dest = self.varMap.get(effect)
        self.edges.append(Edge(source, dest))
        source.addChild(dest)
        dest.addParent(source)
        if dest in self.rootNodes:
            self.rootNodes.remove(dest)

    #
    #     * Sets the CPT variable in the bayesian network (probability of
    #     * this variable given its parents)
    #     * @param variable Variable whose CPT we are setting
    #     * @param probabilities List of probabilities P(V=true|P1,P2...), that must be ordered as follows.
    #       Write out the cpt by hand, with each column representing one of the parents (in alphabetical order).
    #       Then assign these parent variables true/false based on the following order: ...tt, ...tf, ...ft, ...ff.
    #       The assignments in the right most column, P(V=true|P1,P2,...), will be the values you should pass in as probabilities here.
    #
    def setProbabilities(self, variable, probabilities):
        """ generated source for method setProbabilities """
        probList = []
        for probability in probabilities:
            probList.append(probability)
        self.varMap.get(variable).setProbabilities(probList)

    #
    # helper function to perform prior sampling
    # a sampling algorithm that generates events from a Bayesian network. Each variable is sampled
    # according to the conditional distribution given the values already sampled for the variable's
    # parents.
    #
    def priorSample(self):
        # see page 531
        x = {}
        

        # foreach variable x[i] is a random sample from P(Xi | parents(Xi))
        for node in sorted(self.varMap):
            y = random.random()
            if y <= self.varMap.get(node).getProbability(x, True):
                x[node.getName()] = True
            else:
                x[node.getName()] = False
        return x

    def Normalize(self, input):
        sum = 0
        for x in input:
            sum += x
            
        if sum == 0:
            return 0,0
        else:
            return float(input[0])/sum
    #
    #     * Returns an estimate of P(queryVal=true|givenVars) using rejection sampling
    #     * @param queryVar Query variable in probability query
    #     * @param givenVars A list of assignments to variables that represent our given evidence variables
    #     * @param numSamples Number of rejection samples to perform
    #
    def performRejectionSampling(self, queryVar, givenVars, numSamples):
        """ generated source for method performRejectionSampling """
        #  TODO
        #return 0
        # see page 533
        query1 = 0
        query2 = 0
        for i in range (1, numSamples):
            x = self.priorSample()

            for j in givenVars:
                if x[j.getName()] == givenVars[j]:
                    if x[queryVar.getName()]:
                        query1 = query1 + 1
                    else:
                        query2 = query2 + 1

        return self.Normalize([query1, query2])

    #
    # helper function to perform weighted sampling that returns an event and a weighted
    #
    def weightedSample(self, givenVars):
        #see page 534
        w = 1
        x = {}
        #for y in givenVars:
        for node in sorted(self.varMap):
            if givenVars.get(self.varMap.get(node).getVariable()) is not None:
                w = w * self.varMap.get(node).getProbability(x, True)#P(Xi = xi | parents(Xi))
                x[node.getName()] = self.varMap.get(node).getProbability(x, True)
            else:
                #x[i] = random asmple from P(Xi | parents(Xi))
                z = random.randint(0,1)
                if z <= 0.5:
                    x[node.getName()] = True
                else:
                    x[node.getName()] = False
        return x,w

    #
    #     * Returns an estimate of P(queryVal=true|givenVars) using weighted sampling
    #     * @param queryVar Query variable in probability query
    #     * @param givenVars A list of assignments to variables that represent our given evidence variables
    #     * @param numSamples Number of weighted samples to perform
    #
    def performWeightedSampling(self, queryVar, givenVars, numSamples):
        """ generated source for method performWeightedSampling """
        #  TODO
        #return 0
        # see page 534
        query1 = 0
        query2 = 0
        for i in range (1, numSamples):
            x,w = self.weightedSample(givenVars)

            for j in givenVars:
                if x[j.getName()] == givenVars[j]:
                    if x[queryVar.getName()]:
                        query1 = query1 + w
                    else:
                        query2 = query2 + w

        return self.Normalize([query1, query2])
#         count = [0] * sizeof(queryVar)
#         for i = 1 to numSamples:
#             x,w = weightedSample(self, givenVars)
#  
#             for j in queryVar:
#                 count[j] = count[j] + w
#  
#         return Normalize(count)

    #
    #     * Returns an estimate of P(queryVal=true|givenVars) using Gibbs sampling
    #     * @param queryVar Query variable in probability query
    #     * @param givenVars A list of assignments to variables that represent our given evidence variables
    #     * @param numTrials Number of Gibbs trials to perform, where a single trial consists of assignments to ALL
    #       non-evidence variables (ie. not a single state change, but a state change of all non-evidence variables)
    #
    def performGibbsSampling(self, queryVar, givenVars, numTrials):
        """ generated source for method performGibbsSampling """
        #  TODO
        return 0
        # see page 537
#         count = [0] * sizeof(queryVar)
#         Z = self.rootNodes
# 
#         for i = 1 to numSamples:
#             for z in Z:
#                 #set the value of z in x by sampling from P(z|mb(z))
#                 # x is the current state of the network, initially copied from givenVars
#                 z =
# 
#                 for j in queryVar:
#                     count[j] = count[j] + 1
# 
#         return Normalize(count)
