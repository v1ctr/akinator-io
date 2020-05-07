import unittest
from variable import Variable
from constraint import Constraint
from predicates import Equals


class ConstraintTestCase(unittest.TestCase):

    def test_evaluate(self):
        constraint = Constraint([[Equals(5)]])
        self.assertTrue(constraint.evaluate(Variable("Variable", 5)))
        self.assertFalse(constraint.evaluate(Variable("Variable", 10)))
