import unittest
from node import Node


class NodeTestCase(unittest.TestCase):

    def test_add_neighbors(self):
        node_1 = Node("first_node")
        node_2 = Node("second_node")
        node_3 = Node("third_node")

        node_1.add_neighbor(node_2, None)
        node_1.add_neighbor(node_3, None)

        self.assertEqual(node_1.get_degree(), 2)