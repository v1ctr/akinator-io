"""
Constraint Module
"""
from typing import List
import predicates


class Constraint:
    """
    Constraint Class
    Contains predicates.
    Predicates are stored in a 2D list and interpreted as follows:
    Equals(0) or (MoreThan(4) and LessThan(7))
    _predicates = [[Eqals(0)],[MoreThan(4), LessThan(7)]]
    """

    _predicates: List[List[predicates.Predicate]]

    def __init__(self, predicates: List[List[predicates.Predicate]]):
        self._predicates = predicates

    def __str__(self):
        return "({})".\
            format(" or ".join("({})".format(" and ".join(str(and_clause) for and_clause in or_clause)) for or_clause in self._predicates))

    def evaluate(self, operand):
        evaluation = False
        for or_clause in self._predicates:
            and_evaluation = True
            for and_clause in or_clause:
                and_evaluation = and_evaluation and and_clause.evaluate(operand.get_value())
            evaluation = evaluation or and_evaluation
        return evaluation
