# -*- coding: utf-8 -*-

from collections import deque
from p1_is_complete import is_complete
from p2_is_consistent import is_consistent
from p3_basic_backtracking import *


def inference(csp, variable):
    """Performs an inference procedure for the variable assignment.

    For P6, *you do not need to modify this method.*
    """
    return ac3(csp, csp.constraints[variable].arcs())


def backtracking_search(csp):
    """Entry method for the CSP solver.  This method calls the backtrack method to solve the given CSP.

    If there is a solution, this method returns the successful assignment (a dictionary of variable to value);
    otherwise, it returns None.

    For P6, *you do not need to modify this method.*
    """
    if backtrack(csp):
        return csp.assignment
    else:
        return None


def backtrack(csp):
    """Performs the backtracking search for the given csp.

    If there is a solution, this method returns True; otherwise, it returns False.
    """

    # TODO copy from p3
    solution = is_complete(csp)

    if solution:
        return solution

    nextVar = select_unassigned_variable(csp)

    # solution = False here

    for i in order_domain_values(csp, nextVar):
        if is_consistent(csp, nextVar, i):
            csp.variables.begin_transaction()
            nextVar.assign(i)

            if backtrack(csp):
                return True

            csp.variables.rollback()

    return solution

def ac3(csp, arcs=None):
    """Executes the AC3 or the MAC (p.218 of the textbook) algorithms.

    If the parameter 'arcs' is None, then this method executes AC3 - that is, it will check the arc consistency
    for all arcs in the CSP.  Otherwise, this method starts with only the arcs present in the 'arcs' parameter
    in the queue.

    Note that the current domain of each variable can be retrieved by 'variable.domains'.

    This method returns True if the arc consistency check succeeds, and False otherwise.  Note that this method does not
    return any additional variable assignments (for simplicity)."""

    queue_arcs = deque(arcs if arcs is not None else csp.constraints.arcs())

    # TODO copy from p4
    while queue_arcs:
        var = queue_arcs.popleft()

        rev = False
        cs = csp.constraints[var[0]]

        for i in var[0].domain:
            satisfied = False
            for j in var[1].domain:
                if cs[0].is_satisfied(i,j):
                    satisfied = True

            if not satisfied:
                var[0].domain.remove(i)
                rev = True

        if rev:
            if len(var[0].domain) == 0:
                return False

            for i in csp.constraints[var[0]]:
                if not (i.var2 == var[1]):
                    queue_arcs.append(i.var2, var[0])

    return True