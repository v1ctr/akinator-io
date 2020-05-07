"""
Node Module
Contains Node class
"""


class Node:
    """
    Node Class.
    A node consists of an id and neighbors
    """
    _id: str

    def __init__(self, node_id):
        """
        Constructor
        :param node_id: node id. Valid are all immutable data types.
        (Int, String, Tupel,...)
        """
        self._id = node_id
        self._neighbors = {}

    def __str__(self):
        """
        Helper function.
        Better string representation for e.g. str() or print()
        :return: string representation of node
        """
        return str(self._id) + ' Neighbors: ' + str([x.get_id() for x in self._neighbors])

    def add_neighbor(self, neighbor, constraint):
        """
        Adds neighbor to node
        :param neighbor: Neighbor
        :param constraint: Constraint
        :return: void
        """
        self._neighbors[neighbor] = constraint

    def get_neighbors(self):
        """
        Returns all neighbors
        :return: List of neighbors
        """
        return self._neighbors.keys()

    def get_degree(self):
        return len(self._neighbors)

    def get_id(self):
        """
        Returns node id
        :return: Node id as immutable data type. (Int, String, Tupel,...)
        """
        return self._id

    def get_constraint(self, neighbor):
        """
        Constraint for edge between node and neighbor
        :param neighbor: Neighbor
        :return: Constraint
        """
        return self._neighbors[neighbor]

