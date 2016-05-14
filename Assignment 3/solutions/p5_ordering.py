# -*- coding: utf-8 -*-
from test.test_support import temp_cwd

def select_unassigned_variable(csp):
    """Selects the next unassigned variable, or None if there is no more unassigned variables
    (i.e. the assignment is complete).

    This method implements the minimum-remaining-values (MRV) and degree heuristic. That is,
    the variable with the smallest number of values left in its available domain.  If MRV ties,
    then it picks the variable that is involved in the largest number of constraints on other
    unassigned variables.
    """

    # TODO implement this
    nextVar = None
    minRemainVal = 9999999
    
    for i in csp.variables:
        if i.is_assigned():
            continue
        
        #tie breaker
        if len(i.domain) == minRemainVal:
            for constraint in csp.constraints:
                #print("inside tie breaker.....")
                curConstraint = 0
                minRemainValConstraint = 0
                #check constraint on the current iteration of csp
                #print(constraint.var1)
                #print(constraint.var2)
                #print(i)
                #print(minRemainVal)
                #print()
                if constraint.var1 == i or constraint.var2 == i:
                    curConstraint += 1
                if constraint.var1 == minRemainVal or constraint.var2 == minRemainVal:
                    minRemainValConstraint += 1
                
            #print(curConstraint)
            #print(minRemainValConstraint)
            
            #current variable constraint got more constraint
            if minRemainValConstraint < curConstraint:
                #print("am I here?")
                minRemainVal = i
        
        if len(i.domain) < minRemainVal:
            #print("updating value here...")
            minRemainVal = len(i.domain)
            nextVar = i
    
    #print(nextVar)
    return nextVar



def order_domain_values(csp, variable):
    """Returns a list of (ordered) domain values for the given variable.

    This method implements the least-constraining-value (LCV) heuristic; that is, the value
    that rules out the fewest choices for the neighboring variables in the constraint graph
    are placed before others.
    """

    # TODO implement this
    neighbor = []
    result = []

    for constraint in csp.constraints:
        if constraint.var1 == variable:
            neighbor.append(constraint.var2)
        if constraint.var2 == variable:
            neighbor.append(constraint.var1)      

    for i in range (0, len(variable.domain)):
        count = 0;
        for v in neighbor:
            if variable.domain[i] in v.domain:
                count += 1;
        #insert to the result table based on the index
        result.insert(i,count);

    sortedResult = []
    #sorted the result list
    for i in range (0,len(variable.domain)):
        temp = max(result)
        #insert the maximum first, put the second max in front of the max
        #etc.. until all the result is inserted
        sortedResult.insert(0, variable.domain[result.index(temp)])
        
        #since the value is already inserted, 
        #put 0 so it won't mess the calculation in the next iteration
        result[result.index(temp)] = 0

    return sortedResult