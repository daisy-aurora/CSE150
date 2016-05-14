# -*- coding: utf-8 -*-

from collections import deque


def ac3(csp, arcs=None):
    """Executes the AC3 or the MAC (p.218 of the textbook) algorithms.

    If the parameter 'arcs' is None, then this method executes AC3 - that is, it will check the arc consistency
    for all arcs in the CSP.  Otherwise, this method starts with only the arcs present in the 'arcs' parameter
    in the queue.

    Note that the current domain of each variable can be retrieved by 'variable.domains'.

    This method returns True if the arc consistency check succeeds, and False otherwise."""

    queue_arcs = deque(arcs if arcs is not None else csp.constraints.arcs())

    # TODO implement this
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


def revise(csp, xi, xj):
    # You may additionally want to implement the 'revise' method.
    pass
