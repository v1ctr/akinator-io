import unittest
from graph import Graph
from predicates import Equals, LessThan


class GraphTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.graph = Graph()

    def test_variable(self):
        self.graph.create_variable("Variable 1", 5)
        self.assertEqual(self.graph.get_variable("Variable 1").get_value(), 5)

        self.assertEqual(self.graph.get_variable("Variable 2").get_value(), None)

        self.assertEqual(len(self.graph.get_variables()), 2)

    def test_goal(self):
        self.assertTrue(self.graph.create_goal("Goal 1"))
        self.assertTrue(self.graph.get_goal("Goal 2"))

        self.assertEqual(len(self.graph.get_goals()), 2)

    def test_constraint(self):
        self.graph.add_constraint("Goal", "Variable", [[Equals(2)]])
        self.assertEqual(self.graph.get_variable("Variable").get_degree(), 1)
        self.assertEqual(self.graph.get_goal("Goal").get_degree(), 1)
        self.assertFalse(self.graph.get_goal("Goal").is_valid())

    def test_get_most_relevant_variable(self):
        self.graph.add_constraint("Goal 1", "Least Relevant", [[Equals(5)]])
        self.graph.add_constraint("Goal 1", "Most Relevant", [[Equals(5)]])
        self.graph.add_constraint("Goal 2", "Most Relevant", [[LessThan(5)]])

        self.assertEqual(self.graph.get_most_relevant_variable(), self.graph.get_variable("Most Relevant"))
        self.graph.get_variable("Most Relevant").set_value(5)
        print(self.graph.get_most_relevant_variable())
        self.assertEqual(self.graph.get_most_relevant_variable(), self.graph.get_variable("Least Relevant"))

    def test_get_valid_goals(self):
        self.graph.create_goal("Goal 1")
        self.graph.create_goal("Goal 2")
        self.graph.create_goal("Goal 3")

        self.graph.create_variable("Variable 1").set_value(5)

        self.graph.add_constraint("Goal 1", "Variable 1", [[Equals(5)]])
        self.graph.add_constraint("Goal 2", "Variable 1", [[Equals(6)]])

        self.assertEqual(len(self.graph.get_valid_goals()), 2)


