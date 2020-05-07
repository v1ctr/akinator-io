"""
Graph Module
"""
from typing import Dict, List
import heapq

import variable
import predicates
import goal
import constraint


class Graph:
    """
    Graph Class
    A graph consists of nodes and arcs.
    """

    def __init__(self):
        self._variables_dict: Dict[str, variable.Variable] = {}
        self._goals_dict: Dict[str, goal.Goal] = {}
        self._variables_by_degree: List[variable.Variable] = []

    def __str__(self):
        string = ""
        string += "Number of variables: {} \n".format(len(self._variables_dict))
        string += "Number of goals: {} \n".format(len(self._goals_dict))
        return string

    def create_variable(self, name: str, value=None) -> variable.Variable:
        """
        Adds variable node to graph.
        :param name: Variable node name
        :param value: Variable node value
        :return: Variable node
        """
        v = variable.Variable(name, value)
        self._variables_dict[name] = v
        return v

    def get_variable(self, name: str) -> variable.Variable:
        """
        Returns variable node for passed name
        :param name: Variable node name
        :return: Variable node for passed name
        """
        if name not in self._variables_dict:
            return self.create_variable(name)
        return self._variables_dict[name]

    def get_variables(self):
        """
        Returns all variable nodes
        :return: All variable nodes
        """
        return self._variables_dict.values()

    def create_goal(self, node_id: str, cost=1) -> goal.Goal:
        """
        Adds goal node to graph
        :param node_id: Goal node id
        :param cost: Goal cost
        :return: Goal node
        """
        g = goal.Goal(node_id, cost)
        self._goals_dict[node_id] = g
        return g

    def get_goal(self, goal_id: str) -> goal.Goal:
        """
        Returns goal node
        :param goal_id: Goal node id
        :return: Goal node
        """
        if goal_id not in self._goals_dict:
            return self.create_goal(goal_id)
        return self._goals_dict[goal_id]

    def get_goals(self):
        """
        Returns all goals
        :return: All goals
        """
        return self._goals_dict.values()

    def add_constraint(self, goal_id: str, variable_name: str, predicates: List[List[predicates.Predicate]] = None):
        """
        Adds arc with constraint between nodes.
        :param variable_name: Variable name
        :param goal_id: Goal id
        :param predicates: 2D list of predicates
        :return: Constraint
        """
        if predicates is None:
            predicates = [[]]

        v = self.get_variable(variable_name)
        g = self.get_goal(goal_id)
        c = constraint.Constraint(predicates)

        v.add_neighbor(g, c)
        g.add_neighbor(v, c)

        return c

    def get_most_relevant_variable(self):
        """
        Returns most relevant variable node for input prompt.
        :return: Variable node
        """
        self._variables_by_degree = []
        #Variablenknoten mit der größten Grad und noch nicht bestückt finden
        for var in self._variables_dict.values():
            if var.is_empty():
                heapq.heappush(self._variables_by_degree, (var, var.get_degree()))

        return heapq.nlargest(1, self._variables_by_degree, key=lambda e: e[1])[0][0]

    def get_valid_goals(self):
        """
        Returns all valid goals.
        :return: All valid goals.
        """
        valid_goals = []
        for goal in self._goals_dict.values():
            if goal.is_valid():
                valid_goals.append(goal)

        return valid_goals

