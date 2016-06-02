"""Contains all classes used in PA4: Bayesian Networks
"""

__author__ = 'Panqu'
__email__ = 'pawang@ucsd.edu'

#
#   * Represents the CPT for a node in the bayesian network. The table is stored
#   * as a tree structure.
#
class CPT(object):
    """ generated source for class CPT """
    #
    #     * Represents the parent variable that is the root of this current CPT subtable. This is null if we are at a leaf node.
    #
    parentVariable = None

    #
    #     * Represents the subtable if parentVariable is set to true
    #
    trueTable = None

    #
    #     * Represents the subtable if parentVariable is set to false
    #
    falseTable = None

    probability = None

    #
    #     * Returns the probability that the variable is equal to value given the
    #     * assignments of variables in the 'assignments' map
    #     * @param assignments A mapping from variables to assignments, representing the given variables
    #     * @param value The value to assign to the CPT variable
    #     * @return The probability in the CPT representing the given assignments
    #
    def getProbability(self, assignments, value):
        """ generated source for method getProbability """
        if self.parentVariable == None:
            return float(self.probability) if (value == True) else 1 - float(self.probability)
        currentVal = assignments.get(self.parentVariable.getName())
        if self.trueTable != None:
            if currentVal == True:
                return self.trueTable.getProbability(assignments, value)
            else:
                return self.falseTable.getProbability(assignments, value)
        else:
            return float(self.probability) if (currentVal == True) else float(1 - self.probability)

    #
    #     * Initialize the CPT with the list of probabilities
    #     * @param vars List of random variables that are the parents of the CPT node
    #     * @param probabilities List of probabilities P(V=true|P1,P2...), that must be ordered as follows.
    #       Write out the cpt by hand, with each column representing one of the parents (in order corresponding to variables in vars).
    #       Then assign these parent variables true/false based on the following order: ...tt, ...tf, ...ft, ...ff.
    #       The assignments in the right most column, P(V=true|P1,P2,...), will be the values you should pass in as probabilities here.
    #
    def __init__(self, vars, probabilities):
        """ generated source for method __init__ """
        if len(vars) > 0:
            self.parentVariable = vars[0]
            self.trueTable = CPT(vars[1:len(vars)], probabilities[0:len(probabilities) / 2])
            self.falseTable = CPT(vars[1:len(vars)], probabilities[len(probabilities) / 2 : len(probabilities)])
            self.probability = None
        else:
            self.probability = probabilities[0]

#  * A random variable
class RandomVariable(object):
    """ generated source for class RandomVariable """
    #
    #     * Variable name
    #
    name = None

    #
    #     * Construct random variable
    #     * @param name Variable name
    #
    def __init__(self, name):
        """ generated source for method __init__ """
        super(RandomVariable, self).__init__()
        self.name = name

    #
    #     * Get variable name
    #
    def getName(self):
        """ generated source for method getName """
        return self.name

    def equals(self, other):
        """ generated source for method equals """
        return self.name == other.name


#
#  * This represents an assignment of variables in a bayesian network.
#  * You may want to use something like this for your various sampling implementations.
#
class Sample(object):
    """ generated source for class Sample """
    #
    #     * Weight used for weighted sampling
    #
    weight = float()

    #
    #     * Map containing random variable assignments for this sample
    #
    assignments = None

    #
    #     * Default constructor initializes empty sample with weight 1
    #
    def __init__(self):
        """ generated source for method __init__ """
        self.weight = 1
        self.assignments = {}

    #
    #     * Set a variable assignment for this sample
    #     * @param variable The variable to assign
    #     * @param value The value to assign to variable
    #
    def setAssignment(self, variable, value):
        """ generated source for method setAssignment """
        self.assignments[variable]=value

    #
    #     * Get value assigned to variable variable in this sample
    #     * @param variable The variable to check
    #     * @return The value assigned to variable in this sample
    #
    def getValue(self, variable):
        """ generated source for method getValue """
        return self.assignments.get(variable)

    #
    #     * Get weight of this sample, for weighted sampling
    #     * @return The weight of this sample
    #
    def getWeight(self):
        """ generated source for method getWeight """
        return self.weight

    #
    #     * Set weight of this sample, for weighted sampling
    #
    def setWeight(self, weight):
        """ generated source for method setWeight """
        self.weight = weight


#
#   * A directed edge in the bayesian network
#
class Edge(object):
    """ generated source for class Edge """
    #
    #   * Source of directed edge
    #
    source = None

    #
    #   * Destination of directed edge
    #
    dest = None

    #
    #   * Create an edge from source node to dest node
    #   * @param source Source node
    #   * @param dest Destination node
    #
    def __init__(self, source, dest):
        """ generated source for method __init__ """
        self.source = source
        self.dest = dest


#
#   * Represents a node in a bayesian network
#   * @author baduncan
#
class Node(object):
    """ generated source for class Node """
    #
    #     * The variable stored in this node
    #
    variable = None

    #
    #     * The parent nodes
    #
    parents = None

    #
    #     * The child nodes
    #
    children = None

    #
    #     * Probability table for this variable given its parents
    #
    cpt = None

    #
    #     * Default constructor initializes node to hold variable
    #
    def __init__(self, variable):
        """ generated source for method __init__ """
        self.variable = variable
        self.parents = []
        self.children = []

    #
    #     * Get the random variable in this node
    #     * @return The random variable
    #
    def getVariable(self):
        """ generated source for method getVariable """
        return self.variable

    #
    #     * Add a child node in the bayesian network
    #     * @param child Child node
    #
    def addChild(self, child):
        """ generated source for method addChild """
        self.children.append(child)

    #
    #     * Add a parent node in the bayesian network
    #     * @param parent Parent node
    #
    def addParent(self, parent):
        """ generated source for method addParent """
        self.parents.append(parent)

    #
    #     * Get the child nodes
    #     * @return A vector of child nodes
    #
    def getChildren(self):
        """ generated source for method getChildren """
        return self.children

    #
    #     * Get the parent nodes
    #     * @return A vector of parent nodes
    #
    def getParents(self):
        """ generated source for method getParents """
        return self.parents

    #
    #     * Returns the probability that this variable is equal to value given the
    #     * assignments of variables in the 'assignments' map
    #     * @param assignments A mapping from variables to assignments, representing the given variables
    #     * @param value The value to assign to the variable in this node
    #     * @return The probability that this random variable is equal to value given assignments
    #
    def getProbability(self, assignments, value):
        """ generated source for method getProbability """
        return self.cpt.getProbability(assignments, value)

    #
    #     * Sets the CPT of this variable in the bayesian network (probability of
    #     * this variable given its parents)
    #     * @param probabilities List of probabilities P(V=true|P1,P2...), that must be ordered as follows.
    #        Write out the cpt by hand, with each column representing one of the parents (in alphabetical order).
    #        Then assign these parent variables true/false based on the following order: ...tt, ...tf, ...ft, ...ff.
    #        The assignments in the right most column, P(V=true|P1,P2,...), will be the values you should pass in as probabilities here.
    #
    def setProbabilities(self, probabilities):
        """ generated source for method setProbabilities """
        vars = []
        for node in self.parents:
            vars.append(node.variable)
        sorted(vars)
        self.cpt = CPT(vars, probabilities)


