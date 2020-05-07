"""
Variable Module
"""
from typing import Optional
import node


class Variable(node.Node):
    """
    Variable Class
    """

    def __init__(self, name: str, value: object = None) -> object:
        super().__init__(name)
        self._name: str = name
        self._value: Optional[object] = value

    def __str__(self):
        return "{}:{}".format(self._name, self._value)

    def __hash__(self):
        return hash((self._name, self._value))

    def __eq__(self, other):
        if not isinstance(other, Variable):
            # don't attempt to compare against unrelated types
            return NotImplemented

        return isinstance(self._value, type(other.get_value())) and self._value == other.get_value()

    def __lt__(self, other):
        if not isinstance(other, Variable):
            # don't attempt to compare against unrelated types
            return NotImplemented

        return isinstance(self._value, type(other.get_value())) and self._value < other.get_value()

    def __le__(self, other):
        if not isinstance(other, Variable):
            # don't attempt to compare against unrelated types
            return NotImplemented

        return isinstance(self._value, type(other.get_value())) and self._value <= other.get_value()

    def __gt__(self, other):
        if not isinstance(other, Variable):
            # don't attempt to compare against unrelated types
            return NotImplemented

        return isinstance(self._value, type(other.get_value())) and self._value > other.get_value()

    def __ge__(self, other):
        if not isinstance(other, Variable):
            # don't attempt to compare against unrelated types
            return NotImplemented

        return isinstance(self._value, type(other.get_value())) and self._value >= other.get_value()

    def is_empty(self):
        return not bool(self.get_value())

    def set_value(self, value: object):
        self._value = value

    def get_value(self):
        return self._value
