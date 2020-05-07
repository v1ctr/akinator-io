import unittest
from goal import Goal
from variable import Variable
from constraint import Constraint
from predicates import Equals


class GoalTestCase(unittest.TestCase):

    def test_is_valid(self):
        goal = Goal("New Goal")
        self.assertTrue(goal.is_valid())

        goal.add_neighbor(Variable("New Variable"), Constraint([]))
        self.assertFalse(goal.is_valid())

        goal = Goal("New Goal")
        constraint = Constraint([[Equals(3)]])
        variable = Variable("New Variable", 5)
        goal.add_neighbor(variable, constraint)
        self.assertFalse(goal.is_valid())
