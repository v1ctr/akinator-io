"""
Node Module
"""
import node


class Goal(node.Node):
    """
    Class Class
    """

    def __init__(self, node_id: str, cost=1):
        super().__init__(node_id)
        self._cost: int = cost

    def is_valid(self):
        """
        Checks if all constraints of goal node are satisfied
        :return: boolean
        """
        valid = True
        for variable, constraint in self._neighbors.items():
            valid = valid and constraint.evaluate(variable)
        return valid